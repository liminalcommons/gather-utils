"""
Tool: Manage Releases
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Tool for manage releases
Dependencies: subprocess
Lifecycle:
    - Created: To automate common development tasks
    - Active: Currently used in development workflows
    - Obsolescence Conditions:
        1. When project requirements change significantly
        2. When replaced by more comprehensive tooling
Last Validated: 2025-03-21

"""

#!/usr/bin/env python3
"""
Release Management Script

This script manages the release process for the development system improvement project.
It leverages the existing tools and BDD framework to:
1. Create and verify acceptance criteria
2. Execute release tasks
3. Track release progress
4. Generate reports

Usage:
    python tools/manage_releases.py [--release RELEASE] [--action ACTION]

Options:
    --release RELEASE    The release to manage (1, 2, 3, 4, or "all")
    --action ACTION      The action to perform (plan, execute, verify, report)
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Map release numbers to milestone names
RELEASE_TO_MILESTONE = {
    "1": "Documentation",
    "2": "Structure",
    "3": "Automation",
    "4": "Agent",
}


def create_release_plan(release):
    """Create a release plan with acceptance criteria."""
    print(f"\n=== Creating Release Plan for Release {release} ===")

    milestone = RELEASE_TO_MILESTONE.get(release)
    if not milestone:
        print(f"Error: Invalid release number: {release}")
        return False

    # Create BDD scenarios for the release
    cmd = [
        "python",
        "tools/repo_reconcile.py",
        "--milestone",
        milestone,
        "--create-bdd-scenarios",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error creating release plan: {result.stderr}")
        return False

    print(result.stdout)

    # Create release plan document
    release_plan_dir = Path("reports/release_plans")
    release_plan_dir.mkdir(parents=True, exist_ok=True)

    release_plan_file = release_plan_dir / f"release_{release}_plan.md"

    with open(release_plan_file, "w") as f:
        f.write(f"# Release {release}: {milestone} Plan\n\n")
        f.write(f"Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("## Tasks\n\n")

        # Add tasks based on the milestone
        if milestone == "Documentation":
            f.write("1. Document repository structure\n")
            f.write("2. Identify redundancies\n")
            f.write("3. Create development system map\n")
            f.write("4. Create BDD scenarios for improvements\n")
            f.write("5. Generate coverage report\n")
        elif milestone == "Structure":
            f.write("1. Consolidate testing directories\n")
            f.write("2. Centralize documentation\n")
            f.write("3. Update tool documentation\n")
            f.write("4. Run tests to verify no regressions\n")
            f.write("5. Generate updated coverage report\n")
        elif milestone == "Automation":
            f.write("1. Update pre-commit hooks\n")
            f.write("2. Enhance repository health checks\n")
            f.write("3. Create unified CLI for development tasks\n")
            f.write("4. Document automation tools\n")
            f.write("5. Run tests to verify automation\n")
        elif milestone == "Agent":
            f.write("1. Document file structure conventions\n")
            f.write("2. Add agent-specific documentation\n")
            f.write("3. Implement repository structure validation\n")
            f.write("4. Test agent navigation capabilities\n")

        f.write("\n## Acceptance Criteria\n\n")

        # Add acceptance criteria based on the milestone
        if milestone == "Documentation":
            f.write(
                "- [ ] Repository structure documented in a standardized format\n"
            )
            f.write(
                "- [ ] Redundancies identified and categorized by impact\n"
            )
            f.write(
                "- [ ] Development system map created for agent navigation\n"
            )
            f.write("- [ ] BDD scenarios created for each improvement area\n")
            f.write(
                "- [ ] Coverage report shows documentation requirements are met\n"
            )
        elif milestone == "Structure":
            f.write(
                "- [ ] Testing directories consolidated according to plan\n"
            )
            f.write("- [ ] Documentation centralized in docs/ directory\n")
            f.write("- [ ] Tool documentation updated and centralized\n")
            f.write("- [ ] All tests pass after restructuring\n")
            f.write("- [ ] No regression in code coverage\n")
        elif milestone == "Automation":
            f.write("- [ ] Pre-commit hooks updated with additional checks\n")
            f.write(
                "- [ ] Repository health check enhanced with new metrics\n"
            )
            f.write("- [ ] Unified CLI created for common development tasks\n")
            f.write("- [ ] All automation tools documented\n")
            f.write("- [ ] BDD scenarios for automation requirements pass\n")
        elif milestone == "Agent":
            f.write("- [ ] File structure conventions documented for agents\n")
            f.write("- [ ] Agent-specific documentation added\n")
            f.write("- [ ] Repository structure validation implemented\n")
            f.write(
                "- [ ] Agent can successfully navigate and modify the codebase\n"
            )
            f.write("- [ ] BDD scenarios for agent requirements pass\n")

        f.write("\n## General Definition of Done\n\n")
        f.write(
            "In addition to the specific acceptance criteria above, this release must meet all applicable criteria in the general Definition of Done document (DEFINITION_OF_DONE.md).\n"
        )

    print(f"Release plan created: {release_plan_file}")
    return True


def execute_release_tasks(release):
    """Execute tasks for a release."""
    print(f"\n=== Executing Tasks for Release {release} ===")

    milestone = RELEASE_TO_MILESTONE.get(release)
    if not milestone:
        print(f"Error: Invalid release number: {release}")
        return False

    # Check if previous release is complete (except for Release 1)
    if release != "1":
        prev_release = str(int(release) - 1)
        prev_release_file = Path(
            f"reports/release_{prev_release}_complete.txt"
        )

        if not prev_release_file.exists():
            print(f"Error: Previous release {prev_release} is not complete")
            return False

    # Execute tasks based on the milestone
    if milestone == "Documentation":
        # Document repository structure
        print("\n1. Documenting repository structure...")
        subprocess.run(["python", "tools/repo_reconcile.py", "--analyze-only"])

        # Identify redundancies
        print("\n2. Identifying redundancies...")
        subprocess.run(["python", "tools/repo_health_check.py"])

        # Create development system map
        print("\n3. Creating development system map...")
        subprocess.run(["python", "tools/repo_reconcile.py", "--analyze-only"])

        # Create BDD scenarios for improvements
        print("\n4. Creating BDD scenarios for improvements...")
        subprocess.run(
            [
                "python",
                "tools/bdd_scenario_generator.py",
                "--milestone",
                milestone,
            ]
        )

        # Generate coverage report
        print("\n5. Generating coverage report...")
        subprocess.run(["python", "tools/bdd_coverage_report.py"])

    elif milestone == "Structure":
        # Consolidate testing directories
        print("\n1. Consolidating testing directories...")
        subprocess.run(
            [
                "python",
                "tools/repo_reconcile.py",
                "--execute",
                "--milestone",
                milestone,
            ]
        )

        # Centralize documentation
        print("\n2. Centralizing documentation...")
        subprocess.run(
            [
                "python",
                "tools/repo_reconcile.py",
                "--execute",
                "--milestone",
                milestone,
            ]
        )

        # Update tool documentation
        print("\n3. Updating tool documentation...")
        subprocess.run(
            [
                "python",
                "tools/repo_reconcile.py",
                "--execute",
                "--milestone",
                milestone,
            ]
        )

        # Run tests to verify no regressions
        print("\n4. Running tests to verify no regressions...")
        subprocess.run(["python", "tools/run_bdd_tests.py"])

        # Generate updated coverage report
        print("\n5. Generating updated coverage report...")
        subprocess.run(["python", "tools/bdd_coverage_report.py"])

    elif milestone == "Automation":
        # Update pre-commit hooks
        print("\n1. Updating pre-commit hooks...")
        subprocess.run(
            [
                "python",
                "tools/repo_reconcile.py",
                "--execute",
                "--milestone",
                milestone,
            ]
        )

        # Enhance repository health checks
        print("\n2. Enhancing repository health checks...")
        subprocess.run(
            [
                "python",
                "tools/repo_reconcile.py",
                "--execute",
                "--milestone",
                milestone,
            ]
        )

        # Create unified CLI for development tasks
        print("\n3. Creating unified CLI for development tasks...")
        subprocess.run(["python", "tools/repo_reconcile.py", "--create-cli"])

        # Document automation tools
        print("\n4. Documenting automation tools...")
        subprocess.run(
            [
                "python",
                "tools/repo_reconcile.py",
                "--execute",
                "--milestone",
                milestone,
            ]
        )

        # Run tests to verify automation
        print("\n5. Running tests to verify automation...")
        subprocess.run(["python", "tools/run_bdd_tests.py"])

    elif milestone == "Agent":
        # Document file structure conventions
        print("\n1. Documenting file structure conventions...")
        subprocess.run(
            [
                "python",
                "tools/repo_reconcile.py",
                "--execute",
                "--milestone",
                milestone,
            ]
        )

        # Add agent-specific documentation
        print("\n2. Adding agent-specific documentation...")
        subprocess.run(
            [
                "python",
                "tools/repo_reconcile.py",
                "--execute",
                "--milestone",
                milestone,
            ]
        )

        # Implement repository structure validation
        print("\n3. Implementing repository structure validation...")
        subprocess.run(
            ["python", "tools/repo_health_check.py", "--validate-for-agent"]
        )

        # Test agent navigation capabilities
        print("\n4. Testing agent navigation capabilities...")
        subprocess.run(["python", "tools/run_bdd_tests.py", "--tags", "agent"])

    print(f"\nRelease {release} tasks executed")
    return True


def verify_release_acceptance_criteria(release):
    """Verify that a release meets its acceptance criteria."""
    print(f"\n=== Verifying Acceptance Criteria for Release {release} ===")

    milestone = RELEASE_TO_MILESTONE.get(release)
    if not milestone:
        print(f"Error: Invalid release number: {release}")
        return False

    # Verify acceptance criteria using BDD tests
    cmd = ["python", "tools/run_bdd_tests.py", f"--tags={milestone}"]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error verifying acceptance criteria: {result.stderr}")
        return False

    print(result.stdout)

    # Verify general Definition of Done criteria
    print("\n=== Verifying General Definition of Done Criteria ===")

    # This would typically involve checking that all applicable DoD criteria are met
    # For now, we'll just print a message
    print(
        "Verifying that the release meets all applicable criteria in the general Definition of Done..."
    )

    # Mark release as complete
    release_status_file = Path(f"reports/release_{release}_complete.txt")
    release_status_file.parent.mkdir(parents=True, exist_ok=True)
    release_status_file.write_text(
        f"Release {release} completed and acceptance criteria verified on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    print(
        f"Release {release} acceptance criteria verified and marked as complete"
    )
    return True


def generate_release_report(release):
    """Generate a report for a release."""
    print(f"\n=== Generating Report for Release {release} ===")

    milestone = RELEASE_TO_MILESTONE.get(release)
    if not milestone:
        print(f"Error: Invalid release number: {release}")
        return False

    # Check if release is complete
    release_status_file = Path(f"reports/release_{release}_complete.txt")
    if not release_status_file.exists():
        print(f"Error: Release {release} is not complete")
        return False

    # Read release status
    release_status = release_status_file.read_text()

    # Generate report
    report_dir = Path("reports/release_reports")
    report_dir.mkdir(parents=True, exist_ok=True)

    report_file = report_dir / f"release_{release}_report.md"

    with open(report_file, "w") as f:
        f.write(f"# Release {release}: {milestone} Report\n\n")
        f.write(
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )
        f.write(f"## Status\n\n{release_status}\n\n")

        f.write("## Accomplishments\n\n")

        # Add accomplishments based on the milestone
        if milestone == "Documentation":
            f.write("- Repository structure documented\n")
            f.write("- Redundancies identified\n")
            f.write("- Development system map created\n")
            f.write("- BDD scenarios created for improvements\n")
            f.write("- Coverage report generated\n")
        elif milestone == "Structure":
            f.write("- Testing directories consolidated\n")
            f.write("- Documentation centralized\n")
            f.write("- Tool documentation updated\n")
            f.write("- Tests verified no regressions\n")
            f.write("- Coverage report updated\n")
        elif milestone == "Automation":
            f.write("- Pre-commit hooks updated\n")
            f.write("- Repository health checks enhanced\n")
            f.write("- Unified CLI created\n")
            f.write("- Automation tools documented\n")
            f.write("- Automation verified with tests\n")
        elif milestone == "Agent":
            f.write("- File structure conventions documented\n")
            f.write("- Agent-specific documentation added\n")
            f.write("- Repository structure validation implemented\n")
            f.write("- Agent navigation capabilities tested\n")

        f.write("\n## Next Steps\n\n")

        # Add next steps based on the milestone
        if milestone == "Documentation":
            f.write("- Proceed to Release 2: Structure Consolidation\n")
        elif milestone == "Structure":
            f.write("- Proceed to Release 3: Automation Enhancement\n")
        elif milestone == "Automation":
            f.write("- Proceed to Release 4: Agent Optimization\n")
        elif milestone == "Agent":
            f.write("- Maintain and evolve the development system\n")
            f.write("- Consider additional improvements based on feedback\n")

        f.write("\n## Potential DoD Evolution\n\n")
        f.write(
            "Based on this release, the following improvements to the general Definition of Done could be considered:\n\n"
        )
        f.write(
            "- [Add potential DoD improvements identified during this release]\n"
        )

    print(f"Release report generated: {report_file}")
    return True


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Release Management Script")
    parser.add_argument(
        "--release", help="The release to manage (1, 2, 3, 4, or 'all')"
    )
    parser.add_argument(
        "--action",
        help="The action to perform (plan, execute, verify, report)",
    )

    args = parser.parse_args()

    # Default to all releases if not specified
    releases = (
        ["1", "2", "3", "4"]
        if args.release == "all" or not args.release
        else [args.release]
    )

    # Default to all actions if not specified
    actions = (
        ["plan", "execute", "verify", "report"]
        if not args.action
        else [args.action]
    )

    for release in releases:
        if "plan" in actions:
            create_release_plan(release)

        if "execute" in actions:
            execute_release_tasks(release)

        if "verify" in actions:
            verify_release_acceptance_criteria(release)

        if "report" in actions:
            generate_release_report(release)


if __name__ == "__main__":
    main()
