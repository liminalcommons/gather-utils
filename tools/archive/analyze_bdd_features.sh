#!/bin/bash
# BDD Features Analysis Script
# This script runs all BDD analysis tools to generate a comprehensive report for consolidation planning.

set -e  # Exit on error

# Configuration - modify these variables as needed
FEATURES_DIR="tests/bdd/features"
STEPS_DIR="tests/bdd/steps"
REQUIREMENTS_FILE="docs/requirements.json"
REPORTS_DIR="reports/bdd_analysis"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
OUTPUT_DIR="${REPORTS_DIR}/${TIMESTAMP}"

# Create directories
mkdir -p "$OUTPUT_DIR"
echo "Created output directory: $OUTPUT_DIR"

# Log file
LOG_FILE="${OUTPUT_DIR}/analysis_log.txt"
touch "$LOG_FILE"

# Function to log messages
log() {
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $1" | tee -a "$LOG_FILE"
}

log "Starting BDD Feature Analysis"
log "Features directory: $FEATURES_DIR"
log "Steps directory: $STEPS_DIR"
log "Requirements file: $REQUIREMENTS_FILE"

# Step 1: Run Duplication Analyzer
log "Running BDD Duplication Analyzer..."
python tools/bdd_duplication_analyzer.py \
    --feature-dir "$FEATURES_DIR" \
    --output-file "${OUTPUT_DIR}/duplication_report.md" \
    --threshold 0.75 \
    --tag-threshold 0.5 2>&1 | tee -a "$LOG_FILE"

# Step 2: Generate Traceability Matrix
log "Generating Traceability Matrix..."
python tools/bdd_traceability_matrix.py \
    --features-dir "$FEATURES_DIR" \
    --steps-dir "$STEPS_DIR" \
    --output "${OUTPUT_DIR}/traceability_matrix.md" 2>&1 | tee -a "$LOG_FILE"

# Step 3: Analyze Coverage
log "Analyzing BDD Coverage..."
python tools/bdd_coverage_report.py \
    --features-dir "$FEATURES_DIR" \
    --requirements-file "$REQUIREMENTS_FILE" \
    --output-dir "${OUTPUT_DIR}/coverage" 2>&1 | tee -a "$LOG_FILE"

# Step 4: Perform Gap Analysis
log "Performing Gap Analysis..."
python tools/bdd_gap_analysis.py \
    --coverage-data "${OUTPUT_DIR}/coverage/coverage_detailed.json" \
    --requirements-file "$REQUIREMENTS_FILE" \
    --output-dir "${OUTPUT_DIR}/gap_analysis" 2>&1 | tee -a "$LOG_FILE"

# Step 5: Generate Summary Report
log "Generating Analysis Summary Report..."
cat > "${OUTPUT_DIR}/analysis_summary.md" << EOF
# BDD Feature Analysis Summary

Analysis performed on: $(date)

## Overview

This report summarizes the analysis of BDD features in preparation for Release 2 (Feature Consolidation).
The analysis identified:

- Duplicate scenarios
- Overlapping features
- Tag inconsistencies
- Requirements coverage status
- Coverage gaps

## Reports

The following reports were generated:

1. [Duplication Report](./duplication_report.md) - Lists duplicate and overlapping scenarios
2. [Traceability Matrix](./traceability_matrix.md) - Maps requirements to scenarios
3. [Coverage Summary](./coverage/coverage_summary.md) - Provides coverage statistics
4. [Coverage Gaps](./coverage/coverage_gaps.md) - Identifies requirements with insufficient coverage
5. [Gap Analysis](./gap_analysis/gap_analysis.md) - Provides detailed gap analysis
6. [Action Plan](./gap_analysis/gap_action_plan.md) - Provides a prioritized action plan

## Next Steps

Based on these reports, the following actions should be taken:

1. Address duplicate scenarios identified in the duplication report
2. Consolidate overlapping features
3. Standardize inconsistent tags
4. Address high-priority coverage gaps
5. Reorganize feature files according to the BDD conventions

See the individual reports for detailed recommendations.
EOF

log "Creating stats summary..."
# Count features, scenarios, and requirements
FEATURE_COUNT=$(find "$FEATURES_DIR" -name "*.feature" | wc -l)
SCENARIO_COUNT=$(grep -r "Scenario:" "$FEATURES_DIR" --include="*.feature" | wc -l)
REQUIREMENT_COUNT=$(jq length "$REQUIREMENTS_FILE" 2>/dev/null || echo "N/A")

# Append stats to summary
cat >> "${OUTPUT_DIR}/analysis_summary.md" << EOF

## Statistics

- Total Feature Files: $FEATURE_COUNT
- Total Scenarios: $SCENARIO_COUNT
- Total Requirements: $REQUIREMENT_COUNT
- Analysis Timestamp: $TIMESTAMP
- Full Analysis Log: [analysis_log.txt](./analysis_log.txt)

EOF

log "Analysis complete. Reports available in $OUTPUT_DIR"
echo "==============================================="
echo "BDD Feature Analysis Complete"
echo "Reports are available in: $OUTPUT_DIR"
echo "Main summary report: ${OUTPUT_DIR}/analysis_summary.md"
echo "==============================================="
