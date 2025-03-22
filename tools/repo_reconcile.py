#!/usr/bin/env python
"""
Repository reconciliation script.

This script reorganizes the repository according to the reconciliation plan:
1. Documentation organization
2. Testing structure consolidation
3. Code organization and cleanup
4. Automation and maintenance setup
"""
import os
import sys
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

def create_directory(path):
    """Create directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def move_file(src, dest):
    """Move a file from src to dest."""
    if os.path.exists(src):
        # Create destination directory if it doesn't exist
        dest_dir = os.path.dirname(dest)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        # Move the file
        shutil.move(src, dest)
        print(f"Moved: {src} -> {dest}")
    else:
        print(f"Warning: Source file does not exist: {src}")

def organize_documentation():
    """Organize documentation files."""
    print("\n=== Organizing Documentation ===")
    
    # Create archive directory
    create_directory("docs/archive")
    
    # Add timestamp to archived files
    timestamp = datetime.now().strftime("%Y%m%d")
    
    # List of files to archive
    files_to_archive = [
        ("FINAL_SUMMARY.md", f"docs/archive/{timestamp}_FINAL_SUMMARY.md"),
        ("REORGANIZATION_SUMMARY.md", f"docs/archive/{timestamp}_REORGANIZATION_SUMMARY.md"),
        ("REORGANIZATION_PLAN.md", f"docs/archive/{timestamp}_REORGANIZATION_PLAN.md"),
        ("TASK_COMPLETION_SUMMARY.md", f"docs/archive/{timestamp}_TASK_COMPLETION_SUMMARY.md")
    ]
    
    # Move files to archive
    for src, dest in files_to_archive:
        move_file(src, dest)
    
    # Create ARCHIVE.md to explain the archive
    with open("docs/archive/ARCHIVE.md", "w") as f:
        f.write(f"""# Documentation Archive

This directory contains archived documentation that is no longer actively maintained.
These documents represent completed phases of the project or superseded plans.

## Archive Contents

""")
        
        # List archived files
        for src, dest in files_to_archive:
            if os.path.exists(dest):
                basename = os.path.basename(dest)
                f.write(f"- {basename} (archived on {timestamp})\n")
    
    print("Created docs/archive/ARCHIVE.md")

def consolidate_testing_structure():
    """Consolidate testing structure."""
    print("\n=== Consolidating Testing Structure ===")
    
    # Create BDD tests directory
    create_directory("tests/bdd/features")
    create_directory("tests/bdd/steps")
    
    # Move BDD tests to the new location
    feature_files = Path("features").glob("*.feature")
    for feature_file in feature_files:
        dest = f"tests/bdd/features/{feature_file.name}"
        move_file(str(feature_file), dest)
    
    # Move step definitions
    step_files = Path("features/steps").glob("*.py")
    for step_file in step_files:
        dest = f"tests/bdd/steps/{step_file.name}"
        move_file(str(step_file), dest)
    
    # Move environment.py
    move_file("features/environment.py", "tests/bdd/environment.py")
    
    # Move TDD tests
    tdd_feature_files = Path("tdd_tests/features").glob("*.feature")
    for feature_file in tdd_feature_files:
        dest = f"tests/bdd/features/{feature_file.name}"
        move_file(str(feature_file), dest)
    
    tdd_step_files = Path("tdd_tests/features/steps").glob("*.py")
    for step_file in tdd_step_files:
        dest = f"tests/unit/{step_file.name}"
        move_file(str(step_file), dest)
    
    # Update pytest.ini
    with open("pytest.ini", "a") as f:
        f.write("\n# Updated by repo_reconcile.py\n")
        f.write("testpaths = tests\n")
        f.write("bdd_features_dir = tests/bdd/features\n")
        f.write("bdd_steps_dir = tests/bdd/steps\n")
    
    print("Updated pytest.ini")

def organize_code():
    """Organize code and cleanup."""
    print("\n=== Organizing Code ===")
    
    # Create analysis directory
    create_directory("data/analysis")
    
    # Move analysis data
    if os.path.exists("my_analysis"):
        for item in os.listdir("my_analysis"):
            src = os.path.join("my_analysis", item)
            dest = os.path.join("data/analysis", item)
            move_file(src, dest)
    
    # Clean up temporary files
    print("Cleaning up temporary files...")
    for root, dirs, files in os.walk("."):
        # Skip .git directory
        if ".git" in dirs:
            dirs.remove(".git")
        
        # Skip .venv directory
        if ".venv" in dirs:
            dirs.remove(".venv")
        
        # Remove __pycache__ directories
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            shutil.rmtree(pycache_path)
            print(f"Removed: {pycache_path}")
        
        # Remove .pyc files
        for file in files:
            if file.endswith(".pyc"):
                pyc_path = os.path.join(root, file)
                os.remove(pyc_path)
                print(f"Removed: {pyc_path}")

def setup_automation():
    """Setup automation and maintenance tools."""
    print("\n=== Setting Up Automation ===")
    
    # Create health check script
    health_check_script = """#!/usr/bin/env python
\"\"\"
Repository health check script.
Checks for:
- Outdated documentation
- Test coverage
- Code quality
- Redundant files
\"\"\"
import os
import sys
import subprocess
from datetime import datetime, timedelta

def check_documentation_freshness():
    \"\"\"Check if documentation is up to date.\"\"\"
    print("Checking documentation freshness...")
    # Implementation details...

def check_test_coverage():
    \"\"\"Check test coverage meets thresholds.\"\"\"
    print("Checking test coverage...")
    # Run pytest with coverage
    result = subprocess.run(
        ["python", "-m", "pytest", "--cov=gather_manager", "tests/unit"],
        capture_output=True,
        text=True
    )
    
    # Parse coverage output
    # Implementation details...

def check_code_quality():
    \"\"\"Run linters and code quality checks.\"\"\"
    print("Checking code quality...")
    # Run flake8
    result = subprocess.run(
        ["flake8", "src", "tests"],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print("Code quality issues found:")
        print(result.stdout)
        return False
    
    return True

def check_for_redundancy():
    \"\"\"Check for redundant or duplicate files.\"\"\"
    print("Checking for redundancy...")
    # Implementation details...

if __name__ == "__main__":
    check_documentation_freshness()
    check_test_coverage()
    check_code_quality()
    check_for_redundancy()
"""
    
    with open("tools/repo_health_check.py", "w") as f:
        f.write(health_check_script)
    
    # Make it executable
    os.chmod("tools/repo_health_check.py", 0o755)
    print("Created tools/repo_health_check.py")
    
    # Create maintenance guidelines
    maintenance_guidelines = """# Repository Maintenance Guidelines

This document outlines guidelines for maintaining the repository in a clean and organized state.

## Documentation Guidelines

1. **Living Documentation**
   - README.md - Project overview, getting started, and current status
   - docs/project/PROJECT_STATUS.md - Detailed project status
   - docs/project/DEFINITION_OF_DONE.md - Definition of Done criteria

2. **Archived Documentation**
   - docs/archive/ - Completed project documents
   - Each archived document should have a header indicating when it was archived

3. **Documentation Review Schedule**
   - Review README.md monthly
   - Review PROJECT_STATUS.md bi-weekly
   - Review other documentation quarterly

## Code Guidelines

1. **Code Organization**
   - src/ - Source code
   - tests/ - All tests (unit, integration, BDD)
   - tools/ - Utility scripts and tools
   - examples/ - Example code and usage

2. **Code Quality**
   - All code must pass linters
   - All code must have tests
   - Test coverage must meet thresholds (80% minimum)

3. **Code Review**
   - All changes must be reviewed
   - Automated checks must pass before merge

## Testing Guidelines

1. **Test Organization**
   - tests/unit/ - Unit tests (TDD)
   - tests/integration/ - Integration tests
   - tests/bdd/ - BDD tests

2. **Test Quality**
   - Tests must be independent
   - Tests must be deterministic
   - Tests must be fast

3. **Test Coverage**
   - Unit test coverage: 80% minimum
   - Feature coverage: 100% of user stories

## Maintenance Schedule

1. **Weekly**
   - Run repo_health_check.py
   - Address any issues found

2. **Monthly**
   - Review and update README.md
   - Archive completed documentation
   - Clean up temporary files

3. **Quarterly**
   - Comprehensive repository review
   - Update maintenance guidelines as needed
"""
    
    with open("docs/project/MAINTENANCE_GUIDELINES.md", "w") as f:
        f.write(maintenance_guidelines)
    
    print("Created docs/project/MAINTENANCE_GUIDELINES.md")

def update_readme():
    """Update README.md with current project structure."""
    print("\n=== Updating README.md ===")
    
    # Read current README
    with open("README.md", "r") as f:
        readme_content = f.read()
    
    # Add repository structure section
    repo_structure = """
## Repository Structure

- `src/` - Source code
  - `gather_manager/` - Main package
    - `api/` - API client
    - `cli/` - Command-line interface
    - `models/` - Data models
    - `services/` - Business logic
    - `utils/` - Utility functions
- `tests/` - Tests
  - `unit/` - Unit tests (TDD)
  - `integration/` - Integration tests
  - `bdd/` - BDD tests
- `docs/` - Documentation
  - `project/` - Project documentation
  - `api/` - API documentation
  - `user_guide/` - User guide
  - `archive/` - Archived documentation
- `tools/` - Utility scripts and tools
- `examples/` - Example code and usage
- `data/` - Data files and analysis results
"""
    
    # Check if structure section already exists
    if "## Repository Structure" not in readme_content:
        # Add it after the first section
        sections = readme_content.split("\n## ")
        new_content = sections[0] + repo_structure + "\n## " + "\n## ".join(sections[1:])
        
        # Write updated README
        with open("README.md", "w") as f:
            f.write(new_content)
        
        print("Updated README.md with repository structure")
    else:
        print("README.md already has repository structure section")

def manage_release_plan(milestone=None, create_bdd_scenarios=False, verify_acceptance_criteria=False):
    """
    Manage the release plan and acceptance criteria.
    
    Args:
        milestone: The milestone to manage (Documentation, Structure, Automation, Agent)
        create_bdd_scenarios: Whether to create BDD scenarios for the milestone
        verify_acceptance_criteria: Whether to verify acceptance criteria compliance for the milestone
    """
    print(f"\n=== Managing Release Plan for Milestone: {milestone or 'All'} ===")
    
    # Define release milestones and their requirements
    milestones = {
        "Documentation": [
            "REQ-DOC-1: Repository structure documentation",
            "REQ-DOC-2: Redundancy identification",
            "REQ-DOC-3: Development system map",
        ],
        "Structure": [
            "REQ-STR-1: Testing structure consolidation",
            "REQ-STR-2: Documentation centralization",
            "REQ-STR-3: Tool documentation",
        ],
        "Automation": [
            "REQ-AUTO-1: Enhanced pre-commit hooks",
            "REQ-AUTO-2: Improved repository health checks",
            "REQ-AUTO-3: Unified CLI for development tasks",
        ],
        "Agent": [
            "REQ-AGENT-1: File structure conventions",
            "REQ-AGENT-2: Agent-specific documentation",
            "REQ-AGENT-3: Repository structure validation",
        ]
    }
    
    # Filter by milestone if specified
    if milestone and milestone in milestones:
        selected_milestones = {milestone: milestones[milestone]}
    else:
        selected_milestones = milestones
    
    # Create BDD scenarios
    if create_bdd_scenarios:
        create_bdd_scenarios_for_milestone(selected_milestones)
    
    # Verify acceptance criteria compliance
    if verify_acceptance_criteria:
        verify_milestone_acceptance_criteria(selected_milestones)
    
    return selected_milestones

def create_bdd_scenarios_for_milestone(milestones):
    """Create BDD scenarios for milestone requirements."""
    print("\n=== Creating BDD Scenarios ===")
    
    # Create directory if it doesn't exist
    bdd_dir = "features"
    create_directory(bdd_dir)
    
    for milestone, requirements in milestones.items():
        feature_content = f"""Feature: {milestone} Requirements
  As a project stakeholder
  I want to implement {milestone.lower()} improvements
  So that the development system is more maintainable and evolvable

"""
        
        for req in requirements:
            req_id, req_desc = req.split(": ", 1)
            scenario = f"""  @{req_id} @{milestone}
  Scenario: Implement {req_desc}
    Given we need to implement {req_desc.lower()}
    When we complete the implementation
    Then the {req_desc.lower()} should meet acceptance criteria
    And it should comply with the general Definition of Done

"""
            feature_content += scenario
        
        # Write feature file
        feature_file = os.path.join(bdd_dir, f"{milestone.lower()}_requirements.feature")
        with open(feature_file, "w") as f:
            f.write(feature_content)
        
        print(f"Created BDD feature file: {feature_file}")

def verify_milestone_acceptance_criteria(milestones):
    """Verify compliance with milestone acceptance criteria."""
    print("\n=== Verifying Acceptance Criteria Compliance ===")
    
    # Run BDD tests with milestone tags
    for milestone, requirements in milestones.items():
        req_ids = [req.split(": ")[0] for req in requirements]
        tags = ",".join(req_ids)
        
        print(f"\nVerifying acceptance criteria for {milestone}:")
        try:
            result = subprocess.run(
                ["python", "tools/run_bdd_tests.py", f"--tags={tags}"],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"✅ {milestone} acceptance criteria met")
            else:
                print(f"❌ {milestone} acceptance criteria not met:")
                print(result.stdout)
        except Exception as e:
            print(f"Error verifying acceptance criteria: {e}")

def main():
    """Main function to run the reconciliation process."""
    print("Starting repository reconciliation...")
    
    # Check if we're in the repository root
    if not os.path.exists("pyproject.toml"):
        print("Error: This script must be run from the repository root.")
        sys.exit(1)
    
    # Run reconciliation steps
    organize_documentation()
    consolidate_testing_structure()
    organize_code()
    setup_automation()
    update_readme()
    
    print("\nRepository reconciliation complete!")
    print("\nNext steps:")
    print("1. Review the changes and make any necessary adjustments")
    print("2. Run tests to ensure everything still works")
    print("3. Commit the changes")
    print("4. Update documentation as needed")

if __name__ == "__main__":
    # Add argument parsing for release management
    import argparse
    
    parser = argparse.ArgumentParser(description="Repository reconciliation tool")
    parser.add_argument("--milestone", help="Milestone to manage (Documentation, Structure, Automation, Agent)")
    parser.add_argument("--create-bdd-scenarios", action="store_true", help="Create BDD scenarios for milestone requirements")
    parser.add_argument("--verify-acceptance-criteria", action="store_true", help="Verify acceptance criteria compliance")
    parser.add_argument("--execute", action="store_true", help="Execute reconciliation plan")
    parser.add_argument("--analyze-only", action="store_true", help="Analyze without making changes")
    parser.add_argument("--create-cli", action="store_true", help="Create unified CLI tool")
    
    args = parser.parse_args()
    
    if args.create_bdd_scenarios or args.verify_acceptance_criteria:
        manage_release_plan(args.milestone, args.create_bdd_scenarios, args.verify_acceptance_criteria)
    elif args.execute:
        # Existing reconciliation logic
        main()
    elif args.analyze_only:
        # Existing analysis logic
        # Add analysis logic implementation
        pass
    elif args.create_cli:
        # CLI creation logic
        # Add CLI creation logic implementation
        pass
    else:
        # Default behavior
        main() 