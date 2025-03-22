# BDD Tools Suite

This document provides instructions for using the BDD toolset that has been developed as part of our BDD refactoring initiative. These tools help analyze, improve, and maintain our BDD feature files.

## Overview

The BDD Tools Suite consists of the following tools:

1. **BDD Duplication Analyzer**: Identifies duplicate and overlapping scenarios across feature files
2. **BDD Traceability Matrix Generator**: Creates a matrix mapping requirements to scenarios
3. **BDD Coverage Report Generator**: Analyzes coverage of requirements by BDD scenarios
4. **BDD Gap Analysis Tool**: Identifies coverage gaps and provides recommendations

Together, these tools provide a comprehensive solution for analyzing and improving your BDD test suite.

## Installation

All tools are Python-based and have minimal dependencies. To install dependencies:

```bash
pip install -r requirements.txt
```

## BDD Duplication Analyzer

### Purpose
The Duplication Analyzer identifies duplicate scenarios, semantically similar scenarios, overlapping features, and tag inconsistencies in your BDD feature files.

### Usage
```bash
python tools/bdd_duplication_analyzer.py --feature-dir tests/bdd/features --output-file reports/duplication_report.md
```

### Options
- `--feature-dir`: Directory containing BDD feature files
- `--output-file`: File to write the duplication report to
- `--threshold`: Similarity threshold (default: 0.75)
- `--tag-threshold`: Tag overlap threshold (default: 0.5)

### Output
The tool generates a markdown report that lists:
- Exact duplicates
- Semantic duplicates
- Overlapping features
- Tag inconsistencies

Each issue includes recommendations for resolving the duplication or inconsistency.

## BDD Traceability Matrix Generator

### Purpose
The Traceability Matrix Generator creates a matrix that maps requirements to BDD scenarios, helping ensure full requirement coverage.

### Usage
```bash
python tools/bdd_traceability_matrix.py --features-dir tests/bdd/features --steps-dir tests/bdd/steps --output reports/traceability_matrix.md
```

### Options
- `--features-dir`: Directory containing BDD feature files
- `--steps-dir`: Directory containing step definition files
- `--output`: Output markdown file

### Output
The tool generates a markdown file containing a traceability matrix with the following columns:
- Requirement ID
- Requirement Description
- Feature File
- Scenario(s)
- Step Definition File(s)
- Test Status
- Coverage

## BDD Coverage Report Generator

### Purpose
The Coverage Report Generator analyzes BDD feature files and requirements to generate a coverage report, identifying gaps in BDD coverage.

### Usage
```bash
python tools/bdd_coverage_report.py --features-dir tests/bdd/features --requirements-file docs/requirements.json --output-dir reports/coverage
```

### Options
- `--features-dir`: Directory containing BDD feature files
- `--requirements-file`: File containing requirements data (CSV or JSON)
- `--output-dir`: Directory for output reports

### Output
The tool generates several reports in the output directory:
- `coverage_summary.md`: Overall coverage statistics
- `coverage_detailed.json`: Detailed JSON data about coverage
- `coverage_gaps.md`: Analysis of coverage gaps

## BDD Gap Analysis Tool

### Purpose
The Gap Analysis Tool identifies areas where requirements lack adequate BDD coverage and provides prioritized recommendations for improving test coverage.

### Usage
```bash
python tools/bdd_gap_analysis.py --coverage-data reports/coverage/coverage_detailed.json --requirements-file docs/requirements.json --output-dir reports/gap_analysis
```

### Options
- `--coverage-data`: JSON file containing coverage data
- `--requirements-file`: File containing requirements data (CSV or JSON)
- `--areas-file`: Optional file containing requirement areas data
- `--output-dir`: Directory for output reports

### Output
The tool generates several reports in the output directory:
- `gap_analysis.md`: Detailed gap analysis report
- `gap_analysis_data.json`: JSON data about gaps
- `gap_action_plan.md`: Prioritized action plan for addressing gaps

## Workflow - Analyzing and Improving BDD Coverage

Here's a typical workflow using these tools:

1. **Analyze for Duplicates**:
   ```bash
   python tools/bdd_duplication_analyzer.py --feature-dir tests/bdd/features --output-file reports/duplication_report.md
   ```

2. **Clean up duplicates and inconsistencies** based on the duplication report

3. **Generate Traceability Matrix**:
   ```bash
   python tools/bdd_traceability_matrix.py --features-dir tests/bdd/features --output reports/traceability_matrix.md
   ```

4. **Analyze Coverage**:
   ```bash
   python tools/bdd_coverage_report.py --features-dir tests/bdd/features --requirements-file docs/requirements.json --output-dir reports/coverage
   ```

5. **Perform Gap Analysis**:
   ```bash
   python tools/bdd_gap_analysis.py --coverage-data reports/coverage/coverage_detailed.json --requirements-file docs/requirements.json --output-dir reports/gap_analysis
   ```

6. **Implement Action Plan** based on the gap analysis report

7. **Repeat the process** to monitor improvement

## Requirements File Format

The requirements file can be either CSV or JSON format:

### CSV Format
```csv
ID,Description,Priority,Area,Tags
CLI-1,System shall list maps in a space,High,CLI,ui,map
CLI-2,System shall explore portals in a map,Medium,CLI,portal,map
API-1,System shall authenticate with API,High,API,security
```

### JSON Format
```json
[
  {
    "id": "CLI-1",
    "description": "System shall list maps in a space",
    "priority": "High",
    "area": "CLI",
    "tags": ["ui", "map"]
  },
  {
    "id": "CLI-2",
    "description": "System shall explore portals in a map",
    "priority": "Medium",
    "area": "CLI",
    "tags": ["portal", "map"]
  }
]
```

## Continuous Integration Integration

These tools can be integrated into your CI/CD pipeline to provide regular reports on BDD test coverage.

Example GitHub Actions workflow:

```yaml
name: BDD Coverage Analysis

on:
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 0 * * 1'  # Weekly on Monday

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Generate reports
        run: |
          python tools/bdd_duplication_analyzer.py --feature-dir tests/bdd/features --output-file reports/duplication_report.md
          python tools/bdd_traceability_matrix.py --features-dir tests/bdd/features --output reports/traceability_matrix.md
          python tools/bdd_coverage_report.py --features-dir tests/bdd/features --requirements-file docs/requirements.json --output-dir reports/coverage
          python tools/bdd_gap_analysis.py --coverage-data reports/coverage/coverage_detailed.json --requirements-file docs/requirements.json --output-dir reports/gap_analysis
      - name: Archive reports
        uses: actions/upload-artifact@v2
        with:
          name: bdd-reports
          path: reports/
```

## Best Practices

1. **Regular Analysis**: Run these tools regularly (weekly or after significant changes)
2. **Address High Risk Gaps First**: Prioritize fixing high-risk coverage gaps
3. **Standardize Tags**: Use consistent tagging patterns across all feature files
4. **Maintain Requirements**: Keep your requirements file up to date
5. **Automate Coverage Checks**: Include coverage analysis in your CI pipeline
6. **Use Tag Conventions**: Follow the conventions in the [BDD Conventions document](./bdd_conventions.md)

## Troubleshooting

### Common Issues

1. **No Requirements Found**:
   - Ensure your requirements file is properly formatted
   - Check that requirement IDs match the format in your feature tags

2. **Low Coverage Reports**:
   - Verify that your BDD features use the correct requirement tags
   - Check the format of your requirement tags (should be @REQ-[domain]-[number])

3. **No Duplicates Found**:
   - Adjust the similarity threshold (try lowering it)
   - Check that feature files are properly formatted

4. **Performance Issues**:
   - For large feature sets, consider analyzing subsets of features
   - Optimize by specifying a smaller target directory

## Support

For questions or issues, please contact the BDD Refactoring Initiative team. 