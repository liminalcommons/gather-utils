#!/usr/bin/env python3
"""
BDD Tag Standardizer

This tool helps standardize tags across BDD feature files according to the defined
conventions. It analyzes feature files and applies consistent tagging patterns,
ensuring requirement traceability and feature organization.
"""

import os
import re
import sys
import json
import logging
import argparse
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional, Tuple, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('bdd_tag_standardizer')

# Tag patterns as defined in BDD conventions
TAG_PATTERNS = {
    "requirement": r"@REQ-[A-Za-z]+-\d+",
    "release": r"@REL-\d+",
    "component": r"@[A-Za-z]+",
    "process": r"@PROC-[A-Za-z]+"
}

@dataclass
class Scenario:
    """Represents a BDD scenario with its attributes."""
    name: str
    content: str
    tags: List[str] = field(default_factory=list)
    line_number: int = 0
    feature_path: str = ""
    
    @property
    def requirement_tags(self) -> List[str]:
        """Extract requirement tags."""
        return [tag for tag in self.tags if re.match(TAG_PATTERNS["requirement"], tag)]
    
    @property
    def release_tags(self) -> List[str]:
        """Extract release tags."""
        return [tag for tag in self.tags if re.match(TAG_PATTERNS["release"], tag)]
    
    @property
    def component_tags(self) -> List[str]:
        """Extract component tags."""
        return [tag for tag in self.tags
                if not any(re.match(pattern, tag) for pattern in 
                          [TAG_PATTERNS["requirement"], TAG_PATTERNS["release"], TAG_PATTERNS["process"]])]
    
    @property
    def process_tags(self) -> List[str]:
        """Extract process tags."""
        return [tag for tag in self.tags if re.match(TAG_PATTERNS["process"], tag)]

@dataclass
class Feature:
    """Represents a BDD feature file with its attributes."""
    path: Path
    name: str
    content: str
    tags: List[str] = field(default_factory=list)
    scenarios: List[Scenario] = field(default_factory=list)
    background: Optional[str] = None
    description: str = ""
    modified: bool = False
    
    def add_scenario(self, scenario: Scenario):
        """Add a scenario to the feature."""
        scenario.feature_path = str(self.path)
        self.scenarios.append(scenario)

@dataclass
class TagModification:
    """Represents a tag modification to be applied."""
    scenario_name: str
    feature_path: Path
    old_tags: List[str]
    new_tags: List[str]
    action: str  # add, remove, replace
    reason: str = ""

class TagStandardizer:
    """Main class for standardizing BDD tags."""
    
    def __init__(self, 
                 features_dir: str,
                 output_dir: Optional[str] = None,
                 tag_mapping_file: Optional[str] = None,
                 component_map_file: Optional[str] = None,
                 dry_run: bool = False):
        self.features_dir = Path(features_dir)
        self.output_dir = Path(output_dir) if output_dir else None
        self.tag_mapping_file = Path(tag_mapping_file) if tag_mapping_file else None
        self.component_map_file = Path(component_map_file) if component_map_file else None
        self.dry_run = dry_run
        self.features: List[Feature] = []
        self.tag_modifications: List[TagModification] = []
        self.tag_mapping: Dict[str, str] = {}
        self.component_map: Dict[str, str] = {}
        
        # Load tag mapping if provided
        if self.tag_mapping_file and self.tag_mapping_file.exists():
            self._load_tag_mapping()
        
        # Load component mapping if provided
        if self.component_map_file and self.component_map_file.exists():
            self._load_component_map()
    
    def _load_tag_mapping(self):
        """Load tag mapping from file."""
        logger.info(f"Loading tag mapping from {self.tag_mapping_file}")
        
        try:
            with open(self.tag_mapping_file, 'r', encoding='utf-8') as f:
                self.tag_mapping = json.load(f)
                
            logger.info(f"Loaded {len(self.tag_mapping)} tag mappings")
        except Exception as e:
            logger.error(f"Failed to load tag mapping: {e}")
            self.tag_mapping = {}
    
    def _load_component_map(self):
        """Load component mapping from file."""
        logger.info(f"Loading component mapping from {self.component_map_file}")
        
        try:
            with open(self.component_map_file, 'r', encoding='utf-8') as f:
                self.component_map = json.load(f)
                
            logger.info(f"Loaded {len(self.component_map)} component mappings")
        except Exception as e:
            logger.error(f"Failed to load component mapping: {e}")
            self.component_map = {}
    
    def scan_features(self):
        """Scan the features directory for feature files."""
        logger.info(f"Scanning features directory: {self.features_dir}")
        
        feature_files = list(self.features_dir.glob("**/*.feature"))
        logger.info(f"Found {len(feature_files)} feature files")
        
        for feature_file in feature_files:
            feature = self._parse_feature_file(feature_file)
            if feature:
                self.features.append(feature)
    
    def _parse_feature_file(self, file_path: Path) -> Optional[Feature]:
        """Parse a feature file and extract scenarios with tags."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract feature name
            feature_match = re.search(r'Feature:\s*(.+?)$', content, re.MULTILINE)
            if not feature_match:
                logger.warning(f"Could not find Feature declaration in {file_path}")
                return None
            
            feature_name = feature_match.group(1).strip()
            
            # Extract feature description
            description_match = re.search(r'Feature:.*?\n(.*?)(?=\n\s*(?:Background:|Scenario:|@))', 
                                          content, re.DOTALL)
            description = description_match.group(1).strip() if description_match else ""
            
            # Extract feature-level tags
            feature_tags = []
            tags_match = re.search(r'((?:@[^\n]+\n)+)Feature:', content)
            if tags_match:
                feature_tags = re.findall(r'@\S+', tags_match.group(1))
            
            # Create the feature
            feature = Feature(
                path=file_path,
                name=feature_name,
                content=content,
                tags=feature_tags,
                description=description
            )
            
            # Extract background if exists
            background_match = re.search(r'Background:(.*?)(?=(?:@[^\n]+\n)*\s*Scenario:)', content, re.DOTALL)
            if background_match:
                feature.background = f"Background:{background_match.group(1)}"
            
            # Extract scenarios
            scenario_matches = re.finditer(
                r'(?:(?:@[^\n]+\n)+)?\s*(Scenario(?:\s+Outline)?:\s*(.+?)$.*?)(?=\n\s*(?:@|Scenario|$))',
                content, re.DOTALL | re.MULTILINE
            )
            
            line_count = 1
            for scenario_match in scenario_matches:
                scenario_content = scenario_match.group(1)
                scenario_name = scenario_match.group(2).strip()
                
                # Extract scenario tags
                scenario_tags = []
                tag_section = content[:scenario_match.start()]
                last_tag_section = tag_section.rfind('@')
                
                if last_tag_section != -1:
                    tag_lines = tag_section[last_tag_section:].split('\n')
                    for line in tag_lines:
                        if '@' in line:
                            tags = re.findall(r'@\S+', line)
                            scenario_tags.extend(tags)
                
                # Approximate line number
                line_count += tag_section.count('\n') - tag_section[:last_tag_section].count('\n') if last_tag_section != -1 else 0
                
                # Create scenario
                scenario = Scenario(
                    name=scenario_name,
                    content=scenario_content.strip(),
                    tags=scenario_tags,
                    line_number=line_count,
                    feature_path=str(file_path)
                )
                
                # Add to feature
                feature.add_scenario(scenario)
                
                # Update line count for next scenario
                line_count += scenario_content.count('\n') + 1
            
            logger.info(f"Parsed feature {feature_name} with {len(feature.scenarios)} scenarios")
            return feature
        
        except Exception as e:
            logger.error(f"Error parsing feature file {file_path}: {e}")
            return None
    
    def analyze_tags(self):
        """Analyze tags across all features and identify issues."""
        logger.info("Analyzing tags across all features")
        
        # Track statistics
        stats = {
            "missing_requirement_tags": 0,
            "missing_release_tags": 0,
            "inconsistent_req_tags": 0,
            "inconsistent_component_tags": 0,
            "non_standard_tags": 0
        }
        
        # Build tag frequency map
        tag_frequency = {}
        
        for feature in self.features:
            # Check feature-level tags
            feature_modifications = self._analyze_feature_tags(feature)
            if feature_modifications:
                self.tag_modifications.extend(feature_modifications)
            
            # Check scenario-level tags
            for scenario in feature.scenarios:
                # Track tag frequency
                for tag in scenario.tags:
                    if tag not in tag_frequency:
                        tag_frequency[tag] = 0
                    tag_frequency[tag] += 1
                
                # Analyze scenario tags
                modifications = self._analyze_scenario_tags(scenario, feature)
                if modifications:
                    self.tag_modifications.extend(modifications)
                    
                    # Update statistics
                    for mod in modifications:
                        if "missing requirement tag" in mod.reason:
                            stats["missing_requirement_tags"] += 1
                        elif "missing release tag" in mod.reason:
                            stats["missing_release_tags"] += 1
                        elif "non-standard requirement tag" in mod.reason:
                            stats["inconsistent_req_tags"] += 1
                        elif "non-standard component tag" in mod.reason:
                            stats["inconsistent_component_tags"] += 1
                        elif "non-standard tag" in mod.reason:
                            stats["non_standard_tags"] += 1
        
        # Save tag frequency for analysis
        if not self.dry_run:
            self._save_tag_frequency(tag_frequency)
        
        logger.info(f"Analysis complete: Found {len(self.tag_modifications)} tag modifications needed")
        logger.info(f"Statistics: {stats}")
    
    def _analyze_feature_tags(self, feature: Feature) -> List[TagModification]:
        """Analyze tags at the feature level."""
        modifications = []
        
        # For now, we're focusing on scenario-level tags
        # Feature-level tag modifications could be added here in the future
        
        return modifications
    
    def _analyze_scenario_tags(self, scenario: Scenario, feature: Feature) -> List[TagModification]:
        """Analyze tags at the scenario level."""
        modifications = []
        
        # Check for missing requirement tags
        if not scenario.requirement_tags:
            # Generate default requirement tag
            default_req_tag = self._generate_requirement_tag(scenario, feature)
            
            modifications.append(TagModification(
                scenario_name=scenario.name,
                feature_path=feature.path,
                old_tags=scenario.tags.copy(),
                new_tags=scenario.tags + [default_req_tag],
                action="add",
                reason=f"Added missing requirement tag: {default_req_tag}"
            ))
        
        # Check for missing release tags
        if not scenario.release_tags:
            # Generate default release tag
            default_rel_tag = "@REL-1"  # Default to first release
            
            modifications.append(TagModification(
                scenario_name=scenario.name,
                feature_path=feature.path,
                old_tags=scenario.tags.copy(),
                new_tags=scenario.tags + [default_rel_tag],
                action="add",
                reason=f"Added missing release tag: {default_rel_tag}"
            ))
        
        # Check for non-standard requirement tags
        for tag in scenario.requirement_tags:
            if not re.match(TAG_PATTERNS["requirement"], tag):
                # Find replacement in mapping
                replacement = self._find_tag_replacement(tag, "requirement")
                
                if replacement:
                    new_tags = [t if t != tag else replacement for t in scenario.tags]
                    
                    modifications.append(TagModification(
                        scenario_name=scenario.name,
                        feature_path=feature.path,
                        old_tags=scenario.tags.copy(),
                        new_tags=new_tags,
                        action="replace",
                        reason=f"Replaced non-standard requirement tag: {tag} -> {replacement}"
                    ))
        
        # Check for non-standard component tags
        for tag in scenario.component_tags:
            if not re.match(r"@[A-Za-z]+", tag):
                # Find replacement in mapping
                replacement = self._find_tag_replacement(tag, "component")
                
                if replacement:
                    new_tags = [t if t != tag else replacement for t in scenario.tags]
                    
                    modifications.append(TagModification(
                        scenario_name=scenario.name,
                        feature_path=feature.path,
                        old_tags=scenario.tags.copy(),
                        new_tags=new_tags,
                        action="replace",
                        reason=f"Replaced non-standard component tag: {tag} -> {replacement}"
                    ))
        
        # Add domain tag if missing
        domain = self._extract_domain_from_path(feature.path)
        domain_tag = f"@{domain.upper()}"
        
        if domain and domain_tag not in scenario.tags:
            modifications.append(TagModification(
                scenario_name=scenario.name,
                feature_path=feature.path,
                old_tags=scenario.tags.copy(),
                new_tags=scenario.tags + [domain_tag],
                action="add",
                reason=f"Added domain tag: {domain_tag}"
            ))
        
        return modifications
    
    def _generate_requirement_tag(self, scenario: Scenario, feature: Feature) -> str:
        """Generate a default requirement tag."""
        # Extract domain from feature path
        domain = self._extract_domain_from_path(feature.path)
        
        # Generate a simple numeric ID based on scenario name hash
        scenario_id = abs(hash(scenario.name)) % 1000
        
        # Create a REQ tag
        return f"@REQ-{domain.upper()}-{scenario_id}"
    
    def _extract_domain_from_path(self, feature_path: Path) -> str:
        """Extract domain from feature path."""
        # Try to extract from filename
        filename = feature_path.stem
        parts = filename.split('_', 1)
        
        if parts:
            domain = parts[0].lower()
            
            # Map to standard domains
            if domain in ["api", "cli", "core", "model", "models", "process"]:
                return domain
            
            # Check if we have it in our component map
            if domain in self.component_map:
                return self.component_map[domain]
        
        # Check path components
        for part in feature_path.parts:
            part_lower = part.lower()
            if part_lower in ["api", "cli", "core", "model", "models", "process"]:
                return part_lower
        
        # Default to core if no domain identified
        return "core"
    
    def _find_tag_replacement(self, original_tag: str, tag_type: str) -> Optional[str]:
        """Find a replacement for a non-standard tag."""
        # Check if we have a direct mapping
        if original_tag in self.tag_mapping:
            return self.tag_mapping[original_tag]
        
        # Try to generate a replacement based on tag type
        if tag_type == "requirement":
            # Extract any numbers that might be IDs
            id_match = re.search(r"(\d+)", original_tag)
            if id_match:
                req_id = id_match.group(1)
                # Try to find domain
                domain_match = re.search(r"@REQ[-_]?([A-Za-z]+)", original_tag)
                domain = domain_match.group(1) if domain_match else "CORE"
                
                return f"@REQ-{domain.upper()}-{req_id}"
        
        elif tag_type == "component":
            # Extract letter sequence
            comp_match = re.search(r"@([A-Za-z]+)", original_tag)
            if comp_match:
                component = comp_match.group(1)
                return f"@{component.upper()}"
        
        # No replacement found
        return None
    
    def _save_tag_frequency(self, tag_frequency: Dict[str, int]):
        """Save tag frequency to a file for analysis."""
        output_dir = self.output_dir or self.features_dir
        stats_file = output_dir / "tag_frequency.json"
        
        # Sort tags by frequency
        sorted_tags = {k: v for k, v in sorted(tag_frequency.items(), key=lambda item: item[1], reverse=True)}
        
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(sorted_tags, f, indent=2)
        
        logger.info(f"Saved tag frequency to {stats_file}")
    
    def apply_modifications(self):
        """Apply tag modifications to feature files."""
        logger.info(f"Applying {len(self.tag_modifications)} tag modifications")
        
        if self.dry_run:
            logger.info("Dry run mode - not making actual changes")
            return
        
        # Group modifications by feature path
        modifications_by_feature: Dict[str, List[TagModification]] = {}
        
        for mod in self.tag_modifications:
            feature_path = str(mod.feature_path)
            if feature_path not in modifications_by_feature:
                modifications_by_feature[feature_path] = []
            
            modifications_by_feature[feature_path].append(mod)
        
        # Apply modifications to each feature
        for feature_path, mods in modifications_by_feature.items():
            # Find the feature
            feature = next((f for f in self.features if str(f.path) == feature_path), None)
            if not feature:
                logger.warning(f"Could not find feature for path {feature_path}")
                continue
            
            # Apply modifications to the feature's content
            self._apply_to_feature(feature, mods)
    
    def _apply_to_feature(self, feature: Feature, modifications: List[TagModification]):
        """Apply modifications to a specific feature."""
        logger.info(f"Applying {len(modifications)} modifications to {feature.path}")
        
        # Group modifications by scenario name
        mods_by_scenario: Dict[str, List[TagModification]] = {}
        
        for mod in modifications:
            if mod.scenario_name not in mods_by_scenario:
                mods_by_scenario[mod.scenario_name] = []
            
            mods_by_scenario[mod.scenario_name].append(mod)
        
        # Get the original content
        content = feature.content
        
        # Process each scenario
        for scenario in feature.scenarios:
            # Check if we have modifications for this scenario
            if scenario.name not in mods_by_scenario:
                continue
            
            # Get all modifications for this scenario
            scenario_mods = mods_by_scenario[scenario.name]
            
            # Find the scenario's tag section in the content
            scenario_position = content.find(f"Scenario: {scenario.name}")
            scenario_outline_position = content.find(f"Scenario Outline: {scenario.name}")
            
            position = scenario_position if scenario_position != -1 else scenario_outline_position
            
            if position == -1:
                logger.warning(f"Could not find scenario {scenario.name} in content")
                continue
            
            # Find the tag section before this scenario
            tag_start = content.rfind('@', 0, position)
            
            if tag_start == -1:
                # No existing tags, insert new ones
                # First, find the line where the scenario starts
                line_start = content.rfind('\n', 0, position) + 1
                
                # Determine final set of tags
                final_tags = self._compute_final_tags(scenario.tags, scenario_mods)
                
                # Create tag section
                tag_section = '\n'.join(final_tags) + '\n'
                
                # Insert the tags
                content = content[:line_start] + tag_section + content[line_start:]
            else:
                # Find the end of the tag section
                tag_end = content.find('\n', tag_start)
                while content.find('@', tag_end + 1, position) != -1:
                    tag_end = content.find('\n', tag_end + 1)
                
                # Extract existing tag section
                tag_section = content[tag_start:tag_end]
                
                # Determine final set of tags
                final_tags = self._compute_final_tags(scenario.tags, scenario_mods)
                
                # Create new tag section
                new_tag_section = '\n'.join(final_tags)
                
                # Replace the tag section
                content = content[:tag_start] + new_tag_section + content[tag_end:]
        
        # Save the modified content
        output_path = self.output_dir / feature.path.name if self.output_dir else feature.path
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"Saved modified feature to {output_path}")
    
    def _compute_final_tags(self, original_tags: List[str], 
                           modifications: List[TagModification]) -> List[str]:
        """Compute the final set of tags after applying all modifications."""
        current_tags = original_tags.copy()
        
        for mod in modifications:
            if mod.action == "add":
                # Add any tags that aren't already present
                for tag in mod.new_tags:
                    if tag not in current_tags:
                        current_tags.append(tag)
            
            elif mod.action == "remove":
                # Remove specified tags
                current_tags = [tag for tag in current_tags if tag not in mod.old_tags]
            
            elif mod.action == "replace":
                # Replace specific tags
                tag_mapping = {old: new for old, new in zip(mod.old_tags, mod.new_tags) 
                              if old != new}
                
                current_tags = [tag_mapping.get(tag, tag) for tag in current_tags]
        
        return current_tags
    
    def generate_report(self, output_file: str):
        """Generate a report of the tag standardization."""
        logger.info(f"Generating report to {output_file}")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# BDD Tag Standardization Report\n\n")
            
            f.write("## Summary\n\n")
            f.write(f"- Total features analyzed: {len(self.features)}\n")
            f.write(f"- Total scenarios analyzed: {sum(len(feature.scenarios) for feature in self.features)}\n")
            f.write(f"- Tag modifications: {len(self.tag_modifications)}\n\n")
            
            # Count modifications by type
            action_counts = {}
            reason_counts = {}
            
            for mod in self.tag_modifications:
                action_counts[mod.action] = action_counts.get(mod.action, 0) + 1
                
                # Simplified reason category
                category = "requirement" if "requirement" in mod.reason else \
                          "release" if "release" in mod.reason else \
                          "component" if "component" in mod.reason else \
                          "domain" if "domain" in mod.reason else \
                          "other"
                
                reason_counts[category] = reason_counts.get(category, 0) + 1
            
            f.write("### Modifications by Action\n\n")
            for action, count in action_counts.items():
                f.write(f"- {action}: {count}\n")
            
            f.write("\n### Modifications by Category\n\n")
            for category, count in reason_counts.items():
                f.write(f"- {category}: {count}\n")
            
            # Details of modifications
            f.write("\n## Modification Details\n\n")
            
            # Group by feature
            mods_by_feature = {}
            for mod in self.tag_modifications:
                feature_path = str(mod.feature_path)
                if feature_path not in mods_by_feature:
                    mods_by_feature[feature_path] = []
                
                mods_by_feature[feature_path].append(mod)
            
            # List modifications by feature
            for feature_path, mods in mods_by_feature.items():
                feature = next((f for f in self.features if str(f.path) == feature_path), None)
                if not feature:
                    continue
                
                f.write(f"### Feature: {feature.name}\n\n")
                f.write(f"Path: `{feature_path}`\n\n")
                
                for i, mod in enumerate(mods):
                    f.write(f"#### Modification {i+1}: {mod.action.capitalize()}\n\n")
                    f.write(f"Scenario: {mod.scenario_name}\n\n")
                    f.write(f"Reason: {mod.reason}\n\n")
                    
                    if mod.old_tags:
                        f.write("Old tags:\n```\n")
                        for tag in mod.old_tags:
                            f.write(f"{tag}\n")
                        f.write("```\n\n")
                    
                    if mod.new_tags:
                        f.write("New tags:\n```\n")
                        for tag in mod.new_tags:
                            f.write(f"{tag}\n")
                        f.write("```\n\n")
                
                f.write("\n")
            
            # Best practices section
            f.write("## Best Practices\n\n")
            f.write("When adding tags to BDD features, follow these guidelines:\n\n")
            
            f.write("1. **Requirement Tags**: Always include a requirement tag in the format `@REQ-[domain]-[id]`\n")
            f.write("   - Example: `@REQ-API-123`\n\n")
            
            f.write("2. **Release Tags**: Include a release tag in the format `@REL-[version]`\n")
            f.write("   - Example: `@REL-1`\n\n")
            
            f.write("3. **Component Tags**: Include at least one component tag\n")
            f.write("   - Example: `@API`, `@CLI`, `@MODEL`, etc.\n\n")
            
            f.write("4. **Process Tags**: Include process tags when relevant in the format `@PROC-[process]`\n")
            f.write("   - Example: `@PROC-DEPLOY`, `@PROC-SECURITY`\n\n")
            
            f.write("5. **Consistency**: Use consistent capitalization and formatting\n\n")
            
            f.write("6. **One Tag Per Line**: Place each tag on its own line for readability\n\n")
        
        logger.info(f"Report generated: {output_file}")

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description='Standardize tags across BDD feature files')
    parser.add_argument('--features-dir', required=True, help='Directory containing BDD feature files')
    parser.add_argument('--output-dir', help='Directory for output (if not specified, features will be modified in place)')
    parser.add_argument('--tag-mapping', help='JSON file with tag mappings')
    parser.add_argument('--component-map', help='JSON file with component mappings')
    parser.add_argument('--report', help='Path to write standardization report')
    parser.add_argument('--dry-run', action='store_true', help='Perform a dry run without making changes')
    
    args = parser.parse_args()
    
    standardizer = TagStandardizer(
        features_dir=args.features_dir,
        output_dir=args.output_dir,
        tag_mapping_file=args.tag_mapping,
        component_map_file=args.component_map,
        dry_run=args.dry_run
    )
    
    standardizer.scan_features()
    standardizer.analyze_tags()
    
    if not standardizer.tag_modifications:
        logger.info("No tag modifications required")
    else:
        standardizer.apply_modifications()
    
    if args.report:
        standardizer.generate_report(args.report)
    
    logger.info("BDD tag standardization complete")

if __name__ == "__main__":
    main() 