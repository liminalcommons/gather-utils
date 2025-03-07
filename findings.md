# Gather.town API Explorer - Troubleshooting Findings and Request for Information

## Introduction

Our Gather Manager application is designed to interact with the Gather.town API to retrieve space details and map data. Recently, we have encountered persistent HTTP 500 errors with a "Not Found" response when attempting to fetch space and map details—even though our API key (9HoXr7Xr4OpIA8o7) is newly generated and our space URL (https://app.gather.town/app/ELoGghDX4v3HEwI0/Liminal%20Commons) is accessible via the Gather app.

This document summarizes our testing and research, and outlines several points that require your review and input in order to resolve these issues.

## Summary of Findings

### 1. Environment & Credentials

- **API Key Usage:**  
  - We are passing the API key as an HTTP header.  
  - Since the API key has just been generated, we are confident in its validity.
- **Action Item:**  
  - Please double-check that the account associated with the newly generated API key is configured with Admin or Builder privileges for the Liminal Commons space.  
  - If there are any discrepancies in permissions, let us know immediately so we can adjust accordingly.

### 2. Space ID Format

- **Formatting Requirements:**  
  - The space identifier should use a backslash (`\`) instead of a forward slash (`/`).  
  - For example, instead of `ELoGghDX4v3HEwI0/Liminal Commons`, our code uses `ELoGghDX4v3HEwI0\\Liminal Commons`.  
  - When embedding this value in a URL, both the backslash and spaces must be URL-encoded (e.g., `%5C` for `\` and `%20` for spaces).
- **Action Item:**  
  - Could you review the expected format for the space ID in API calls?  
  - Please advise whether we should use the literal backslash-separated string (i.e., `ELoGghDX4v3HEwI0\\Liminal Commons`) or if a URL-encoded version (i.e., `ELoGghDX4v3HEwI0%5CLiminal%20Commons`) is required.

### 3. API Endpoint Structure

- **Endpoint Testing:**  
  - We have tried multiple endpoint formats:
    - `https://api.gather.town/v2/spaces/ELoGghDX4v3HEwI0`
    - `https://api.gather.town/v2/spaces/ELoGghDX4v3HEwI0/maps?useV2Map=true`
    - Other variations combining space ID and space name.
  - All these attempts result in a 500 error with a "Not Found" message.
- **Action Item:**  
  - Please confirm whether the endpoints we are using match the latest Gather.town API specifications.  
  - Are there any recent changes or additional query parameters (like `useV2Map=true`) that we must include for successful API calls?

### 4. Error Analysis

- **Observed Behavior:**  
  - Both our curl tests (using the API key as a Bearer token) and our Python client yield a 500 error, with an HTML page that indicates "404 - Not Found".  
  - This suggests that the resource may not be recognized, potentially due to issues with authentication, space ID formatting, or endpoint structure.
- **Action Item:**  
  - Could you check if there is any additional error information available from the API (such as specific error codes, logs, or header details) that might provide further insight into the root cause of these failures?  
  - Are there any known issues or beta-related limitations with the Gather.town API that could be influencing these responses?

## Test Code

Below is the test script we use to perform API requests with our client implementation:

```python
#!/usr/bin/env python3
"""Test Gather.town API using the GatherClient."""

from gather_manager.api.client import GatherClient

API_KEY = "9HoXr7Xr4OpIA8o7"
SPACE_ID = "ELoGghDX4v3HEwI0"
SPACE_NAME = "Liminal Commons"

# For code, use backslash between SPACE_ID and SPACE_NAME
code_space_id = f"{SPACE_ID}\\{SPACE_NAME}"

print(f"API Key: {API_KEY}")
print(f"Space ID: {SPACE_ID}")
print(f"Space Name: {SPACE_NAME}")
print(f"Code Space ID: {code_space_id}")

client = GatherClient(api_key=API_KEY)

print("\nFetching space info using SPACE_ID only...")
try:
    space = client.get_space(SPACE_ID)
    print("Space info:", space)
except Exception as e:
    print("Error fetching space info:", e)

print("\nFetching maps using SPACE_ID only...")
try:
    maps = client.get_maps(SPACE_ID)
    print("Maps:", maps)
except Exception as e:
    print("Error fetching maps:", e)
```

## Requested Information

To move forward, we kindly request the following from the development team:

1. **Account Permissions:**  
   - Verify that the account associated with the API key (9HoXr7Xr4OpIA8o7) is properly set up with Admin or Builder permissions on the Liminal Commons space.

2. **Space ID Format:**  
   - Confirm the exact format that the API expects for the space ID.  
   - Should we provide it as a plain string with a literal backslash (i.e., `ELoGghDX4v3HEwI0\\Liminal Commons`) or as a URL-encoded string?

3. **Endpoint Verification:**  
   - Confirm that we are using the correct API endpoints based on the latest documentation.  
   - Inform us of any endpoint changes, additional required query parameters, or extra headers necessary for a successful API call.

4. **Additional Error Insights:**  
   - Provide any internal logs or extra error details (headers, error codes, etc.) from Gather.town that might shed light on the 500 "Not Found" error.  
   - Advise if there are any known issues with the API (especially in beta) that might contribute to these errors.

## Next Steps

Based on your input, we plan to:
- Adjust our API client configuration (particularly regarding space ID formatting and endpoint usage).
- Modify error handling to capture more detailed API responses.
- Perform further tests using updated configurations, potentially leveraging tools like Postman for additional validation.

---

Your prompt review and feedback on these points are crucial for us to resolve the issues and complete the Gather Manager integration successfully. Thank you for your assistance. 