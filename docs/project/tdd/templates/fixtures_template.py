"""
Test fixtures for [module_name] tests.

Test Fixture Metadata:
- Created: YYYY-MM-DD
- Last Updated: YYYY-MM-DD
- Status: Draft
- Owner: [Team/Individual]
- Purpose: [Brief description of what these fixtures are for]
- Lifecycle:
  - Created: [Why these fixtures were created]
  - Active: [Current usage status]
  - Obsolescence Conditions:
    1. [When these fixtures would be considered obsolete]
    2. [Additional condition if applicable]
- Last Validated: YYYY-MM-DD

Changelog:
- YYYY-MM-DD | [Author] | [Description of change]
"""

import pytest
from [module_path] import [ModuleName]

# Test data constants
SAMPLE_DATA = {
    "id": 1,
    "name": "Test Name",
    "values": [1, 2, 3]
}


@pytest.fixture(scope="function")
def basic_fixture():
    """
    Create a basic test object.
    
    This fixture provides a basic instance of [ModuleName] with default values
    for unit testing.
    
    Returns:
        [ModuleName]: An instance with test values.
    """
    return [ModuleName](param1="test", param2=123)


@pytest.fixture(scope="function")
def configured_fixture():
    """
    Create a configured test object.
    
    This fixture provides an instance of [ModuleName] that has been configured
    with specific test values for edge case testing.
    
    Returns:
        [ModuleName]: A configured instance for testing.
    """
    obj = [ModuleName](param1="custom", param2=456)
    obj.configure(option1=True, option2="test")
    return obj


@pytest.fixture(scope="module")
def expensive_resource():
    """
    Create an expensive resource that should be reused across tests.
    
    This fixture sets up a resource that is expensive to create and should be
    reused across multiple tests within the same module.
    
    Yields:
        object: The expensive resource.
    """
    # Setup code
    resource = [ExpensiveResource]()
    resource.initialize()
    
    yield resource
    
    # Teardown code
    resource.cleanup()


@pytest.fixture
def mock_dependency(mocker):
    """
    Mock an external dependency.
    
    This fixture provides a mock for an external dependency that should not
    be called during unit testing.
    
    Args:
        mocker: The pytest-mock fixture.
        
    Returns:
        MagicMock: A configured mock object.
    """
    mock = mocker.patch("[module_path].external_dependency")
    mock.return_value = "mocked_value"
    return mock


@pytest.fixture(params=[
    ("input1", "expected1"),
    ("input2", "expected2"),
    ("input3", "expected3"),
])
def multiple_test_cases(request):
    """
    Provide multiple test cases.
    
    This parametrized fixture provides multiple input/expected output
    combinations for testing.
    
    Args:
        request: The pytest request object.
        
    Returns:
        tuple: A tuple containing (input_value, expected_output).
    """
    return request.param


# Factory functions for creating test data
def create_test_user(name="Test User", role="user", active=True):
    """
    Create a test user with customizable properties.
    
    This factory function creates test users with default values that can
    be overridden as needed.
    
    Args:
        name (str): The user's name.
        role (str): The user's role.
        active (bool): Whether the user is active.
        
    Returns:
        dict: A dictionary representing a user.
    """
    return {
        "id": 1,
        "name": name,
        "role": role,
        "active": active,
        "created_at": "2024-01-01T00:00:00Z"
    } 