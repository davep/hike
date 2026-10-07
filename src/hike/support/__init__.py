"""Support code and classes."""

##############################################################################
# Local imports.
from .mouse import is_copy_request_click
from .terminal_theme import (
    SCHEME_THEMES,
    UNWATCH_COLOUR_SCHEME,
    WATCH_COLOUR_SCHEME,
    terminal_theme,
)
from .view_in_browser import view_in_browser

##############################################################################
# Exports.
__all__ = [
    "is_copy_request_click",
    "SCHEME_THEMES",
    "terminal_theme",
    "UNWATCH_COLOUR_SCHEME",
    "view_in_browser",
    "WATCH_COLOUR_SCHEME",
]

### __init__.py ends here
