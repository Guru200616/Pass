"""
Password Generator Package

Provides:
- Core password generation logic
- Tkinter-based GUI application
"""

from .logic import generate_password
from .gui import run_app

__all__ = ["generate_password", "run_app"]
