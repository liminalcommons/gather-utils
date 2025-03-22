#!/usr/bin/env python3
"""
BDD Feature Template Generator

This tool generates standardized BDD feature templates according to the defined
conventions. It helps ensure consistency in new feature files and makes it easier
for developers to follow the established BDD patterns.
"""

import os
import sys
import json
import logging
import argparse
import datetime
from pathlib import Path
from typing import List, Dict, Optional, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('bdd_feature_template')

# Directory structure as defined in BDD conventions
STANDARD_DOMAINS = [
    "core", "cli", "api", "models", "process", "release_plans"
]

# Template formats
FEATURE_TEMPLATE = """\
{feature_tags}
Feature: {feature_name}
  {feature_description}
  
  As a {actor}
  I want {action}
  So that {benefit}

{background_section}

{scenarios}
"""

BACKGROUND_TEMPLATE = """\
  Background:
    Given {given_condition}
"""

SCENARIO_TEMPLATE = """\
  {scenario_tags}
  Scenario: {scenario_name}
    Given {given_condition}
    When {when_action}
    Then {then_result}
"""

SCENARIO_OUTLINE_TEMPLATE = """\
  {scenario_tags}
  Scenario Outline: {scenario_name}
    Given {given_condition}
    When {when_action}
    Then {then_result}
    
    Examples:
      | {example_header} |
      | {example_value}  |
"""

class FeatureTemplateGenerator:
    """Main class for generating BDD feature templates."""
    
    def __init__(self, 
                 output_dir: str,
                 domain: str,
                 functionality: str,
                 component_map_file: Optional[str] = None):
        self.output_dir = Path(output_dir)
        self.domain = domain.lower()
        self.functionality = functionality.lower()
        self.component_map_file = Path(component_map_file) if component_map_file else None
        self.component_map: Dict[str, str] = {}
        
        # Load component mapping if provided
        if self.component_map_file and self.component_map_file.exists():
            self._load_component_map()
    
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
    
    def generate_template(self, 
                         feature_name: str,
                         feature_description: str,
                         actor: str,
                         action: str,
                         benefit: str,
                         requirements: List[str],
                         release: str = "REL-1",
                         with_background: bool = False,
                         num_scenarios: int = 2,
                         with_outline: bool = False) -> str:
        """Generate a feature template from the provided information."""
        logger.info(f"Generating template for feature: {feature_name}")
        
        # Validate domain
        if self.domain not in STANDARD_DOMAINS and self.domain not in self.component_map:
            suggested_domain = self._suggest_domain()
            logger.warning(f"Domain '{self.domain}' is not standard. Suggested: {suggested_domain}")
            self.domain = suggested_domain
        
        # Generate feature tags
        feature_tags = self._generate_feature_tags()
        
        # Generate background if requested
        background_section = ""
        if with_background:
            background_section = BACKGROUND_TEMPLATE.format(
                given_condition=f"the system is ready for {self.functionality} operations"
            )
        
        # Generate scenarios
        scenarios = []
        for i in range(1, num_scenarios + 1):
            # Create scenario tags
            scenario_tags = self._generate_scenario_tags(requirements, release, i)
            
            if i <= 1 or not with_outline:
                # Regular scenario
                scenario = SCENARIO_TEMPLATE.format(
                    scenario_tags="\n  ".join(scenario_tags),
                    scenario_name=f"{feature_name} - basic case {i}",
                    given_condition=f"the {self.functionality} system is configured",
                    when_action=f"the user performs {self.functionality} operation",
                    then_result=f"the system responds with the expected {self.functionality} result"
                )
            else:
                # Scenario outline for variety
                scenario = SCENARIO_OUTLINE_TEMPLATE.format(
                    scenario_tags="\n  ".join(scenario_tags),
                    scenario_name=f"{feature_name} - with multiple cases",
                    given_condition=f"the {self.functionality} system is configured with <parameter>",
                    when_action=f"the user performs {self.functionality} operation",
                    then_result=f"the system responds with <expected>",
                    example_header="parameter | expected",
                    example_value="value1    | result1"
                )
            
            scenarios.append(scenario)
        
        # Format the full feature
        feature_content = FEATURE_TEMPLATE.format(
            feature_tags="\n".join(feature_tags),
            feature_name=feature_name,
            feature_description=feature_description,
            actor=actor,
            action=action,
            benefit=benefit,
            background_section=background_section,
            scenarios="\n\n".join(scenarios)
        )
        
        return feature_content
    
    def _generate_feature_tags(self) -> List[str]:
        """Generate standard tags for the feature."""
        # Feature-level tags are typically minimal, as most tags go on scenarios
        return [f"@{self.domain.upper()}"]
    
    def _generate_scenario_tags(self, 
                               requirements: List[str], 
                               release: str,
                               scenario_num: int) -> List[str]:
        """Generate standard tags for a scenario."""
        tags = []
        
        # Add domain tag
        domain_tag = f"@{self.domain.upper()}"
        tags.append(domain_tag)
        
        # Add functionality tag
        func_tag = f"@{self.functionality.upper()}"
        tags.append(func_tag)
        
        # Add requirements
        for req in requirements:
            # Ensure REQ tag format is correct
            if not req.startswith("@REQ-"):
                req = f"@REQ-{self.domain.upper()}-{req}"
            tags.append(req)
        
        # Add release tag
        if not release.startswith("@REL-"):
            release = f"@REL-{release}"
        tags.append(release)
        
        # For variety in the examples, add a process tag to some scenarios
        if scenario_num % 2 == 0:
            tags.append("@PROC-VALIDATION")
        
        return tags
    
    def _suggest_domain(self) -> str:
        """Suggest an appropriate domain based on the provided domain name."""
        domain_lower = self.domain.lower()
        
        # Try to match to a standard domain
        if "api" in domain_lower:
            return "api"
        elif "cli" in domain_lower or "command" in domain_lower:
            return "cli"
        elif "model" in domain_lower or "data" in domain_lower:
            return "models"
        elif "process" in domain_lower or "workflow" in domain_lower:
            return "process"
        elif "plan" in domain_lower or "release" in domain_lower:
            return "release_plans"
        else:
            return "core"  # Default
    
    def save_template(self, template_content: str) -> Path:
        """Save the generated template to a file."""
        # Ensure directory exists
        domain_dir = self.output_dir / self.domain
        domain_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate filename
        filename = f"{self.domain}_{self.functionality}.feature"
        file_path = domain_dir / filename
        
        # Write the template to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(template_content)
        
        logger.info(f"Template saved to {file_path}")
        return file_path
    
    def generate_step_definition_template(self, feature_file_path: Path) -> str:
        """Generate a template for step definitions based on the feature."""
        logger.info(f"Generating step definition template for {feature_file_path}")
        
        try:
            # Read the feature file
            with open(feature_file_path, 'r', encoding='utf-8') as f:
                feature_content = f.read()
            
            # Extract steps
            given_steps = []
            when_steps = []
            then_steps = []
            
            # Simple extraction of steps (a more robust parser would be better in production)
            for line in feature_content.split('\n'):
                line = line.strip()
                if line.startswith('Given '):
                    given_steps.append(line[6:])
                elif line.startswith('When '):
                    when_steps.append(line[5:])
                elif line.startswith('Then '):
                    then_steps.append(line[5:])
            
            # Remove duplicates
            given_steps = list(set(given_steps))
            when_steps = list(set(when_steps))
            then_steps = list(set(then_steps))
            
            # Generate the step definition template
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            
            step_template = f"""#!/usr/bin/env python3
'''
Step definitions for {self.domain}_{self.functionality} feature
Created: {today}
'''

from behave import given, when, then
from hamcrest import assert_that, equal_to

# Given steps
"""
            
            for step in given_steps:
                # Convert to regex pattern for step definition
                pattern = step.replace('<', '{').replace('>', '}')
                
                # Extract parameters
                params = []
                param_start = pattern.find('{')
                while param_start != -1:
                    param_end = pattern.find('}', param_start)
                    if param_end != -1:
                        param = pattern[param_start+1:param_end]
                        params.append(param)
                        param_start = pattern.find('{', param_end)
                    else:
                        break
                
                # Convert to step definition format
                python_params = ', '.join(['context'] + params)
                definition = f'@given("{pattern}")\ndef given_{self.functionality}_{"_".join(params)}({python_params}):\n    """Implementation for: {step}"""\n    # TODO: Implement step\n    pass\n\n'
                step_template += definition
            
            step_template += "# When steps\n"
            
            for step in when_steps:
                # Convert to regex pattern
                pattern = step.replace('<', '{').replace('>', '}')
                
                # Extract parameters
                params = []
                param_start = pattern.find('{')
                while param_start != -1:
                    param_end = pattern.find('}', param_start)
                    if param_end != -1:
                        param = pattern[param_start+1:param_end]
                        params.append(param)
                        param_start = pattern.find('{', param_end)
                    else:
                        break
                
                # Convert to step definition format
                python_params = ', '.join(['context'] + params)
                definition = f'@when("{pattern}")\ndef when_{self.functionality}_{"_".join(params) if params else "action"}({python_params}):\n    """Implementation for: {step}"""\n    # TODO: Implement step\n    pass\n\n'
                step_template += definition
            
            step_template += "# Then steps\n"
            
            for step in then_steps:
                # Convert to regex pattern
                pattern = step.replace('<', '{').replace('>', '}')
                
                # Extract parameters
                params = []
                param_start = pattern.find('{')
                while param_start != -1:
                    param_end = pattern.find('}', param_start)
                    if param_end != -1:
                        param = pattern[param_start+1:param_end]
                        params.append(param)
                        param_start = pattern.find('{', param_end)
                    else:
                        break
                
                # Convert to step definition format
                python_params = ', '.join(['context'] + params)
                definition = f'@then("{pattern}")\ndef then_{self.functionality}_{"_".join(params) if params else "result"}({python_params}):\n    """Implementation for: {step}"""\n    # TODO: Implement step\n    assert_that(True, equal_to(True))  # Placeholder assertion\n    pass\n\n'
                step_template += definition
            
            return step_template
            
        except Exception as e:
            logger.error(f"Failed to generate step definition template: {e}")
            return ""
    
    def save_step_definition_template(self, step_template: str, feature_file_path: Path) -> Path:
        """Save the generated step definition template to a file."""
        if not step_template:
            return Path("")
        
        # Create steps directory if it doesn't exist
        steps_dir = self.output_dir.parent / "steps" / self.domain
        steps_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate filename (replace .feature with _steps.py)
        feature_name = feature_file_path.stem
        step_filename = f"{feature_name}_steps.py"
        step_file_path = steps_dir / step_filename
        
        # Write the template to the file
        with open(step_file_path, 'w', encoding='utf-8') as f:
            f.write(step_template)
        
        logger.info(f"Step definition template saved to {step_file_path}")
        return step_file_path

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description='Generate standardized BDD feature templates')
    
    parser.add_argument('--output-dir', required=True, help='Directory to save the generated templates')
    parser.add_argument('--domain', required=True, help='Domain of the feature (e.g., api, cli, core)')
    parser.add_argument('--functionality', required=True, help='Functionality being tested (e.g., authentication)')
    parser.add_argument('--feature-name', required=True, help='Name of the feature')
    parser.add_argument('--description', required=True, help='Description of the feature')
    parser.add_argument('--actor', default='user', help='Actor in the user story')
    parser.add_argument('--action', required=True, help='Action in the user story')
    parser.add_argument('--benefit', required=True, help='Benefit in the user story')
    parser.add_argument('--requirements', nargs='+', required=True, help='List of requirement IDs to include')
    parser.add_argument('--release', default='REL-1', help='Release tag to apply')
    parser.add_argument('--background', action='store_true', help='Include a background section')
    parser.add_argument('--num-scenarios', type=int, default=2, help='Number of scenarios to generate')
    parser.add_argument('--with-outline', action='store_true', help='Include a scenario outline')
    parser.add_argument('--component-map', help='JSON file with component mappings')
    parser.add_argument('--generate-steps', action='store_true', help='Generate step definition template')
    
    args = parser.parse_args()
    
    generator = FeatureTemplateGenerator(
        output_dir=args.output_dir,
        domain=args.domain,
        functionality=args.functionality,
        component_map_file=args.component_map
    )
    
    template = generator.generate_template(
        feature_name=args.feature_name,
        feature_description=args.description,
        actor=args.actor,
        action=args.action,
        benefit=args.benefit,
        requirements=args.requirements,
        release=args.release,
        with_background=args.background,
        num_scenarios=args.num_scenarios,
        with_outline=args.with_outline
    )
    
    feature_file_path = generator.save_template(template)
    
    if args.generate_steps:
        step_template = generator.generate_step_definition_template(feature_file_path)
        generator.save_step_definition_template(step_template, feature_file_path)
    
    logger.info("BDD feature template generation complete")

if __name__ == "__main__":
    main() 