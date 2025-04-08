"""
Tool: BDD Import Fixer
Created: 2025-03-22
Author: Development Team
Status: Active
Purpose: Fix import statements in BDD step definition files to use absolute imports
Dependencies: ast, re
Lifecycle:
    - Created: To resolve import dependencies and make step definitions more portable
    - Active: Used for refactoring BDD tests
    - Obsolescence Conditions:
        1. When all step definition files have been refactored
        2. When BDD framework is replaced
Last Validated: 2025-03-22
"""

import os
import re
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


def find_relative_imports(file_path: Path) -> List[Tuple[str, str]]:
    """Find relative imports in a file.
    
    Args:
        file_path: Path to the file
        
    Returns:
        List of tuples (import_line, module_path)
    """
    relative_imports = []
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find imports like: from ..common import x
    pattern1 = r'from\s+(\.+[a-zA-Z0-9_.]+)\s+import\s+([a-zA-Z0-9_,\s*]+)'
    for match in re.finditer(pattern1, content):
        import_line = match.group(0)
        module_path = match.group(1)
        relative_imports.append((import_line, module_path))
    
    # Find imports like: from . import x
    pattern2 = r'from\s+(\.[a-zA-Z0-9_.]*)\s+import\s+([a-zA-Z0-9_,\s*]+)'
    for match in re.finditer(pattern2, content):
        import_line = match.group(0)
        module_path = match.group(1)
        relative_imports.append((import_line, module_path))
    
    return relative_imports


def convert_to_absolute_import(file_path: Path, relative_module: str) -> Optional[str]:
    """Convert a relative import to an absolute import.
    
    Args:
        file_path: Path to the file containing the import
        relative_module: The relative module path
        
    Returns:
        The absolute module path, or None if conversion failed
    """
    # Get the directory of the file
    file_dir = file_path.parent
    
    # Count the dots in the relative path
    dot_count = 0
    for char in relative_module:
        if char == '.':
            dot_count += 1
        else:
            break
    
    # Get the relative part of the module
    module_part = relative_module[dot_count:]
    
    # Calculate the absolute path
    current_path = file_dir
    for _ in range(dot_count):
        current_path = current_path.parent
    
    # Get the absolute module path
    module_parts = []
    path_parts = current_path.parts
    
    # Find the 'tests' package to use as the base
    tests_index = -1
    for i, part in enumerate(path_parts):
        if part == 'tests':
            tests_index = i
            break
    
    if tests_index == -1:
        return None
    
    # Construct the absolute module path
    absolute_parts = path_parts[tests_index:]
    module_path = '.'.join(absolute_parts)
    
    if module_part:
        return f"{module_path}.{module_part}"
    else:
        return module_path


def fix_imports(file_path: Path, dry_run: bool = False) -> bool:
    """Fix imports in a file.
    
    Args:
        file_path: Path to the file
        dry_run: Whether to perform a dry run without making changes
        
    Returns:
        True if changes were made, False otherwise
    """
    relative_imports = find_relative_imports(file_path)
    if not relative_imports:
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    changes_made = False
    for import_line, module_path in relative_imports:
        absolute_path = convert_to_absolute_import(file_path, module_path)
        if absolute_path:
            new_import = import_line.replace(module_path, absolute_path)
            content = content.replace(import_line, new_import)
            changes_made = True
            print(f"  Converting: {import_line} -> {new_import}")
    
    if changes_made and not dry_run:
        with open(file_path, 'w') as f:
            f.write(content)
    
    return changes_made


def process_directory(directory: Path, dry_run: bool = False) -> Tuple[int, int]:
    """Process all Python files in a directory.
    
    Args:
        directory: Path to the directory
        dry_run: Whether to perform a dry run without making changes
        
    Returns:
        Tuple of (files_processed, files_modified)
    """
    files_processed = 0
    files_modified = 0
    
    for file_path in directory.rglob('*.py'):
        files_processed += 1
        print(f"Processing: {file_path}")
        if fix_imports(file_path, dry_run):
            files_modified += 1
    
    return files_processed, files_modified


def add_common_imports(file_path: Path, dry_run: bool = False) -> bool:
    """Add imports from the common imports module.
    
    Args:
        file_path: Path to the file
        dry_run: Whether to perform a dry run without making changes
        
    Returns:
        True if changes were made, False otherwise
    """
    # Check if the common imports are already in the file
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check if the file already imports from our utils.imports
    if 'from tests.bdd.utils.imports import' in content:
        return False
    
    # Add the import at the top of the file, after existing imports
    import_line = "from tests.bdd.utils.imports import *"
    
    # Find where to insert the import
    import_section_end = 0
    for match in re.finditer(r'import\s+[a-zA-Z0-9_,\s]+', content):
        end = match.end()
        if end > import_section_end:
            import_section_end = end
    
    for match in re.finditer(r'from\s+[a-zA-Z0-9_.]+\s+import\s+[a-zA-Z0-9_,\s*]+', content):
        end = match.end()
        if end > import_section_end:
            import_section_end = end
    
    if import_section_end > 0:
        # Insert after the last import
        new_content = content[:import_section_end] + "\n\n" + import_line + content[import_section_end:]
    else:
        # Insert at the beginning, after docstring if present
        docstring_end = 0
        docstring_match = re.search(r'""".*?"""', content, re.DOTALL)
        if docstring_match:
            docstring_end = docstring_match.end()
        
        new_content = content[:docstring_end] + "\n\n" + import_line + content[docstring_end:]
    
    if not dry_run:
        with open(file_path, 'w') as f:
            f.write(new_content)
    
    return True


def add_common_imports_to_directory(directory: Path, dry_run: bool = False) -> Tuple[int, int]:
    """Add common imports to all Python files in a directory.
    
    Args:
        directory: Path to the directory
        dry_run: Whether to perform a dry run without making changes
        
    Returns:
        Tuple of (files_processed, files_modified)
    """
    files_processed = 0
    files_modified = 0
    
    for file_path in directory.rglob('*.py'):
        # Skip __init__.py files
        if file_path.name == '__init__.py':
            continue
        
        files_processed += 1
        print(f"Adding common imports to: {file_path}")
        if add_common_imports(file_path, dry_run):
            files_modified += 1
    
    return files_processed, files_modified


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Fix import statements in BDD step definition files")
    parser.add_argument('--dir', type=str, default='tests/bdd/steps', 
                        help='Directory to process (default: tests/bdd/steps)')
    parser.add_argument('--dry-run', action='store_true', 
                        help='Perform a dry run without making changes')
    parser.add_argument('--add-common-imports', action='store_true',
                        help='Add common imports from utils.imports')
    
    args = parser.parse_args()
    
    directory = Path(args.dir)
    if not directory.exists():
        print(f"Error: Directory {args.dir} does not exist")
        return 1
    
    print(f"Processing directory: {directory}")
    
    if args.add_common_imports:
        files_processed, files_modified = add_common_imports_to_directory(directory, args.dry_run)
        action = "Would modify" if args.dry_run else "Modified"
        print(f"Added common imports: {action} {files_modified} of {files_processed} files")
    
    files_processed, files_modified = process_directory(directory, args.dry_run)
    action = "Would modify" if args.dry_run else "Modified"
    print(f"Fixed imports: {action} {files_modified} of {files_processed} files")
    
    return 0


if __name__ == '__main__':
    sys.exit(main()) 