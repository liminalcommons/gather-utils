# BDD Testing Infrastructure

This document describes the enhanced BDD testing infrastructure, which provides parallel execution, performance metrics, and detailed reporting.

## Test Runner

The test runner (`tools/bdd_test_runner.py`) provides the following features:

### Parallel Execution
```bash
# Run tests in parallel (default)
python tools/bdd_test_runner.py

# Run tests sequentially
python tools/bdd_test_runner.py --no-parallel

# Control parallel workers
python tools/bdd_test_runner.py --max-workers 4
```

### Test Selection
```bash
# Run specific tags
python tools/bdd_test_runner.py --tags REQ-1 REQ-2

# Exclude tags
python tools/bdd_test_runner.py --exclude-tags slow performance

# Stop on first failure
python tools/bdd_test_runner.py --fail-fast
```

### Test Output
```bash
# Capture stdout/stderr (default)
python tools/bdd_test_runner.py

# Don't capture output
python tools/bdd_test_runner.py --no-capture
```

### Failed Test Handling
```bash
# Rerun failed tests (default)
python tools/bdd_test_runner.py

# Skip rerunning failed tests
python tools/bdd_test_runner.py --no-rerun-failed
```

## Test Reports

The test runner generates comprehensive reports in:
```
test_results/bdd/
├── test_report.json     # Machine-readable results
├── test_report.html     # Interactive HTML report
└── {feature}_results.json   # Individual feature results
```

### HTML Report Features
1. **Summary Dashboard**
   - Total tests run
   - Pass/fail/skip counts
   - Overall duration

2. **Performance Metrics**
   - Total and average durations
   - Slowest/fastest scenarios
   - Step timing analysis
   - Resource usage metrics

3. **Interactive Results**
   - Expandable scenario details
   - Step-by-step results
   - Error messages and stack traces
   - Test output logs

4. **Performance Visualizations**
   - Scenario duration distribution
   - Step timing analysis
   - Resource usage graphs

## Pre-commit Integration

The test runner is integrated into the pre-commit workflow:

1. **BDD Tests Hook**
   - Runs on push
   - Sequential execution
   - All tests

2. **Performance Check Hook**
   - Runs on push
   - Only performance-tagged tests
   - Parallel execution

## Best Practices

### Test Organization
1. **Tag Usage**
   - `@performance` for performance-sensitive tests
   - `@slow` for time-consuming tests
   - `@REQ-{id}` for requirement traceability

2. **Performance Testing**
   - Add performance assertions
   - Use resource monitoring
   - Tag performance-critical scenarios

3. **Parallel Execution**
   - Ensure test independence
   - Use proper cleanup
   - Avoid shared resources

### Report Analysis
1. **Performance Monitoring**
   - Track scenario durations
   - Identify slow steps
   - Monitor resource usage

2. **Failure Analysis**
   - Check error messages
   - Review test output
   - Analyze step timing

3. **Continuous Improvement**
   - Optimize slow scenarios
   - Refactor common steps
   - Update performance baselines

## Configuration

### Test Runner Options
```bash
usage: bdd_test_runner.py [-h] [--base-dir BASE_DIR] [--no-parallel]
                         [--max-workers MAX_WORKERS]
                         [--tags [TAGS ...]]
                         [--exclude-tags [EXCLUDE_TAGS ...]]
                         [--fail-fast] [--no-rerun-failed]
                         [--no-capture]

Enhanced BDD test runner

optional arguments:
  -h, --help            show this help message and exit
  --base-dir BASE_DIR   Base directory containing the project
  --no-parallel         Disable parallel execution
  --max-workers MAX_WORKERS
                        Maximum number of parallel workers
  --tags [TAGS ...]     Only run features with these tags
  --exclude-tags [EXCLUDE_TAGS ...]
                        Exclude features with these tags
  --fail-fast          Stop on first failure
  --no-rerun-failed    Disable rerunning failed tests
  --no-capture         Don't capture stdout/stderr
```

### Pre-commit Configuration
```yaml
-   repo: local
    hooks:
    -   id: bdd-tests
        name: BDD Tests
        entry: python tools/bdd_test_runner.py
        language: python
        files: ^(tests/bdd/.*\.feature|tests/bdd/steps/.*\.py)$
        pass_filenames: false
        stages: [push]
        args: ["--no-parallel"]

    -   id: bdd-performance
        name: BDD Performance Check
        entry: python tools/bdd_test_runner.py
        language: python
        files: ^(tests/bdd/.*\.feature|tests/bdd/steps/.*\.py)$
        pass_filenames: false
        stages: [push]
        args: ["--tags", "performance"]
```

## Future Enhancements

1. **Resource Monitoring**
   - CPU profiling
   - Memory tracking
   - I/O metrics

2. **Report Enhancements**
   - Trend analysis
   - Historical comparisons
   - Performance regression detection

3. **Test Optimization**
   - Dynamic parallelization
   - Test prioritization
   - Resource-aware scheduling 