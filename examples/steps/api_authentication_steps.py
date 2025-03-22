#!/usr/bin/env python3
"""
Step definitions for api_authentication feature
Created: 2023-06-15
"""

import json

import requests
from behave import given, then, when
from hamcrest import assert_that, equal_to


# Mock API client for demonstration
class ApiClient:
    def __init__(self):
        self.base_url = "https://api.example.com"
        self.token = None
        self.last_response = None

    def authenticate(self, auth_type, credentials):
        # Mock authentication logic
        if "invalid" in credentials:
            self.last_response = {
                "status": "error",
                "message": "Invalid credentials",
            }
            return False
        else:
            self.token = "mock_token_12345"
            self.last_response = {"status": "success", "token": self.token}
            return True


# Given steps
@given("the system is ready for authentication operations")
def given_system_ready(context):
    """Implementation for: the system is ready for authentication operations"""
    # Setup the API client
    context.api_client = ApiClient()
    assert context.api_client is not None


@given("the authentication system is configured")
def given_auth_system_configured(context):
    """Implementation for: the authentication system is configured"""
    # Ensure API client is setup with default configuration
    if not hasattr(context, "api_client"):
        context.api_client = ApiClient()

    # Set default auth type
    context.auth_type = "basic"
    assert context.api_client is not None


@given("the authentication system is configured with {auth_type}")
def given_auth_system_configured_with_type(context, auth_type):
    """Implementation for: the authentication system is configured with auth_type"""
    # Setup API client with specific auth type
    if not hasattr(context, "api_client"):
        context.api_client = ApiClient()

    context.auth_type = auth_type
    assert context.auth_type in ["basic", "oauth"]


# When steps
@when("the user performs authentication with valid credentials")
def when_auth_with_valid_credentials(context):
    """Implementation for: the user performs authentication with valid credentials"""
    # Use the auth type from context or default to basic
    auth_type = getattr(context, "auth_type", "basic")
    credentials = f"valid_{auth_type}"

    # Perform authentication
    result = context.api_client.authenticate(auth_type, credentials)
    context.authentication_result = result
    assert context.authentication_result is True


@when("the user performs authentication with invalid credentials")
def when_auth_with_invalid_credentials(context):
    """Implementation for: the user performs authentication with invalid credentials"""
    # Use the auth type from context or default to basic
    auth_type = getattr(context, "auth_type", "basic")
    credentials = f"invalid_{auth_type}"

    # Perform authentication
    result = context.api_client.authenticate(auth_type, credentials)
    context.authentication_result = result
    assert context.authentication_result is False


@when("the user performs authentication with {credential}")
def when_auth_with_credential(context, credential):
    """Implementation for: the user performs authentication with credential"""
    # Use the auth type from context
    auth_type = context.auth_type

    # Perform authentication
    result = context.api_client.authenticate(auth_type, credential)
    context.authentication_result = result

    # Don't assert here, as we're testing both valid and invalid cases


# Then steps
@then("the system responds with a valid authentication token")
def then_system_responds_with_token(context):
    """Implementation for: the system responds with a valid authentication token"""
    # Check that we got a token
    assert_that(context.api_client.token is not None, equal_to(True))
    assert_that(
        context.api_client.last_response["status"], equal_to("success")
    )


@then("the system responds with an authentication error")
def then_system_responds_with_error(context):
    """Implementation for: the system responds with an authentication error"""
    # Check that we got an error
    assert_that(context.api_client.token is None, equal_to(True))
    assert_that(context.api_client.last_response["status"], equal_to("error"))


@then("the system responds with {expected}")
def then_system_responds_with_expected(context, expected):
    """Implementation for: the system responds with expected"""
    if expected == "valid_token":
        assert_that(context.api_client.token is not None, equal_to(True))
        assert_that(
            context.api_client.last_response["status"], equal_to("success")
        )
    elif expected == "authentication_error":
        assert_that(context.api_client.token is None, equal_to(True))
        assert_that(
            context.api_client.last_response["status"], equal_to("error")
        )
    else:
        raise ValueError(f"Unknown expected response: {expected}")
