"""The main application class."""

##############################################################################
# Textual enhanced imports.
from textual_enhanced.app import EnhancedApp

##############################################################################
# Local imports.
from . import __version__
from .screens import Main


##############################################################################
class Hike(EnhancedApp[None]):
    """The main application class."""

    HELP_TITLE = f"Hike {__version__}"
    HELP_ABOUT = """
    `Hike` is a terminal-based Markdown viewer; it was created
    by and is maintained by [Dave Pearson](https://www.davep.org/); it is
    Free Software and can be [found on
    GitHub](https://github.com/davep/hike).
    """
    HELP_LICENSE = """
    Hike - A Markdown viewer for the terminal.  \n    Copyright (C) 2025 Dave Pearson

    This program is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the Free
    Software Foundation, either version 3 of the License, or (at your option)
    any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
    more details.

    You should have received a copy of the GNU General Public License along with
    this program. If not, see <https://www.gnu.org/licenses/>.
    """

    COMMANDS = set()

    def get_default_screen(self) -> Main:
        """Get the default screen for the application.

        Returns:
            The main screen.
        """
        return Main()


### hike.py ends here
