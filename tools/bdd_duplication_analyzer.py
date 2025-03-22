#!/usr/bin/env python3
"""
BDD Duplication Analyzer

This tool analyzes BDD feature files to identify duplicate or overlapping features.
It provides reports on:
1. Exact duplicates (same content in different files)
2. Semantic duplicates (similar scenarios in different files)
3. Overlapping features (features that cover similar requirements)
4. Inconsistent tagging (different tags for similar scenarios)

Usage:
    python tools/bdd_duplication_analyzer.py [--output-file REPORT_FILE]
    python tools/bdd_duplication_analyzer.py --generate-merge-plan
"""

import argparse
import os
import re
import difflib
import json
import sys
import datetime
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Set, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("bdd_duplication_analyzer")

# Constants
FEATURES_DIR = Path("tests/bdd/features")
DEFAULT_OUTPUT_FILE = Path("reports/bdd_duplication_report.md")
MERGE_PLAN_FILE = Path("reports/bdd_merge_plan.json")

@dataclass
class Scenario:
    """Represents a BDD scenario with its attributes."""
    name: str
    tags: List[str]
    content: str
    line_number: int

@dataclass
class Feature:
    """Represents a BDD feature file with its attributes."""
    path: Path
    name: str
    description: List[str]
    scenarios: List[Scenario] = field(default_factory=list)
    background: Optional[str] = None
    content: str = ""
    
    def has_tag(self, tag: str) -> bool:
        """Check if the feature has a specific tag."""
        return any(tag in scenario.tags for scenario in self.scenarios)
    
    def get_all_tags(self) -> Set[str]:
        """Get all unique tags used in this feature."""
        tags = set()
        for scenario in self.scenarios:
            tags.update(scenario.tags)
        return tags

@dataclass
class Duplicate:
    """Represents a duplicate or overlapping feature/scenario."""
    type: str  # "exact", "semantic", "overlap", "tag_inconsistency"
    source: Feature
    target: Feature
    similarity: float
    source_scenarios: List[Scenario] = field(default_factory=list)
    target_scenarios: List[Scenario] = field(default_factory=list)
    recommendation: str = ""

class BDDDuplicationAnalyzer:
    """Analyzes BDD feature files for duplication and inconsistencies."""
    
    def __init__(self, features_dir: Path):
        self.features_dir = features_dir
        self.features: List[Feature] = []
        self.duplicates: List[Duplicate] = []
    
    def analyze(self):
        """Run the full analysis."""
        logger.info("Starting BDD duplication analysis")
        self._load_features()
        self._find_exact_duplicates()
        self._find_semantic_duplicates()
        self._find_overlapping_features()
        self._find_tag_inconsistencies()
        logger.info(f"Analysis complete. Found {len(self.duplicates)} issues.")
    
    def _load_features(self):
        """Load all feature files into memory."""
        logger.info(f"Loading feature files from {self.features_dir}")
        if not self.features_dir.exists():
            logger.error(f"Features directory not found: {self.features_dir}")
            sys.exit(1)
            
        feature_files = list(self.features_dir.glob("**/*.feature"))
        logger.info(f"Found {len(feature_files)} feature files")
        
        for file_path in feature_files:
            try:
                self.features.append(self._parse_feature_file(file_path))
            except Exception as e:
                logger.warning(f"Error parsing feature file {file_path}: {e}")
        
        logger.info(f"Loaded {len(self.features)} features with {sum(len(f.scenarios) for f in self.features)} scenarios")
    
    def _parse_feature_file(self, file_path: Path) -> Feature:
        """Parse a feature file into a Feature object."""
        content = file_path.read_text(encoding="utf-8")
        lines = content.splitlines()
        
        # Extract feature name and description
        feature_match = re.search(r"Feature:\s*(.*)", content)
        if not feature_match:
            raise ValueError(f"No feature found in {file_path}")
        
        feature_name = feature_match.group(1).strip()
        
        # Basic parsing - this would be more robust in a production implementation
        description = []
        scenarios = []
        current_scenario = None
        in_background = False
        background_content = []
        
        for i, line in enumerate(lines):
            # Parse feature description
            if i > 0 and line.strip() and not line.strip().startswith("@") and not line.strip().startswith("Background:") and not line.strip().startswith("Scenario:") and not line.strip().startswith("Scenario Outline:"):
                if not current_scenario and not in_background:
                    description.append(line.strip())
            
            # Parse background
            if line.strip().startswith("Background:"):
                in_background = True
                continue
            
            if in_background and line.strip() and not line.strip().startswith("Scenario:") and not line.strip().startswith("@") and not line.strip().startswith("Scenario Outline:"):
                background_content.append(line)
            
            # Parse scenario
            if line.strip().startswith("Scenario:") or line.strip().startswith("Scenario Outline:"):
                in_background = False
                if current_scenario:
                    scenarios.append(current_scenario)
                
                scenario_name = line.split(":", 1)[1].strip()
                current_scenario = Scenario(
                    name=scenario_name,
                    tags=[],
                    content=line + "\n",
                    line_number=i+1
                )
                
                # Look back for tags
                j = i - 1
                while j >= 0 and lines[j].strip().startswith("@"):
                    for tag in re.findall(r"@\S+", lines[j]):
                        current_scenario.tags.append(tag)
                    j -= 1
                
            elif current_scenario:
                current_scenario.content += line + "\n"
        
        # Add the last scenario
        if current_scenario:
            scenarios.append(current_scenario)
        
        background = "\n".join(background_content) if background_content else None
        
        return Feature(
            path=file_path,
            name=feature_name,
            description=description,
            scenarios=scenarios,
            background=background,
            content=content
        )
    
    def _find_exact_duplicates(self):
        """Find exact duplicate scenarios across feature files."""
        logger.info("Looking for exact duplicates")
        
        # Create a dictionary to store scenarios by content
        scenario_dict = {}
        
        # Iterate through all features
        for feature in self.features:
            for scenario in feature.scenarios:
                # Normalize whitespace to avoid false negatives due to whitespace differences
                normalized_content = re.sub(r'\s+', ' ', scenario.content.strip())
                
                # If we haven't seen this scenario before, add it to the dictionary
                if normalized_content not in scenario_dict:
                    scenario_dict[normalized_content] = [(feature, scenario)]
                else:
                    # If we have seen it, add this instance to the list
                    scenario_dict[normalized_content].append((feature, scenario))
        
        # Look for scenarios that appear more than once
        for content, instances in scenario_dict.items():
            if len(instances) > 1:
                # For each duplicate group, create Duplicate objects
                source_feature, source_scenario = instances[0]
                
                for target_feature, target_scenario in instances[1:]:
                    # Skip if both scenarios are in the same feature file
                    if source_feature.path == target_feature.path:
                        continue
                    
                    # Create a Duplicate object
                    duplicate = Duplicate(
                        type="exact",
                        source=source_feature,
                        target=target_feature,
                        similarity=100.0,  # Exact duplicate has 100% similarity
                        source_scenarios=[source_scenario],
                        target_scenarios=[target_scenario],
                        recommendation=f"Consider removing the duplicate scenario '{target_scenario.name}' from '{target_feature.path.name}' or consolidating features."
                    )
                    
                    self.duplicates.append(duplicate)
                    logger.debug(f"Found exact duplicate: {source_feature.path.name}:{source_scenario.name} = {target_feature.path.name}:{target_scenario.name}")
        
        logger.info(f"Found {sum(1 for d in self.duplicates if d.type == 'exact')} exact duplicates")
    
    def _find_semantic_duplicates(self):
        """Find semantically similar scenarios (not exact matches)."""
        logger.info("Looking for semantic duplicates")
        
        # Threshold for similarity (80% similarity is considered a semantic duplicate)
        SIMILARITY_THRESHOLD = 0.8
        
        # Compare each scenario with every other scenario
        for i, feature1 in enumerate(self.features):
            for scenario1 in feature1.scenarios:
                # Only compare with features that come after this one to avoid duplicates
                for feature2 in self.features[i:]:
                    # Skip comparing scenarios within the same feature
                    if feature1.path == feature2.path:
                        continue
                    
                    for scenario2 in feature2.scenarios:
                        # Skip exact duplicates as we've already found them
                        content1 = re.sub(r'\s+', ' ', scenario1.content.strip())
                        content2 = re.sub(r'\s+', ' ', scenario2.content.strip())
                        
                        if content1 == content2:
                            continue
                        
                        # Calculate similarity using difflib
                        similarity = difflib.SequenceMatcher(None, content1, content2).ratio()
                        
                        # If similarity is above threshold, consider it a semantic duplicate
                        if similarity >= SIMILARITY_THRESHOLD:
                            # Create a Duplicate object
                            duplicate = Duplicate(
                                type="semantic",
                                source=feature1,
                                target=feature2,
                                similarity=similarity * 100,  # Convert to percentage
                                source_scenarios=[scenario1],
                                target_scenarios=[scenario2],
                                recommendation=f"Consider standardizing scenarios '{scenario1.name}' and '{scenario2.name}' or consolidating the features."
                            )
                            
                            self.duplicates.append(duplicate)
                            logger.debug(f"Found semantic duplicate: {feature1.path.name}:{scenario1.name} ~ {feature2.path.name}:{scenario2.name} ({similarity:.1%})")
        
        logger.info(f"Found {sum(1 for d in self.duplicates if d.type == 'semantic')} semantic duplicates")
    
    def _find_overlapping_features(self):
        """Find features that overlap in functionality."""
        logger.info("Looking for overlapping features")
        
        # Threshold for feature name similarity
        NAME_SIMILARITY_THRESHOLD = 0.75
        
        # Threshold for overlap in requirements (determined by tags)
        TAG_OVERLAP_THRESHOLD = 0.5
        
        # Compare each feature with every other feature
        for i, feature1 in enumerate(self.features):
            # Only compare with features that come after this one to avoid duplicates
            for feature2 in self.features[i+1:]:
                # Skip comparing a feature with itself
                if feature1.path == feature2.path:
                    continue
                
                # Calculate similarity in feature names
                name_similarity = difflib.SequenceMatcher(None, feature1.name, feature2.name).ratio()
                
                # Get tags from all scenarios in both features
                tags1 = feature1.get_all_tags()
                tags2 = feature2.get_all_tags()
                
                # Calculate tag overlap
                tag_overlap = 0.0
                if tags1 and tags2:  # Only calculate if both have tags
                    common_tags = tags1.intersection(tags2)
                    tag_overlap = len(common_tags) / max(len(tags1), len(tags2))
                
                # If either name similarity or tag overlap is above threshold, consider it an overlap
                if name_similarity >= NAME_SIMILARITY_THRESHOLD or tag_overlap >= TAG_OVERLAP_THRESHOLD:
                    # Determine overlap type and recommendation
                    if name_similarity >= NAME_SIMILARITY_THRESHOLD:
                        overlap_type = "name similarity"
                        recommendation = f"Consider merging these features with similar names or clarifying their distinct purposes."
                    else:
                        overlap_type = "requirement tag overlap"
                        recommendation = f"Consider reorganizing these features as they cover similar requirements."
                    
                    # Create a Duplicate object (of type "overlap")
                    duplicate = Duplicate(
                        type="overlap",
                        source=feature1,
                        target=feature2,
                        similarity=max(name_similarity, tag_overlap) * 100,  # Use the higher similarity as the overall measure
                        source_scenarios=[],  # No specific scenarios to highlight
                        target_scenarios=[],
                        recommendation=recommendation
                    )
                    
                    self.duplicates.append(duplicate)
                    
                    # Log the details
                    common_tag_str = ", ".join(tags1.intersection(tags2)) if tags1 and tags2 else "none"
                    logger.debug(f"Found overlapping features: {feature1.path.name} ~ {feature2.path.name} (overlap type: {overlap_type}, common tags: {common_tag_str})")
        
        logger.info(f"Found {sum(1 for d in self.duplicates if d.type == 'overlap')} overlapping features")
    
    def _find_tag_inconsistencies(self):
        """Find inconsistent tagging across similar scenarios."""
        logger.info("Looking for tag inconsistencies")
        
        # First, analyze tag patterns
        # Look for scenarios with similar content but different tags
        
        # Group scenarios by name pattern to find similar scenarios
        scenario_name_groups = {}
        
        # Extract standard tag patterns
        req_pattern = re.compile(r'@REQ-[A-Za-z]+-\d+')
        rel_pattern = re.compile(r'@REL-\d+')
        
        for feature in self.features:
            for scenario in feature.scenarios:
                # Normalize the scenario name to create a key
                # Remove common words and special characters, convert to lowercase
                normalized_name = re.sub(r'\b(the|a|an|in|on|for|to|with|and|or|of|that|this|as)\b', '', 
                                        scenario.name.lower())
                normalized_name = re.sub(r'[^\w\s]', '', normalized_name)
                normalized_name = re.sub(r'\s+', ' ', normalized_name).strip()
                
                if not normalized_name:  # Skip if normalization results in empty string
                    continue
                
                if normalized_name not in scenario_name_groups:
                    scenario_name_groups[normalized_name] = []
                
                scenario_name_groups[normalized_name].append((feature, scenario))
        
        # Now check each group for tag inconsistencies
        for name, scenarios in scenario_name_groups.items():
            if len(scenarios) <= 1:
                continue  # Skip groups with only one scenario
            
            # Analyze tags in this group
            req_tags_present = False
            rel_tags_present = False
            inconsistent_tags = False
            req_tags = set()
            rel_tags = set()
            
            for feature, scenario in scenarios:
                # Check for requirement tags
                req_tags_in_scenario = [tag for tag in scenario.tags if req_pattern.match(tag)]
                if req_tags_in_scenario:
                    req_tags_present = True
                    req_tags.update(req_tags_in_scenario)
                
                # Check for release tags
                rel_tags_in_scenario = [tag for tag in scenario.tags if rel_pattern.match(tag)]
                if rel_tags_in_scenario:
                    rel_tags_present = True
                    rel_tags.update(rel_tags_in_scenario)
            
            # Check for inconsistencies
            for feature, scenario in scenarios:
                req_tags_in_scenario = [tag for tag in scenario.tags if req_pattern.match(tag)]
                rel_tags_in_scenario = [tag for tag in scenario.tags if rel_pattern.match(tag)]
                
                # If some scenarios have REQ tags but this one doesn't, that's inconsistent
                if req_tags_present and not req_tags_in_scenario:
                    inconsistent_tags = True
                
                # If some scenarios have REL tags but this one doesn't, that's inconsistent
                if rel_tags_present and not rel_tags_in_scenario:
                    inconsistent_tags = True
                
                # If this scenario has different REQ tags than others, that's inconsistent
                if req_tags_in_scenario and req_tags_in_scenario[0] not in req_tags:
                    inconsistent_tags = True
            
            # If we found inconsistencies, create Duplicate objects for each pair
            if inconsistent_tags and len(scenarios) > 1:
                base_feature, base_scenario = scenarios[0]
                
                for feature, scenario in scenarios[1:]:
                    # Create a description of the inconsistency
                    base_tags = set(base_scenario.tags)
                    current_tags = set(scenario.tags)
                    
                    missing_tags = base_tags - current_tags
                    extra_tags = current_tags - base_tags
                    
                    inconsistency_desc = []
                    if missing_tags:
                        inconsistency_desc.append(f"Missing tags: {', '.join(missing_tags)}")
                    if extra_tags:
                        inconsistency_desc.append(f"Extra tags: {', '.join(extra_tags)}")
                    
                    recommendation = "Consider standardizing tags across similar scenarios."
                    if req_tags_present:
                        recommendation += f" Requirement tags found: {', '.join(req_tags)}."
                    if rel_tags_present:
                        recommendation += f" Release tags found: {', '.join(rel_tags)}."
                    
                    # Create a Duplicate object
                    duplicate = Duplicate(
                        type="tag_inconsistency",
                        source=base_feature,
                        target=feature,
                        similarity=70.0,  # Using a fixed similarity score for tag inconsistencies
                        source_scenarios=[base_scenario],
                        target_scenarios=[scenario],
                        recommendation=recommendation
                    )
                    
                    self.duplicates.append(duplicate)
                    logger.debug(f"Found tag inconsistency: {base_feature.path.name}:{base_scenario.name} vs {feature.path.name}:{scenario.name}")
        
        logger.info(f"Found {sum(1 for d in self.duplicates if d.type == 'tag_inconsistency')} tag inconsistencies")
    
    def generate_report(self, output_file: Path) -> str:
        """Generate a Markdown report of the duplication analysis."""
        logger.info(f"Generating report to {output_file}")
        
        now = datetime.datetime.now()
        report = f"# BDD Duplication Analysis Report\n\n"
        report += f"Generated on: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        report += f"## Summary\n\n"
        report += f"- Total feature files analyzed: {len(self.features)}\n"
        report += f"- Total scenarios analyzed: {sum(len(f.scenarios) for f in self.features)}\n"
        report += f"- Exact duplicates found: {sum(1 for d in self.duplicates if d.type == 'exact')}\n"
        report += f"- Semantic duplicates found: {sum(1 for d in self.duplicates if d.type == 'semantic')}\n"
        report += f"- Overlapping features found: {sum(1 for d in self.duplicates if d.type == 'overlap')}\n"
        report += f"- Tag inconsistencies found: {sum(1 for d in self.duplicates if d.type == 'tag_inconsistency')}\n\n"
        
        # Details for each type of issue
        for issue_type in ["exact", "semantic", "overlap", "tag_inconsistency"]:
            issues = [d for d in self.duplicates if d.type == issue_type]
            if not issues:
                continue
            
            type_name = {
                "exact": "Exact Duplicates",
                "semantic": "Semantic Duplicates",
                "overlap": "Overlapping Features",
                "tag_inconsistency": "Tag Inconsistencies"
            }[issue_type]
            
            report += f"## {type_name}\n\n"
            
            for i, issue in enumerate(issues, 1):
                report += f"### {i}. {issue.source.name} vs {issue.target.name}\n\n"
                report += f"- Source: `{issue.source.path.relative_to(self.features_dir)}`\n"
                report += f"- Target: `{issue.target.path.relative_to(self.features_dir)}`\n"
                report += f"- Similarity: {issue.similarity:.1f}%\n"
                report += f"- Recommendation: {issue.recommendation}\n\n"
                
                # Add more details depending on issue type
                if issue_type in ["exact", "semantic"]:
                    for j, (src, tgt) in enumerate(zip(issue.source_scenarios, issue.target_scenarios), 1):
                        report += f"#### Scenario Pair {j}\n\n"
                        report += f"**Source Scenario** (line {src.line_number}):\n```gherkin\n{src.content}```\n\n"
                        report += f"**Target Scenario** (line {tgt.line_number}):\n```gherkin\n{tgt.content}```\n\n"
                
                report += "---\n\n"
        
        # Write report to file
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(report, encoding="utf-8")
        
        return report
    
    def generate_merge_plan(self, output_file: Path = MERGE_PLAN_FILE):
        """Generate a merge plan for duplicate features."""
        logger.info(f"Generating merge plan to {output_file}")
        
        now = datetime.datetime.now()
        merge_plan = {
            "generated_date": now.isoformat(),
            "merge_groups": []
        }
        
        # Group duplicates by feature
        feature_groups = {}
        for duplicate in self.duplicates:
            if duplicate.type in ["exact", "semantic", "overlap"]:
                key = duplicate.source.path.stem
                if key not in feature_groups:
                    feature_groups[key] = []
                feature_groups[key].append(duplicate)
        
        # Create merge groups
        for group_name, duplicates in feature_groups.items():
            features = set()
            for duplicate in duplicates:
                features.add(str(duplicate.source.path))
                features.add(str(duplicate.target.path))
            
            merge_groups = {
                "name": group_name,
                "features": sorted(list(features)),
                "recommended_target": None,  # Would be determined by a more sophisticated algorithm
                "duplicates": [
                    {
                        "source": str(d.source.path),
                        "target": str(d.target.path),
                        "type": d.type,
                        "similarity": d.similarity
                    }
                    for d in duplicates
                ]
            }
            
            merge_plan["merge_groups"].append(merge_groups)
        
        # Write merge plan to file
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(merge_plan, f, indent=2)
        
        return merge_plan

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Analyze BDD feature files for duplication and inconsistencies.")
    parser.add_argument("--output-file", "-o", type=str, default=str(DEFAULT_OUTPUT_FILE),
                        help=f"Output file for the analysis report (default: {DEFAULT_OUTPUT_FILE})")
    parser.add_argument("--generate-merge-plan", "-p", action="store_true",
                        help="Generate a merge plan for duplicate features")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Enable verbose logging")
    
    return parser.parse_args()

def main():
    """Main entry point."""
    args = parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    output_file = Path(args.output_file)
    
    analyzer = BDDDuplicationAnalyzer(FEATURES_DIR)
    analyzer.analyze()
    analyzer.generate_report(output_file)
    
    if args.generate_merge_plan:
        analyzer.generate_merge_plan()
    
    logger.info("Analysis complete.")
    
    if not analyzer.duplicates:
        logger.info("No duplicates or inconsistencies found.")
        return 0
    
    logger.info(f"Found {len(analyzer.duplicates)} issues. See report at {output_file}")
    return 0

if __name__ == "__main__":
    sys.exit(main()) 