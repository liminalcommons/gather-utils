#!/usr/bin/env python3
"""
BDD Test Coverage Report Generator

This script analyzes BDD feature files and generates a report showing which
requirements from the project plan are covered by BDD scenarios.

Usage:
    python tools/bdd_coverage_report.py

Output:
    - A markdown report showing test coverage
    - A JSON file with detailed coverage data
"""
import json
import os
import re
from collections import defaultdict
from pathlib import Path


def extract_requirements_from_plan(plan_file):
    """Extract requirements from the project plan markdown file."""
    requirements = []
    
    with open(plan_file, 'r') as f:
        content = f.read()
        
        # Find all milestones
        milestones = {}
        for milestone_match in re.finditer(r'### Milestone \d+: (.+?)(?=\n)', content):
            milestone_name = milestone_match.group(1)
            milestone_pos = milestone_match.start()
            milestones[milestone_pos] = milestone_name
        
        # Sort milestones by position
        sorted_milestones = sorted(milestones.items())
        
        # Find all tasks
        for task_match in re.finditer(r'\*\*Task (\d+\.\d+): (.+?)\*\*', content):
            task_id = task_match.group(1)
            task_name = task_match.group(2)
            task_pos = task_match.start()
            req_id = f"REQ-{task_id}"
            
            # Find the milestone this task belongs to
            current_milestone = None
            for pos, name in sorted_milestones:
                if pos < task_pos:
                    current_milestone = name
                else:
                    break
            
            if current_milestone:
                requirements.append({
                    'id': req_id,
                    'milestone': current_milestone,
                    'task_id': task_id,
                    'name': task_name,
                    'covered': False,
                    'scenarios': []
                })
    
    return requirements


def extract_scenarios_from_features(feature_dir):
    """Extract scenarios and their tags from feature files."""
    scenarios = []
    
    for feature_file in Path(feature_dir).glob('*.feature'):
        current_feature = None
        current_scenario = None
        
        with open(feature_file, 'r') as f:
            for line in f:
                line = line.strip()
                
                # Extract feature
                if line.startswith('Feature:'):
                    current_feature = line[8:].strip()
                
                # Extract tags
                elif line.startswith('@'):
                    tags = line.split()
                
                # Extract scenario
                elif line.startswith('Scenario:') and current_feature:
                    if current_scenario:
                        scenarios.append(current_scenario)
                    
                    current_scenario = {
                        'feature': current_feature,
                        'name': line[9:].strip(),
                        'file': str(feature_file),
                        'tags': tags if 'tags' in locals() else [],
                        'steps': []
                    }
                    tags = []
                
                # Extract steps
                elif (line.startswith('Given ') or line.startswith('When ') or 
                      line.startswith('Then ') or line.startswith('And ')) and current_scenario:
                    current_scenario['steps'].append(line)
            
            # Add the last scenario
            if current_scenario:
                scenarios.append(current_scenario)
    
    return scenarios


def map_scenarios_to_requirements(requirements, scenarios):
    """Map scenarios to requirements based on tags."""
    # Create a lookup dictionary for requirements
    req_dict = {req['id']: req for req in requirements}
    
    # Map scenarios to requirements
    for scenario in scenarios:
        for tag in scenario['tags']:
            if tag.startswith('@REQ-'):
                req_id = tag[1:]  # Remove the @ symbol
                if req_id in req_dict:
                    req_dict[req_id]['covered'] = True
                    req_dict[req_id]['scenarios'].append({
                        'name': scenario['name'],
                        'feature': scenario['feature'],
                        'file': scenario['file']
                    })
    
    return requirements


def generate_coverage_report(requirements, output_dir):
    """Generate a coverage report in markdown format."""
    # Calculate coverage statistics
    total_reqs = len(requirements)
    covered_reqs = sum(1 for req in requirements if req['covered'])
    coverage_percent = (covered_reqs / total_reqs * 100) if total_reqs > 0 else 0
    
    # Group requirements by milestone
    reqs_by_milestone = defaultdict(list)
    for req in requirements:
        reqs_by_milestone[req['milestone']].append(req)
    
    # Generate the report
    report = [
        "# BDD Test Coverage Report",
        "",
        f"**Total Requirements:** {total_reqs}",
        f"**Covered Requirements:** {covered_reqs}",
        f"**Coverage:** {coverage_percent:.2f}%",
        "",
        "## Coverage by Milestone",
        ""
    ]
    
    for milestone, reqs in reqs_by_milestone.items():
        milestone_total = len(reqs)
        milestone_covered = sum(1 for req in reqs if req['covered'])
        milestone_percent = (milestone_covered / milestone_total * 100) if milestone_total > 0 else 0
        
        report.append(f"### {milestone}")
        report.append(f"**Coverage:** {milestone_percent:.2f}% ({milestone_covered}/{milestone_total})")
        report.append("")
        report.append("| Requirement | Name | Covered | Scenarios |")
        report.append("|------------|------|---------|-----------|")
        
        for req in reqs:
            status = "✅" if req['covered'] else "❌"
            scenario_count = len(req['scenarios'])
            scenario_text = f"{scenario_count} scenario{'s' if scenario_count != 1 else ''}" if scenario_count > 0 else "None"
            
            report.append(f"| {req['id']} | {req['name']} | {status} | {scenario_text} |")
        
        report.append("")
    
    # Write the report to a file
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, 'bdd_coverage_report.md'), 'w') as f:
        f.write('\n'.join(report))
    
    # Write the raw data to a JSON file
    with open(os.path.join(output_dir, 'bdd_coverage_data.json'), 'w') as f:
        json.dump({
            'summary': {
                'total_requirements': total_reqs,
                'covered_requirements': covered_reqs,
                'coverage_percent': coverage_percent
            },
            'requirements': requirements
        }, f, indent=2)
    
    return os.path.join(output_dir, 'bdd_coverage_report.md')


def main():
    """Main function to generate the BDD coverage report."""
    # Define paths
    project_root = Path(__file__).parent.parent
    plan_file = project_root / 'docs' / 'project' / 'plan-release0.md'
    feature_dir = project_root / 'features'
    output_dir = project_root / 'reports'
    
    # Extract requirements and scenarios
    requirements = extract_requirements_from_plan(plan_file)
    scenarios = extract_scenarios_from_features(feature_dir)
    
    # Map scenarios to requirements
    requirements = map_scenarios_to_requirements(requirements, scenarios)
    
    # Generate the report
    report_file = generate_coverage_report(requirements, output_dir)
    
    print(f"BDD coverage report generated: {report_file}")


if __name__ == '__main__':
    main() 