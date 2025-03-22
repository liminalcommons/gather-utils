#!/usr/bin/env python3
"""
BDD Feature Reorganizer

This tool helps reorganize BDD feature files according to the defined directory
structure conventions. It analyzes feature files and moves them to the appropriate
locations based on their domain, functionality, and tags.
"""

import os
import re
import sys
import json
import shutil
import logging
import argparse
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('bdd_feature_reorganizer')

# Directory structure as defined in BDD conventions
STANDARD_DIRS = {
    "core": "Core functionality features",
    "cli": "Command-line interface features",
    "api": "API functionality features",
    "models": "Data model features",
    "process": "Process improvement features",
    "release_plans": "Release planning features"
}

@dataclass
class Feature:
    """Represents a BDD feature file with its attributes."""
    path: Path
    name: str
    description: str
    scenarios: List[Dict] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    content: str = ""
    domain: str = ""
    functionality: str = ""
    
    @property
    def suggested_directory(self) -> str:
        """Determine the suggested directory based on domain."""
        if not self.domain:
            return "core"  # Default
        
        domain_lower = self.domain.lower()
        
        # Map domain to standard directory
        if "api" in domain_lower:
            return "api"
        elif "cli" in domain_lower:
            return "cli"
        elif "model" in domain_lower:
            return "models"
        elif "process" in domain_lower:
            return "process"
        elif "release" in domain_lower or "plan" in domain_lower:
            return "release_plans"
        else:
            return "core"
    
    @property
    def suggested_filename(self) -> str:
        """Generate a standardized filename based on domain and functionality."""
        if not self.domain or not self.functionality:
            # Extract from path if not set
            filename = self.path.stem
            parts = filename.split('_', 1)
            
            domain = self.domain or (parts[0] if len(parts) > 0 else "core")
            functionality = self.functionality or (parts[1] if len(parts) > 1 else "general")
            
            return f"{domain.lower()}_{functionality.lower()}.feature"
        
        return f"{self.domain.lower()}_{self.functionality.lower()}.feature"
    
    @property
    def suggested_path(self, base_dir: Optional[Path] = None) -> Path:
        """Generate the suggested path for this feature."""
        directory = self.suggested_directory
        filename = self.suggested_filename
        
        if base_dir:
            return base_dir / "features" / directory / filename
        else:
            # Use relative path if no base directory specified
            return Path("features") / directory / filename

@dataclass
class ReorganizationPlan:
    """Plan for reorganizing a feature file."""
    feature: Feature
    source_path: Path
    target_path: Path
    action: str = "move"  # move, rename, or split
    reason: str = ""
    
    def execute(self, dry_run: bool = False) -> bool:
        """Execute the reorganization plan."""
        logger.info(f"Executing plan: {self.action} {self.source_path} to {self.target_path}")
        
        if dry_run:
            logger.info("Dry run mode - not making actual changes")
            return True
        
        # Create target directory if it doesn't exist
        self.target_path.parent.mkdir(parents=True, exist_ok=True)
        
        if self.action == "move":
            return self._execute_move()
        elif self.action == "rename":
            return self._execute_rename()
        elif self.action == "split":
            logger.warning("Split action not implemented yet")
            return False
        else:
            logger.error(f"Unknown action: {self.action}")
            return False
    
    def _execute_move(self) -> bool:
        """Move the feature file to the target location."""
        try:
            shutil.copy2(self.source_path, self.target_path)
            logger.info(f"Moved {self.source_path} to {self.target_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to move {self.source_path}: {e}")
            return False
    
    def _execute_rename(self) -> bool:
        """Rename the feature file in place."""
        try:
            shutil.copy2(self.source_path, self.target_path)
            logger.info(f"Renamed {self.source_path} to {self.target_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to rename {self.source_path}: {e}")
            return False

class FeatureReorganizer:
    """Main class for reorganizing BDD features."""
    
    def __init__(self, 
                 features_dir: str, 
                 output_dir: str,
                 steps_dir: Optional[str] = None,
                 dry_run: bool = False,
                 delete_source: bool = False):
        self.features_dir = Path(features_dir)
        self.output_dir = Path(output_dir)
        self.steps_dir = Path(steps_dir) if steps_dir else None
        self.dry_run = dry_run
        self.delete_source = delete_source
        self.features: List[Feature] = []
        self.plans: List[ReorganizationPlan] = []
    
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
        """Parse a feature file and extract relevant information."""
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
            
            # Extract scenarios
            scenarios = []
            scenario_matches = re.finditer(
                r'(?:(?:@[^\n]+\n)+)?\s*(Scenario(?:\s+Outline)?:\s*(.+?)$.*?)(?=\n\s*(?:@|Scenario|$))',
                content, re.DOTALL | re.MULTILINE
            )
            
            for scenario_match in scenario_matches:
                scenario_content = scenario_match.group(1)
                scenario_name = scenario_match.group(2).strip()
                
                # Extract scenario tags
                scenario_tags = []
                scenario_tags_match = re.search(r'((?:@[^\n]+\n)+)Scenario', scenario_content)
                if scenario_tags_match:
                    scenario_tags = re.findall(r'@\S+', scenario_tags_match.group(1))
                
                scenarios.append({
                    "name": scenario_name,
                    "content": scenario_content.strip(),
                    "tags": scenario_tags
                })
            
            # Determine domain and functionality from filename or tags
            domain, functionality = self._extract_domain_functionality(file_path, feature_tags)
            
            feature = Feature(
                path=file_path,
                name=feature_name,
                description=description,
                scenarios=scenarios,
                tags=feature_tags,
                content=content,
                domain=domain,
                functionality=functionality
            )
            
            logger.info(f"Parsed feature: {feature_name} ({domain}/{functionality})")
            return feature
        
        except Exception as e:
            logger.error(f"Error parsing feature file {file_path}: {e}")
            return None
    
    def _extract_domain_functionality(self, file_path: Path, tags: List[str]) -> Tuple[str, str]:
        """Extract domain and functionality from filename or tags."""
        # Try to extract from filename first
        filename = file_path.stem
        parts = filename.split('_', 1)
        
        domain = parts[0] if len(parts) > 0 else ""
        functionality = parts[1] if len(parts) > 1 else ""
        
        # If domain not found in filename, try to extract from tags
        if not domain:
            for tag in tags:
                # Check if tag matches a known domain
                tag_name = tag[1:] if tag.startswith('@') else tag  # Remove @ if present
                tag_lower = tag_name.lower()
                
                for known_domain in ["api", "cli", "model", "core", "process"]:
                    if known_domain in tag_lower:
                        domain = known_domain
                        break
                
                if domain:
                    break
        
        # If still no domain, try to extract from directory
        if not domain:
            for part in file_path.parts:
                part_lower = part.lower()
                for known_domain in ["api", "cli", "model", "core", "process"]:
                    if known_domain in part_lower:
                        domain = known_domain
                        break
                
                if domain:
                    break
        
        # Default domain if still not found
        if not domain:
            domain = "core"
        
        # Default functionality if not found
        if not functionality:
            functionality = "general"
        
        return domain, functionality
    
    def create_reorganization_plans(self):
        """Create plans for reorganizing feature files."""
        logger.info("Creating reorganization plans")
        
        for feature in self.features:
            source_path = feature.path
            
            # Determine if the feature is already in the correct location
            relative_source = source_path.relative_to(self.features_dir)
            current_directory = relative_source.parent
            
            # Determine target directory and filename
            target_directory = feature.suggested_directory
            target_filename = feature.suggested_filename
            target_path = self.output_dir / "features" / target_directory / target_filename
            
            # Determine action and reason
            if str(current_directory) == target_directory and source_path.name == target_filename:
                logger.info(f"Feature {source_path.name} already in correct location")
                continue
            
            if str(current_directory) != target_directory:
                action = "move"
                reason = f"Feature belongs in {target_directory} directory based on domain"
            else:
                action = "rename"
                reason = f"Feature should be renamed to follow naming convention: {target_filename}"
            
            # Create reorganization plan
            plan = ReorganizationPlan(
                feature=feature,
                source_path=source_path,
                target_path=target_path,
                action=action,
                reason=reason
            )
            
            self.plans.append(plan)
        
        logger.info(f"Created {len(self.plans)} reorganization plans")
    
    def execute_plans(self):
        """Execute all reorganization plans."""
        logger.info(f"Executing {len(self.plans)} reorganization plans")
        
        success_count = 0
        for i, plan in enumerate(self.plans):
            logger.info(f"Executing plan {i+1}/{len(self.plans)}")
            if plan.execute(dry_run=self.dry_run):
                success_count += 1
                
                # Delete source file if requested
                if self.delete_source and not self.dry_run:
                    try:
                        os.remove(plan.source_path)
                        logger.info(f"Deleted source file {plan.source_path}")
                    except Exception as e:
                        logger.error(f"Failed to delete source file {plan.source_path}: {e}")
        
        logger.info(f"Successfully executed {success_count}/{len(self.plans)} plans")
    
    def reorganize_step_definitions(self):
        """Reorganize step definition files to match feature files."""
        if not self.steps_dir:
            logger.info("No steps directory provided, skipping step definition reorganization")
            return
        
        logger.info(f"Reorganizing step definition files in {self.steps_dir}")
        
        # Create mapping of feature files to step files
        feature_to_steps = {}
        
        # Find all step definition files
        step_files = list(self.steps_dir.glob("**/*_steps.py"))
        logger.info(f"Found {len(step_files)} step definition files")
        
        # Match step files to features based on naming convention
        for step_file in step_files:
            step_base = step_file.stem.replace('_steps', '')
            
            # Find matching feature
            for feature in self.features:
                feature_base = feature.path.stem
                if step_base == feature_base:
                    feature_to_steps[str(feature.path)] = step_file
                    break
        
        # Create plans for step files
        step_plans = []
        
        for feature_path, step_file in feature_to_steps.items():
            # Find the feature
            feature = next((f for f in self.features if str(f.path) == feature_path), None)
            if not feature:
                continue
            
            # Determine target directory and filename for step file
            target_directory = feature.suggested_directory
            target_filename = feature.suggested_filename.replace('.feature', '_steps.py')
            target_path = self.output_dir / "steps" / target_directory / target_filename
            
            # Create plan
            plan = ReorganizationPlan(
                feature=feature,
                source_path=step_file,
                target_path=target_path,
                action="move",
                reason=f"Step file should be moved to match feature location: {target_path}"
            )
            
            step_plans.append(plan)
        
        logger.info(f"Created {len(step_plans)} step definition reorganization plans")
        
        # Execute step plans
        success_count = 0
        for i, plan in enumerate(step_plans):
            logger.info(f"Executing step plan {i+1}/{len(step_plans)}")
            if plan.execute(dry_run=self.dry_run):
                success_count += 1
                
                # Delete source file if requested
                if self.delete_source and not self.dry_run:
                    try:
                        os.remove(plan.source_path)
                        logger.info(f"Deleted source step file {plan.source_path}")
                    except Exception as e:
                        logger.error(f"Failed to delete source step file {plan.source_path}: {e}")
        
        logger.info(f"Successfully executed {success_count}/{len(step_plans)} step plans")
    
    def generate_report(self, output_file: str):
        """Generate a report of the reorganization."""
        logger.info(f"Generating report to {output_file}")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# BDD Feature Reorganization Report\n\n")
            
            f.write("## Summary\n\n")
            f.write(f"- Total features analyzed: {len(self.features)}\n")
            f.write(f"- Features requiring reorganization: {len(self.plans)}\n")
            
            # Count by action
            action_counts = {}
            for plan in self.plans:
                action_counts[plan.action] = action_counts.get(plan.action, 0) + 1
            
            f.write("- Plans by action:\n")
            for action, count in action_counts.items():
                f.write(f"  - {action}: {count}\n")
            
            # Details of each plan
            f.write("\n## Reorganization Plans\n\n")
            
            for i, plan in enumerate(self.plans):
                f.write(f"### Plan {i+1}: {plan.action.capitalize()} {plan.feature.name}\n\n")
                f.write(f"- Source path: `{plan.source_path}`\n")
                f.write(f"- Target path: `{plan.target_path}`\n")
                f.write(f"- Reason: {plan.reason}\n")
                f.write(f"- Domain: {plan.feature.domain}\n")
                f.write(f"- Functionality: {plan.feature.functionality}\n")
                f.write("\n")
            
            # Directory structure
            f.write("\n## Resulting Directory Structure\n\n")
            f.write("```\n")
            f.write("features/\n")
            
            # Group features by directory
            features_by_dir = {}
            for feature in self.features:
                target_dir = feature.suggested_directory
                if target_dir not in features_by_dir:
                    features_by_dir[target_dir] = []
                
                features_by_dir[target_dir].append(feature.suggested_filename)
            
            # Write directory structure
            for directory, files in sorted(features_by_dir.items()):
                f.write(f"├── {directory}/\n")
                for i, file in enumerate(sorted(files)):
                    if i == len(files) - 1:
                        f.write(f"│   └── {file}\n")
                    else:
                        f.write(f"│   ├── {file}\n")
            
            f.write("```\n")
        
        logger.info(f"Report generated: {output_file}")

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description='Reorganize BDD feature files according to conventions')
    parser.add_argument('--features-dir', required=True, help='Directory containing BDD feature files')
    parser.add_argument('--output-dir', required=True, help='Directory for reorganized output')
    parser.add_argument('--steps-dir', help='Directory containing step definition files')
    parser.add_argument('--report', help='Path to write reorganization report')
    parser.add_argument('--dry-run', action='store_true', help='Perform a dry run without making changes')
    parser.add_argument('--delete-source', action='store_true', help='Delete source files after reorganization')
    
    args = parser.parse_args()
    
    reorganizer = FeatureReorganizer(
        features_dir=args.features_dir,
        output_dir=args.output_dir,
        steps_dir=args.steps_dir,
        dry_run=args.dry_run,
        delete_source=args.delete_source
    )
    
    reorganizer.scan_features()
    reorganizer.create_reorganization_plans()
    
    if not reorganizer.plans:
        logger.warning("No reorganization plans created")
        return
    
    reorganizer.execute_plans()
    
    if args.steps_dir:
        reorganizer.reorganize_step_definitions()
    
    if args.report:
        reorganizer.generate_report(args.report)
    
    logger.info("BDD feature reorganization complete")

if __name__ == "__main__":
    main() 