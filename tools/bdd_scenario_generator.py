"""
Tool: Bdd Scenario Generator
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Supports BDD testing and development workflows
Dependencies: bdd_coverage_report
Lifecycle:
    - Created: To support BDD testing and development workflows
    - Active: Currently used in development workflows
    - Obsolescence Conditions:
        1. When BDD testing approach changes significantly
        2. When replaced by more comprehensive tooling
Last Validated: 2025-03-21

"""

#!/usr/bin/env python3
"""
BDD Scenario Generator

This script analyzes the project plan and generates skeleton BDD scenarios
for requirements that don't have corresponding scenarios yet.

Usage:
    python tools/bdd_scenario_generator.py [--milestone MILESTONE]

Options:
    --milestone MILESTONE    Generate scenarios only for the specified milestone
"""
import argparse
import json
import os
import re
from collections import defaultdict
from pathlib import Path

# Import the functions from the coverage report script
from bdd_coverage_report import (
    extract_requirements_from_plan,
    extract_scenarios_from_features,
    map_scenarios_to_requirements,
)


def generate_scenario_template(requirement):
    """Generate a scenario template for a requirement."""
    req_id = requirement["id"]
    task_name = requirement["name"]

    # Convert the task name to a scenario name
    scenario_name = task_name

    # Generate steps based on the task name
    steps = []

    # Add Given step
    if "implement" in task_name.lower() or "create" in task_name.lower():
        steps.append(f"Given I need to {task_name.lower()}")
    elif "enhance" in task_name.lower() or "update" in task_name.lower():
        steps.append(f"Given I have the existing implementation")
    else:
        steps.append("Given I have the necessary components")

    # Add When step
    if "implement" in task_name.lower():
        steps.append(f"When I implement the functionality")
    elif "create" in task_name.lower():
        steps.append(f"When I create the component")
    elif "enhance" in task_name.lower() or "update" in task_name.lower():
        steps.append(f"When I enhance the implementation")
    elif "test" in task_name.lower():
        steps.append(f"When I run the tests")
    else:
        steps.append(f"When I perform the task")

    # Add Then steps
    steps.append(f"Then the {task_name.lower()} should be complete")
    steps.append(f"And it should meet all requirements")

    # Create the scenario template
    scenario_template = [
        f"  @{req_id}",
        f"  Scenario: {scenario_name}",
    ]

    # Add steps
    for step in steps:
        scenario_template.append(f"    {step}")

    return scenario_template


def generate_feature_file(milestone, requirements):
    """Generate a feature file for a milestone with missing scenarios."""
    # Filter requirements for this milestone
    milestone_reqs = [
        req for req in requirements if req["milestone"] == milestone
    ]

    # Filter requirements without scenarios
    missing_reqs = [req for req in milestone_reqs if not req["covered"]]

    if not missing_reqs:
        print(f"No missing scenarios for milestone: {milestone}")
        return None

    # Create the feature file content
    feature_content = [
        f"Feature: {milestone}",
        f"  As a developer",
        f"  I want to implement the {milestone.lower()} functionality",
        f"  So that the Portal Explorer meets all requirements",
        "",
        "  Background:",
        "    Given I have the Portal Explorer codebase",
        "    And I have the necessary dependencies installed",
        "",
    ]

    # Add scenarios for each missing requirement
    for req in missing_reqs:
        scenario_template = generate_scenario_template(req)
        feature_content.extend(scenario_template)
        feature_content.append("")

    return "\n".join(feature_content)


def save_feature_file(milestone, content, output_dir):
    """Save the generated feature file."""
    if not content:
        return None

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create a filename from the milestone
    filename = f"generated_{milestone.lower().replace(' ', '_')}.feature"
    file_path = os.path.join(output_dir, filename)

    # Write the content to the file
    with open(file_path, "w") as f:
        f.write(content)

    return file_path


def suggest_step_definitions(steps, existing_steps):
    """Suggest step definitions based on existing ones."""
    suggestions = {}

    for step in steps:
        # Extract the step type (Given, When, Then, And)
        step_type = step.strip().split(" ")[0]
        step_text = " ".join(step.strip().split(" ")[1:])

        # Look for similar steps in existing steps
        best_match = None
        best_score = 0

        for existing_step, func_name in existing_steps.items():
            if existing_step.startswith(step_type):
                # Simple similarity score based on word overlap
                existing_text = " ".join(existing_step.strip().split(" ")[1:])
                words1 = set(step_text.lower().split())
                words2 = set(existing_text.lower().split())
                overlap = len(words1.intersection(words2))
                score = (
                    overlap / max(len(words1), len(words2))
                    if max(len(words1), len(words2)) > 0
                    else 0
                )

                if (
                    score > best_score and score > 0.3
                ):  # Threshold for similarity
                    best_score = score
                    best_match = (existing_step, func_name)

        if best_match:
            suggestions[step] = best_match

    return suggestions


def extract_existing_step_definitions(steps_dir):
    """Extract existing step definitions from Python files."""
    existing_steps = {}

    for py_file in Path(steps_dir).glob("*.py"):
        with open(py_file, "r") as f:
            content = f.read()

            # Find all step definitions
            step_patterns = re.findall(
                r'@(?:given|when|then)\([\'"](.+?)[\'"]\)\s*\ndef\s+(\w+)',
                content,
                re.IGNORECASE,
            )

            for pattern, func_name in step_patterns:
                # Convert the pattern to a step string
                step_type = pattern.split("'")[0].strip()
                step_text = pattern

                # Add to existing steps
                existing_steps[step_text] = func_name

    return existing_steps


def generate_step_definition_file(milestone, steps, suggestions, output_dir):
    """Generate a step definition file with suggested implementations."""
    if not steps:
        return None

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create a filename from the milestone
    filename = f"generated_{milestone.lower().replace(' ', '_')}_steps.py"
    file_path = os.path.join(output_dir, filename)

    # Create the file content
    content = [
        '"""',
        f"Step definitions for the {milestone} feature.",
        '"""',
        "from behave import given, when, then",
        "from unittest.mock import MagicMock, patch",
        "",
        "",
    ]

    # Add step definitions
    for step in steps:
        # Extract the step type (Given, When, Then, And)
        step_parts = step.strip().split(" ")
        step_type = step_parts[0].lower()
        step_text = " ".join(step_parts[1:])

        # Skip 'And' steps as they will be handled by the previous step type
        if step_type == "and":
            continue

        # Create a function name from the step text
        func_name = (
            f"step_{step_text.lower().replace(' ', '_').replace('-', '_')}"
        )
        func_name = re.sub(r"[^a-z0-9_]", "", func_name)

        # Add the step definition
        content.append(f"@{step_type}('{step_text}')")
        content.append(f"def {func_name}(context):")

        # Add function body
        if step in suggestions:
            # Use the suggested implementation
            suggested_step, suggested_func = suggestions[step]
            content.append(
                f'    """Implementation based on similar step: {suggested_step}"""'
            )
            content.append(
                f"    # TODO: Adapt the implementation from {suggested_func}"
            )
            content.append(f"    pass")
        else:
            content.append(
                f'    """Implement the step definition for: {step}"""'
            )
            content.append(f"    # TODO: Implement this step")
            content.append(f"    pass")

        content.append("")

    # Write the content to the file
    with open(file_path, "w") as f:
        f.write("\n".join(content))

    return file_path


def extract_steps_from_feature(feature_content):
    """Extract steps from a feature file content."""
    steps = []

    for line in feature_content.split("\n"):
        line = line.strip()
        if (
            line.startswith("Given ")
            or line.startswith("When ")
            or line.startswith("Then ")
            or line.startswith("And ")
        ):
            steps.append(line)

    return steps


def main():
    """Main function to generate BDD scenarios."""
    parser = argparse.ArgumentParser(
        description="Generate BDD scenarios for missing requirements"
    )
    parser.add_argument(
        "--milestone",
        help="Generate scenarios only for the specified milestone",
    )
    args = parser.parse_args()

    # Define paths
    project_root = Path(__file__).parent.parent
    plan_file = project_root / "docs" / "project" / "plan-release0.md"
    feature_dir = project_root / "features"
    steps_dir = project_root / "features" / "steps"
    output_dir = project_root / "features" / "generated"

    # Extract requirements and scenarios
    requirements = extract_requirements_from_plan(plan_file)
    scenarios = extract_scenarios_from_features(feature_dir)

    # Map scenarios to requirements
    requirements = map_scenarios_to_requirements(requirements, scenarios)

    # Extract existing step definitions
    existing_steps = extract_existing_step_definitions(steps_dir)

    # Group requirements by milestone
    reqs_by_milestone = defaultdict(list)
    for req in requirements:
        reqs_by_milestone[req["milestone"]].append(req)

    # Generate feature files for each milestone
    generated_files = []

    if args.milestone:
        # Generate for the specified milestone only
        if args.milestone in reqs_by_milestone:
            feature_content = generate_feature_file(
                args.milestone, requirements
            )
            if feature_content:
                file_path = save_feature_file(
                    args.milestone, feature_content, output_dir
                )
                if file_path:
                    generated_files.append((args.milestone, file_path))

                    # Extract steps and generate step definitions
                    steps = extract_steps_from_feature(feature_content)
                    suggestions = suggest_step_definitions(
                        steps, existing_steps
                    )
                    step_file = generate_step_definition_file(
                        args.milestone, steps, suggestions, steps_dir
                    )
                    if step_file:
                        generated_files.append(
                            (f"{args.milestone} Steps", step_file)
                        )
        else:
            print(f"Milestone not found: {args.milestone}")
    else:
        # Generate for all milestones
        for milestone in reqs_by_milestone:
            feature_content = generate_feature_file(milestone, requirements)
            if feature_content:
                file_path = save_feature_file(
                    milestone, feature_content, output_dir
                )
                if file_path:
                    generated_files.append((milestone, file_path))

                    # Extract steps and generate step definitions
                    steps = extract_steps_from_feature(feature_content)
                    suggestions = suggest_step_definitions(
                        steps, existing_steps
                    )
                    step_file = generate_step_definition_file(
                        milestone, steps, suggestions, steps_dir
                    )
                    if step_file:
                        generated_files.append(
                            (f"{milestone} Steps", step_file)
                        )

    # Print summary
    if generated_files:
        print("\nGenerated files:")
        for name, path in generated_files:
            print(f"- {name}: {path}")
    else:
        print(
            "\nNo files generated. All requirements are covered by existing scenarios."
        )


if __name__ == "__main__":
    main()
