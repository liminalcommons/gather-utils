#!/usr/bin/env python3
"""
Build the documentation using MkDocs.

This script builds the documentation using MkDocs and deploys it to GitHub Pages.
"""
import os
import subprocess
import sys
from pathlib import Path


def check_dependencies():
    """Check if the required dependencies are installed."""
    try:
        subprocess.run(["mkdocs", "--version"], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: mkdocs is not installed. Please install it with:")
        print("pip install mkdocs mkdocs-material mkdocstrings pymdown-extensions")
        sys.exit(1)


def build_docs():
    """Build the documentation using MkDocs."""
    # Change to the docs directory
    docs_dir = Path(__file__).parent.parent / "docs"
    os.chdir(docs_dir)

    # Build the documentation
    print("Building documentation...")
    result = subprocess.run(["mkdocs", "build"], check=False)
    
    if result.returncode != 0:
        print("Error: Failed to build documentation.")
        sys.exit(1)
    
    print("Documentation built successfully.")
    print(f"Output directory: {docs_dir}/site")


def deploy_docs():
    """Deploy the documentation to GitHub Pages."""
    # Change to the docs directory
    docs_dir = Path(__file__).parent.parent / "docs"
    os.chdir(docs_dir)

    # Deploy the documentation
    print("Deploying documentation to GitHub Pages...")
    result = subprocess.run(["mkdocs", "gh-deploy", "--force"], check=False)
    
    if result.returncode != 0:
        print("Error: Failed to deploy documentation.")
        sys.exit(1)
    
    print("Documentation deployed successfully to GitHub Pages.")


def main():
    """Main function."""
    # Check if the required dependencies are installed
    check_dependencies()

    # Parse command-line arguments
    if len(sys.argv) > 1 and sys.argv[1] == "--deploy":
        deploy_docs()
    else:
        build_docs()


if __name__ == "__main__":
    main() 