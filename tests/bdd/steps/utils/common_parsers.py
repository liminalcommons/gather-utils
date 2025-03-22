"""
Common parsers for step definitions.

This module centralizes the parser imports needed across step definition files,
helping to avoid import issues when steps are consolidated.
"""

# Import the parse module from behave
try:
    import parse
    from behave import register_type

    # Create a parsers object with a parse method for compatibility
    class Parsers:
        @staticmethod
        def parse(pattern):
            """Wrapper for parse to maintain compatibility with pytest-bdd."""

            def decorator(func):
                # This is the behave way of using parse
                from behave import step

                return step(pattern)(func)

            return decorator

    parsers = Parsers()
except ImportError:
    try:
        # Try pytest-bdd's parsers as a fallback
        from pytest_bdd import parsers
    except ImportError:
        # If neither is available, create a minimal implementation
        class DummyParser:
            @staticmethod
            def parse(pattern):
                """Dummy implementation for parse, returns the pattern unchanged."""

                def decorator(func):
                    return func

                return decorator

        parsers = DummyParser()

# Export the parsers to be used in step definitions
__all__ = ["parsers"]
