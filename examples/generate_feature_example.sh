#!/bin/bash
# Example script demonstrating the BDD Feature Template Generator

# Ensure the script is executable
# chmod +x examples/generate_feature_example.sh

# Create output directory if it doesn't exist
mkdir -p examples/features/api
mkdir -p examples/steps/api

echo "Generating API Authentication feature..."
# Execute the feature template generator
python tools/bdd_feature_template.py \
  --output-dir examples/features \
  --domain api \
  --functionality authentication \
  --feature-name "API Authentication" \
  --description "This feature describes the authentication process for the API." \
  --actor "API user" \
  --action "authenticate with the API" \
  --benefit "access protected resources" \
  --requirements REQ-API-101 REQ-API-102 REQ-API-103 \
  --release 1 \
  --background \
  --num-scenarios 3 \
  --with-outline \
  --generate-steps

echo "Feature generation complete. Check examples/features/api directory for the generated files."
echo "Step definitions are in examples/steps/api directory."

# Optionally, display the generated files
echo "\nGenerated Feature File:"
cat examples/features/api/api_authentication.feature

echo "\nGenerated Step Definitions:"
cat examples/steps/api/api_authentication_steps.py 