#!/bin/bash

# This script helps remove sensitive data from your git history using BFG Repo-Cleaner.
# WARNING: This operation rewrites git history. Make sure to back up your repository and coordinate with your team.
#
# Prerequisites:
# 1. Install BFG Repo-Cleaner (https://rtyley.github.io/bfg-repo-cleaner/)
#
# Usage:
#   bash cleanup_secrets.sh
#   Then run:
#   git reflog expire --expire=now --all && git gc --prune=now --aggressive

# Define the sensitive strings to remove. Update these values as needed.
SENSITIVE_STRINGS=(
  "9HoXr7Xr4OpIA8o7"
  "ELoGghDX4v3HEwI0"
)

# Remove any files matching .env or .env.example from history
echo "Removing .env and .env.example files from history..."
bfg --delete-files ".env*"

# Remove sensitive strings from history using --replace-text with an expressions file.
temp_file=$(mktemp)
for secret in "${SENSITIVE_STRINGS[@]}"; do
  echo "${secret}==>***REMOVED***" >> "$temp_file"
done
echo "Removing sensitive strings from history..."
bfg --replace-text "$temp_file"
rm "$temp_file"

echo "Cleanup complete. Now run:"
echo "git reflog expire --expire=now --all && git gc --prune=now --aggressive"
