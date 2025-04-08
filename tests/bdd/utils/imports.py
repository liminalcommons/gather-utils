"""
Common imports for BDD step definitions.

This module provides centralized imports for BDD step definitions to ensure
consistent import patterns and avoid circular dependencies.
"""

import os
import sys
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# BDD framework imports
from behave import given, then, when
from pytest_bdd import parsers

# Application imports
from gather_manager.api import GatherAPI
from gather_manager.models import Portal, PortalConnection

# Export commonly used modules and functions
__all__ = [
    # Python standard library
    'os', 'sys', 'json', 'tempfile', 'unittest', 'Path', 
    'MagicMock', 'patch',
    
    # BDD framework
    'given', 'then', 'when', 'parsers',
    
    # Application
    'GatherAPI', 'Portal', 'PortalConnection',
] 