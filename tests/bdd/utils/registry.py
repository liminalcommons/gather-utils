"""
Registry for BDD step definitions.

This module provides a registry for tracking step definitions to help prevent
duplicate step definitions and make it easier to manage steps across
multiple files.
"""

class StepRegistry:
    """Registry for tracking BDD step definitions."""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StepRegistry, cls).__new__(cls)
            cls._instance._steps = {}
        return cls._instance
    
    def register_step(self, step_type, pattern, function):
        """Register a step definition.
        
        Args:
            step_type (str): The step type (given, when, then)
            pattern (str): The step pattern (e.g., "I have {x}")
            function (callable): The step function
            
        Returns:
            callable: The registered function
        """
        key = f"{step_type}:{pattern}"
        self._steps[key] = function
        return function
    
    def is_registered(self, step_type, pattern):
        """Check if a step is already registered.
        
        Args:
            step_type (str): The step type (given, when, then)
            pattern (str): The step pattern
            
        Returns:
            bool: True if the step is registered, False otherwise
        """
        key = f"{step_type}:{pattern}"
        return key in self._steps
    
    def get_step(self, step_type, pattern):
        """Get a registered step function.
        
        Args:
            step_type (str): The step type (given, when, then)
            pattern (str): The step pattern
            
        Returns:
            callable: The step function, or None if not registered
        """
        key = f"{step_type}:{pattern}"
        return self._steps.get(key)
    
    def clear(self):
        """Clear all registered steps."""
        self._steps = {}

# Create a singleton registry
registry = StepRegistry()

# Decorator functions for registering steps
def given_step(pattern):
    """Decorator for registering 'given' steps."""
    def decorator(func):
        return registry.register_step("given", pattern, func)
    return decorator

def when_step(pattern):
    """Decorator for registering 'when' steps."""
    def decorator(func):
        return registry.register_step("when", pattern, func)
    return decorator

def then_step(pattern):
    """Decorator for registering 'then' steps."""
    def decorator(func):
        return registry.register_step("then", pattern, func)
    return decorator 