#!/usr/bin/env python3
"""
BDD Feature Consolidator

This tool helps consolidate duplicate and similar BDD scenarios while preserving
requirement coverage. It takes the output from the BDD Duplication Analyzer and
guides users through the consolidation process.
"""

import os
import re
import sys
import json
import shutil
import logging
import argparse
import tempfile
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('bdd_feature_consolidator')

@dataclass
class Scenario:
    """Represents a BDD scenario with its attributes."""
    name: str
    tags: List[str]
    content: str
    line_number: int
    feature_path: str = ""
    
    @property
    def requirement_tags(self) -> List[str]:
        """Extract requirement tags."""
        return [tag for tag in self.tags if tag.startswith("@REQ-")]
    
    @property
    def component_tags(self) -> List[str]:
        """Extract component tags."""
        return [tag for tag in self.tags 
                if not tag.startswith("@REQ-") and 
                not tag.startswith("@REL-")]
    
    @property
    def release_tags(self) -> List[str]:
        """Extract release tags."""
        return [tag for tag in self.tags if tag.startswith("@REL-")]

@dataclass
class Feature:
    """Represents a BDD feature file with its attributes."""
    path: str
    name: str
    description: List[str]
    scenarios: List[Scenario] = field(default_factory=list)
    background: Optional[str] = None
    content: str = ""
    
    def add_scenario(self, scenario: Scenario):
        """Add a scenario to the feature."""
        scenario.feature_path = self.path
        self.scenarios.append(scenario)
    
    def remove_scenario(self, scenario: Scenario) -> bool:
        """Remove a scenario from the feature."""
        for i, s in enumerate(self.scenarios):
            if s.name == scenario.name and s.content == scenario.content:
                del self.scenarios[i]
                return True
        return False
    
    def write_to_file(self, output_path: Optional[str] = None) -> str:
        """Write the feature to a file."""
        target_path = output_path or self.path
        with open(target_path, 'w', encoding='utf-8') as f:
            # Write feature header
            f.write(f"Feature: {self.name}\n")
            
            # Write feature description
            for line in self.description:
                f.write(f"  {line}\n")
            
            f.write("\n")
            
            # Write background if exists
            if self.background:
                f.write(f"{self.background}\n\n")
            
            # Write scenarios
            for i, scenario in enumerate(self.scenarios):
                if i > 0:
                    f.write("\n")
                
                # Write tags
                for tag in scenario.tags:
                    f.write(f"{tag}\n")
                
                # Write scenario content
                f.write(f"{scenario.content}\n")
        
        logger.info(f"Wrote feature to {target_path}")
        return target_path

@dataclass
class ConsolidationPlan:
    """Represents a plan for consolidating duplicates."""
    source_scenarios: List[Scenario]
    target_feature: Feature
    target_scenario: Optional[Scenario] = None
    action: str = "merge"  # merge, move, or create
    consolidated_scenario: Optional[Scenario] = None
    
    def execute(self, dry_run: bool = False) -> bool:
        """Execute the consolidation plan."""
        logger.info(f"Executing consolidation plan: {self.action}")
        
        if dry_run:
            logger.info("Dry run mode - not making actual changes")
            return True
        
        if self.action == "merge":
            return self._execute_merge()
        elif self.action == "move":
            return self._execute_move()
        elif self.action == "create":
            return self._execute_create()
        else:
            logger.error(f"Unknown action: {self.action}")
            return False
    
    def _execute_merge(self) -> bool:
        """Merge duplicates into the target scenario."""
        if not self.consolidated_scenario:
            logger.error("No consolidated scenario provided for merge action")
            return False
        
        # Remove original scenarios from their features
        for scenario in self.source_scenarios:
            self._remove_scenario_from_feature(scenario)
        
        if self.target_scenario:
            self._remove_scenario_from_feature(self.target_scenario)
        
        # Add the consolidated scenario to the target feature
        self.target_feature.add_scenario(self.consolidated_scenario)
        
        # Write the updated target feature
        self.target_feature.write_to_file()
        
        logger.info(f"Merged {len(self.source_scenarios)} scenarios into {self.consolidated_scenario.name}")
        return True
    
    def _execute_move(self) -> bool:
        """Move a scenario to a different feature."""
        if not self.source_scenarios:
            logger.error("No source scenarios provided for move action")
            return False
        
        scenario = self.source_scenarios[0]
        
        # Remove the scenario from its original feature
        self._remove_scenario_from_feature(scenario)
        
        # Add the scenario to the target feature
        self.target_feature.add_scenario(scenario)
        
        # Write the updated target feature
        self.target_feature.write_to_file()
        
        logger.info(f"Moved scenario {scenario.name} to {self.target_feature.path}")
        return True
    
    def _execute_create(self) -> bool:
        """Create a new consolidated scenario in the target feature."""
        if not self.consolidated_scenario:
            logger.error("No consolidated scenario provided for create action")
            return False
        
        # Add the new scenario to the target feature
        self.target_feature.add_scenario(self.consolidated_scenario)
        
        # Write the updated target feature
        self.target_feature.write_to_file()
        
        logger.info(f"Created new scenario {self.consolidated_scenario.name} in {self.target_feature.path}")
        return True
    
    def _remove_scenario_from_feature(self, scenario: Scenario) -> bool:
        """Remove a scenario from its feature."""
        if not scenario.feature_path:
            logger.warning(f"Scenario {scenario.name} has no feature path")
            return False
        
        feature_path = scenario.feature_path
        
        # Load the feature
        feature = parse_feature_file(feature_path)
        if not feature:
            logger.error(f"Failed to load feature from {feature_path}")
            return False
        
        # Remove the scenario
        if feature.remove_scenario(scenario):
            # Write the updated feature
            feature.write_to_file()
            logger.info(f"Removed scenario {scenario.name} from {feature_path}")
            return True
        else:
            logger.warning(f"Failed to remove scenario {scenario.name} from {feature_path}")
            return False

class FeatureConsolidator:
    """Main class for consolidating BDD features."""
    
    def __init__(self, 
                 features_dir: str, 
                 duplicates_report: str, 
                 output_dir: Optional[str] = None,
                 dry_run: bool = False):
        self.features_dir = Path(features_dir)
        self.duplicates_report = Path(duplicates_report)
        self.output_dir = Path(output_dir) if output_dir else None
        self.dry_run = dry_run
        self.features: Dict[str, Feature] = {}
        self.duplicates: List[Dict] = []
        self.consolidation_plans: List[ConsolidationPlan] = []
        
    def load_data(self):
        """Load features and duplicates report."""
        logger.info("Loading features and duplicates report")
        
        # Load duplicates report
        self._load_duplicates_report()
        
        # Load features
        feature_files = list(self.features_dir.glob("**/*.feature"))
        logger.info(f"Found {len(feature_files)} feature files")
        
        for feature_file in feature_files:
            feature = parse_feature_file(str(feature_file))
            if feature:
                self.features[str(feature_file)] = feature
    
    def _load_duplicates_report(self):
        """Load the duplicates report."""
        logger.info(f"Loading duplicates report from {self.duplicates_report}")
        
        # For now, we'll parse the markdown report
        # In a real implementation, you might want to use a structured format
        with open(self.duplicates_report, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract duplicate sections
        # This is a simple parser for the markdown report
        # In a real implementation, you'd want a more robust parser
        duplicate_sections = re.findall(
            r'### Duplicate: (.+?)\s+Source: (.+?)\s+Target: (.+?)\s+Similarity: (.+?)%\s+(.+?)(?=### Duplicate:|$)', 
            content, 
            re.DOTALL
        )
        
        for name, source, target, similarity, details in duplicate_sections:
            # Parse source and target files
            source_file = re.search(r'File: (.+?)(?:\s|$)', source)
            target_file = re.search(r'File: (.+?)(?:\s|$)', target)
            
            if source_file and target_file:
                self.duplicates.append({
                    'name': name.strip(),
                    'source_file': source_file.group(1).strip(),
                    'target_file': target_file.group(1).strip(),
                    'similarity': float(similarity),
                    'details': details.strip()
                })
        
        logger.info(f"Loaded {len(self.duplicates)} duplicates")
    
    def create_consolidation_plans(self):
        """Create plans for consolidating duplicates."""
        logger.info("Creating consolidation plans")
        
        for duplicate in self.duplicates:
            source_file = duplicate['source_file']
            target_file = duplicate['target_file']
            
            # Get the features
            source_feature = self.features.get(source_file)
            target_feature = self.features.get(target_file)
            
            if not source_feature or not target_feature:
                logger.warning(f"Could not find features for {source_file} or {target_file}")
                continue
            
            # Find the scenarios in each feature that match the duplicate name
            source_scenarios = [s for s in source_feature.scenarios 
                              if s.name == duplicate['name']]
            target_scenarios = [s for s in target_feature.scenarios 
                              if s.name == duplicate['name']]
            
            if not source_scenarios or not target_scenarios:
                logger.warning(f"Could not find scenarios for duplicate {duplicate['name']}")
                continue
            
            # Create a plan for this duplicate
            plan = self._create_plan_for_duplicate(
                source_scenarios[0], 
                target_scenarios[0] if target_scenarios else None,
                source_feature,
                target_feature,
                duplicate
            )
            
            if plan:
                self.consolidation_plans.append(plan)
    
    def _create_plan_for_duplicate(
        self,
        source_scenario: Scenario,
        target_scenario: Optional[Scenario],
        source_feature: Feature,
        target_feature: Feature,
        duplicate: Dict
    ) -> Optional[ConsolidationPlan]:
        """Create a consolidation plan for a specific duplicate."""
        # Determine the action based on the similarity and whether target exists
        similarity = duplicate['similarity']
        
        if similarity >= 95:  # Almost identical
            # If they're almost identical, we can just move the source to the target
            if target_scenario:
                # Merge tags
                merged_tags = list(set(source_scenario.tags + target_scenario.tags))
                
                # Create a consolidated scenario
                consolidated_scenario = Scenario(
                    name=target_scenario.name,
                    tags=merged_tags,
                    content=target_scenario.content,
                    line_number=target_scenario.line_number
                )
                
                return ConsolidationPlan(
                    source_scenarios=[source_scenario],
                    target_feature=target_feature,
                    target_scenario=target_scenario,
                    action="merge",
                    consolidated_scenario=consolidated_scenario
                )
            else:
                # If no target scenario, just move the source
                return ConsolidationPlan(
                    source_scenarios=[source_scenario],
                    target_feature=target_feature,
                    action="move"
                )
        elif similarity >= 75:  # Similar but not identical
            # For similar scenarios, we need to merge them
            if target_scenario:
                # Merge tags
                merged_tags = list(set(source_scenario.tags + target_scenario.tags))
                
                # For now, use the target scenario as the base
                # In a real implementation, you'd want to merge the contents
                consolidated_scenario = Scenario(
                    name=target_scenario.name,
                    tags=merged_tags,
                    content=target_scenario.content,
                    line_number=target_scenario.line_number
                )
                
                return ConsolidationPlan(
                    source_scenarios=[source_scenario],
                    target_feature=target_feature,
                    target_scenario=target_scenario,
                    action="merge",
                    consolidated_scenario=consolidated_scenario
                )
            else:
                # If no target scenario, just move the source
                return ConsolidationPlan(
                    source_scenarios=[source_scenario],
                    target_feature=target_feature,
                    action="move"
                )
        else:
            # For low similarity, we might not want to merge automatically
            logger.info(f"Similarity too low ({similarity}%) for automatic consolidation of {source_scenario.name}")
            return None
    
    def execute_plans(self):
        """Execute all consolidation plans."""
        logger.info(f"Executing {len(self.consolidation_plans)} consolidation plans")
        
        success_count = 0
        for i, plan in enumerate(self.consolidation_plans):
            logger.info(f"Executing plan {i+1}/{len(self.consolidation_plans)}")
            if plan.execute(dry_run=self.dry_run):
                success_count += 1
        
        logger.info(f"Successfully executed {success_count}/{len(self.consolidation_plans)} plans")
    
    def generate_report(self, output_file: str):
        """Generate a report of the consolidation."""
        logger.info(f"Generating report to {output_file}")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# BDD Feature Consolidation Report\n\n")
            
            f.write("## Summary\n\n")
            f.write(f"- Total duplicates identified: {len(self.duplicates)}\n")
            f.write(f"- Consolidation plans created: {len(self.consolidation_plans)}\n")
            
            # Count by action
            action_counts = {}
            for plan in self.consolidation_plans:
                action_counts[plan.action] = action_counts.get(plan.action, 0) + 1
            
            f.write("- Plans by action:\n")
            for action, count in action_counts.items():
                f.write(f"  - {action}: {count}\n")
            
            # Details of each plan
            f.write("\n## Consolidation Plans\n\n")
            
            for i, plan in enumerate(self.consolidation_plans):
                f.write(f"### Plan {i+1}: {plan.action.capitalize()}\n\n")
                
                if plan.source_scenarios:
                    source_names = [s.name for s in plan.source_scenarios]
                    f.write(f"- Source scenarios: {', '.join(source_names)}\n")
                
                if plan.target_scenario:
                    f.write(f"- Target scenario: {plan.target_scenario.name}\n")
                
                f.write(f"- Target feature: {plan.target_feature.path}\n")
                
                if plan.consolidated_scenario:
                    f.write(f"- Consolidated scenario: {plan.consolidated_scenario.name}\n")
                    f.write(f"- Tags: {', '.join(plan.consolidated_scenario.tags)}\n")
                
                f.write("\n")
        
        logger.info(f"Report generated: {output_file}")

def parse_feature_file(file_path: str) -> Optional[Feature]:
    """Parse a feature file and extract scenarios."""
    logger.info(f"Parsing feature file: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract feature name
    feature_match = re.search(r'Feature:\s*(.+)$', content, re.MULTILINE)
    if not feature_match:
        logger.warning(f"Could not find Feature declaration in {file_path}")
        return None
    
    feature_name = feature_match.group(1).strip()
    
    # Extract feature description
    description_start = feature_match.end()
    description_end = content.find("Background:", description_start)
    if description_end == -1:
        scenario_match = re.search(r'(?:@[^\n]+\n)*\s*Scenario:', content[description_start:])
        if scenario_match:
            description_end = description_start + scenario_match.start()
        else:
            description_end = len(content)
    
    description = content[description_start:description_end].strip().split('\n')
    description = [line.strip() for line in description if line.strip()]
    
    # Extract background if exists
    background = None
    background_match = re.search(r'Background:(.*?)(?=(?:@[^\n]+\n)*\s*Scenario:)', content, re.DOTALL)
    if background_match:
        background = f"Background:{background_match.group(1)}"
    
    # Create the feature
    feature = Feature(
        path=file_path,
        name=feature_name,
        description=description,
        background=background,
        content=content
    )
    
    # Extract scenarios
    scenario_pattern = re.compile(
        r'((?:@[^\n]+\n)+)?\s*(Scenario(?:\s+Outline)?:.*?)'
        r'(?=(?:@[^\n]+\n)+\s*Scenario(?:\s+Outline)?:|$)',
        re.DOTALL
    )
    
    line_number = 1
    for tags_match, scenario_match in scenario_pattern.findall(content):
        # Extract tags
        tags = re.findall(r'@\S+', tags_match)
        
        # Get the scenario content
        scenario_content = scenario_match.strip()
        
        # Extract scenario name
        scenario_name_match = re.match(r'Scenario(?:\s+Outline)?:\s*(.+)$', scenario_content, re.MULTILINE)
        if scenario_name_match:
            scenario_name = scenario_name_match.group(1).strip()
            
            # Create the scenario
            scenario = Scenario(
                name=scenario_name,
                tags=tags,
                content=scenario_content,
                line_number=line_number
            )
            
            # Add to feature
            feature.add_scenario(scenario)
            
            # Update line number (approximate)
            line_number += len(scenario_content.split('\n')) + len(tags)
    
    logger.info(f"Parsed feature {feature_name} with {len(feature.scenarios)} scenarios")
    return feature

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description='Consolidate duplicate BDD scenarios')
    parser.add_argument('--features-dir', required=True, help='Directory containing BDD feature files')
    parser.add_argument('--duplicates-report', required=True, help='Path to duplicates report from bdd_duplication_analyzer.py')
    parser.add_argument('--output-dir', help='Directory for output (if not specified, features will be modified in place)')
    parser.add_argument('--report', help='Path to write consolidation report')
    parser.add_argument('--dry-run', action='store_true', help='Perform a dry run without making changes')
    
    args = parser.parse_args()
    
    consolidator = FeatureConsolidator(
        features_dir=args.features_dir,
        duplicates_report=args.duplicates_report,
        output_dir=args.output_dir,
        dry_run=args.dry_run
    )
    
    consolidator.load_data()
    consolidator.create_consolidation_plans()
    
    if not consolidator.consolidation_plans:
        logger.warning("No consolidation plans created")
        return
    
    consolidator.execute_plans()
    
    if args.report:
        consolidator.generate_report(args.report)
    
    logger.info("BDD feature consolidation complete")

if __name__ == "__main__":
    main() 