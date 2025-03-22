#!/usr/bin/env python3
"""
BDD Test Structure Consolidation - Phase 4: Configuration Cleanup

This script implements Phase 4 of the BDD Test Structure Consolidation project:
1. Clean up duplicate entries in pytest.ini
2. Ensure behave.ini is correctly configured
3. Update environment setup in tests/bdd/environment.py

Usage:
    python config_cleanup.py
"""

import os
import re
import logging
import filecmp
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("config_cleanup.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Define the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()

# Define configuration files
PYTEST_INI = PROJECT_ROOT / "pytest.ini"
BEHAVE_INI = PROJECT_ROOT / "behave.ini"
ENVIRONMENT_PY = PROJECT_ROOT / "tests" / "bdd" / "environment.py"

def clean_pytest_ini():
    """Clean up duplicate entries in pytest.ini"""
    if not PYTEST_INI.exists():
        logger.warning(f"pytest.ini not found at {PYTEST_INI}")
        return False
    
    try:
        with open(PYTEST_INI, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract lines
        lines = content.splitlines()
        
        # Find [pytest] section
        pytest_section_index = -1
        for i, line in enumerate(lines):
            if line.strip() == "[pytest]":
                pytest_section_index = i
                break
        
        if pytest_section_index == -1:
            logger.warning("No [pytest] section found in pytest.ini")
            return False
        
        # Remove duplicate entries
        seen_settings = {}
        cleaned_lines = lines[:pytest_section_index + 1]  # Include [pytest] line
        
        for i in range(pytest_section_index + 1, len(lines)):
            line = lines[i]
            if line.strip() and not line.strip().startswith("#"):
                # For non-empty, non-comment lines, extract key
                if "=" in line:
                    key = line.split("=")[0].strip()
                    if key not in seen_settings:
                        seen_settings[key] = line
                        cleaned_lines.append(line)
                    else:
                        logger.info(f"Removing duplicate setting: {line}")
                else:
                    # Keep lines without '=' (section headers, etc.)
                    cleaned_lines.append(line)
            else:
                # Keep comments and empty lines
                cleaned_lines.append(line)
        
        # Ensure BDD settings
        bdd_settings = {
            "bdd_features_dir": "tests/bdd/features",
            "bdd_steps_dir": "tests/bdd/steps"
        }
        
        for key, value in bdd_settings.items():
            if key not in seen_settings:
                logger.info(f"Adding missing setting: {key}={value}")
                cleaned_lines.append(f"{key} = {value}")
        
        # Write back cleaned content
        cleaned_content = "\n".join(cleaned_lines)
        
        # Check if content changed
        if content != cleaned_content:
            with open(PYTEST_INI, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            logger.info(f"Updated pytest.ini with cleaned configuration")
            return True
        else:
            logger.info(f"No changes needed for pytest.ini")
            return False
            
    except Exception as e:
        logger.error(f"Error cleaning pytest.ini: {e}")
        return False

def update_behave_ini():
    """Ensure behave.ini is correctly configured"""
    expected_content = """[behave]
# Define the paths for features and steps
paths = tests/bdd/features
steps_dir = tests/bdd/steps
# Output configuration
junit = true
junit_directory = reports/junit
format = pretty
outfile = reports/bdd_test_results.txt
show_skipped = true
show_timings = true
# Don't stop on first failure
stop = false
"""

    try:
        if not BEHAVE_INI.exists():
            # Create new behave.ini if it doesn't exist
            with open(BEHAVE_INI, 'w', encoding='utf-8') as f:
                f.write(expected_content)
            logger.info(f"Created new behave.ini with correct configuration")
            return True
        
        # Read existing behave.ini
        with open(BEHAVE_INI, 'r', encoding='utf-8') as f:
            current_content = f.read()
        
        # Parse the current content
        current_config = parse_ini_content(current_content)
        expected_config = parse_ini_content(expected_content)
        
        # Merge configurations, prioritizing expected values for paths and steps_dir
        final_config = {}
        for section, settings in current_config.items():
            final_config[section] = settings.copy()
        
        # Ensure behave section exists
        if 'behave' not in final_config:
            final_config['behave'] = {}
            
        # Update with expected values for critical settings
        for key, value in expected_config.get('behave', {}).items():
            if key in ['paths', 'steps_dir']:
                final_config['behave'][key] = value
        
        # Format the final configuration back to INI format
        final_content = format_ini_content(final_config)
        
        # Check if content changed
        if current_content != final_content:
            with open(BEHAVE_INI, 'w', encoding='utf-8') as f:
                f.write(final_content)
            logger.info(f"Updated behave.ini with correct configuration")
            return True
        else:
            logger.info(f"No changes needed for behave.ini")
            return False
            
    except Exception as e:
        logger.error(f"Error updating behave.ini: {e}")
        return False

def parse_ini_content(content):
    """Parse INI content into a dictionary structure"""
    config = {}
    current_section = None
    
    lines = content.splitlines()
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        # Check for section header
        section_match = re.match(r'\[(.*?)\]', line)
        if section_match:
            current_section = section_match.group(1)
            config[current_section] = {}
            continue
            
        # Parse key=value pair
        if current_section and '=' in line:
            key, value = [part.strip() for part in line.split('=', 1)]
            config[current_section][key] = value
    
    return config

def format_ini_content(config):
    """Format a configuration dictionary back to INI content"""
    lines = []
    
    for section, settings in config.items():
        lines.append(f"[{section}]")
        for key, value in settings.items():
            lines.append(f"{key} = {value}")
        lines.append("")  # Empty line between sections
    
    return "\n".join(lines)

def update_environment_py():
    """Update environment setup in tests/bdd/environment.py"""
    if not ENVIRONMENT_PY.exists():
        logger.warning(f"environment.py not found at {ENVIRONMENT_PY}")
        # Create a basic environment.py file
        create_basic_environment_py()
        return True
    
    try:
        with open(ENVIRONMENT_PY, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if the environment.py file contains necessary imports and hooks
        required_hooks = ['before_all', 'after_all', 'before_feature', 'after_feature', 
                           'before_scenario', 'after_scenario']
        
        # Check which hooks are missing
        missing_hooks = []
        for hook in required_hooks:
            if f"def {hook}(" not in content:
                missing_hooks.append(hook)
        
        # If all hooks are present, no changes needed
        if not missing_hooks:
            logger.info(f"No changes needed for environment.py - all required hooks present")
            return False
        
        # Add missing hooks
        updated_content = content.rstrip() + "\n\n"
        for hook in missing_hooks:
            logger.info(f"Adding missing hook: {hook}")
            updated_content += f"""
def {hook}(context, {'feature' if 'feature' in hook else 'scenario' if 'scenario' in hook else ''}):
    \"\"\"
    {hook.replace('_', ' ').capitalize()} hook.
    \"\"\"
    pass
"""
        
        # Write back updated content
        with open(ENVIRONMENT_PY, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        logger.info(f"Updated environment.py with missing hooks: {', '.join(missing_hooks)}")
        return True
            
    except Exception as e:
        logger.error(f"Error updating environment.py: {e}")
        return False

def create_basic_environment_py():
    """Create a basic environment.py file with all required hooks"""
    basic_content = """# BDD test environment setup
from behave import fixture, use_fixture

def before_all(context):
    \"\"\"Before all hook.\"\"\"
    # Setup code that runs before all features
    pass

def after_all(context):
    \"\"\"After all hook.\"\"\"
    # Cleanup code that runs after all features
    pass

def before_feature(context, feature):
    \"\"\"Before feature hook.\"\"\"
    # Setup code that runs before each feature
    pass

def after_feature(context, feature):
    \"\"\"After feature hook.\"\"\"
    # Cleanup code that runs after each feature
    pass

def before_scenario(context, scenario):
    \"\"\"Before scenario hook.\"\"\"
    # Setup code that runs before each scenario
    pass

def after_scenario(context, scenario):
    \"\"\"After scenario hook.\"\"\"
    # Cleanup code that runs after each scenario
    pass
"""

    try:
        # Create directory if it doesn't exist
        ENVIRONMENT_PY.parent.mkdir(parents=True, exist_ok=True)
        
        # Write the environment.py file
        with open(ENVIRONMENT_PY, 'w', encoding='utf-8') as f:
            f.write(basic_content)
        
        logger.info(f"Created basic environment.py file at {ENVIRONMENT_PY}")
        return True
    except Exception as e:
        logger.error(f"Error creating environment.py: {e}")
        return False

def main():
    """Main function to execute the configuration cleanup process"""
    logger.info("Starting Phase 4: Configuration Cleanup")
    
    changes_made = False
    
    # Step 1: Clean up duplicate entries in pytest.ini
    print("\n=== Cleaning up pytest.ini ===")
    if clean_pytest_ini():
        print("Updated pytest.ini with cleaned configuration")
        changes_made = True
    else:
        print("No changes needed for pytest.ini")
    
    # Step 2: Ensure behave.ini is correctly configured
    print("\n=== Updating behave.ini ===")
    if update_behave_ini():
        print("Updated behave.ini with correct configuration")
        changes_made = True
    else:
        print("No changes needed for behave.ini")
    
    # Step 3: Update environment setup in tests/bdd/environment.py
    print("\n=== Updating environment.py ===")
    if update_environment_py():
        print("Updated environment.py with required hooks")
        changes_made = True
    else:
        print("No changes needed for environment.py")
    
    if changes_made:
        logger.info("Phase 4: Configuration Cleanup completed with changes")
        print("\nPhase 4: Configuration Cleanup completed with changes")
    else:
        logger.info("Phase 4: Configuration Cleanup completed with no changes needed")
        print("\nPhase 4: Configuration Cleanup completed with no changes needed")
    
    print("\nNext steps:")
    print("1. Proceed to Phase 5: Verification")

if __name__ == "__main__":
    main() 