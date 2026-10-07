"""The main application class."""

##############################################################################
# Python imports.
from argparse import Namespace
from dataclasses import replace

##############################################################################
# Textual imports.
from textual import events
from textual.app import InvalidThemeError, ScreenStackError

##############################################################################
# Textual enhanced imports.
from textual_enhanced.app import EnhancedApp

##############################################################################
# Local imports.
from . import __version__
from .data import (
    load_configuration,
    update_configuration,
)
from .screens import Main
from .support import (
    SCHEME_THEMES,
    UNWATCH_COLOUR_SCHEME,
    WATCH_COLOUR_SCHEME,
    terminal_theme,
)


##############################################################################
class Hike(EnhancedApp[None]):
    """The main application class."""

    HELP_TITLE = f"Hike v{__version__}"
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

    def __init__(self, arguments: Namespace) -> None:
        """Initialise the application.

        Args:
            The command line arguments passed to the application.
        """
        self._arguments = arguments
        """The command line arguments passed to the application."""
        super().__init__()
        self._match_terminal(terminal_theme() or "textual-dark")
        configuration = load_configuration()
        theme = arguments.theme or configuration.theme
        if theme is not None:
            try:
                self.theme = theme
            except InvalidThemeError:
                pass
        try:
            self.update_keymap(configuration.bindings)
        except ScreenStackError:  # https://github.com/Textualize/textual/issues/5742
            pass

    def watch_theme(self) -> None:
        """Save the application's theme when it's changed."""
        with update_configuration() as config:
            config.theme = self.theme

    def _match_terminal(self, theme: str) -> None:
        """Make the `textual-auto` theme look like the given theme.

        Args:
            theme: The name of the theme that matches the terminal.
        """
        if (base := self.get_theme(theme)) is not None:
            self.register_theme(replace(base, name="textual-auto"))
            if self.theme == "textual-auto":
                self.mutate_reactive(Hike.theme)

    def on_mount(self) -> None:
        """Ask the terminal to tell us when its colour scheme changes."""
        if self._driver is not None:
            self._driver.write(WATCH_COLOUR_SCHEME)

    def on_unmount(self) -> None:
        """Stop the terminal telling us about colour scheme changes."""
        if self._driver is not None:
            self._driver.write(UNWATCH_COLOUR_SCHEME)

    async def on_event(self, event: events.Event) -> None:
        """Keep `textual-auto` in step with the terminal's colour scheme."""
        if isinstance(event, events.Key) and event.key in SCHEME_THEMES:
            self._match_terminal(SCHEME_THEMES[event.key])
            return
        await super().on_event(event)

    def get_default_screen(self) -> Main:
        """Get the default screen for the application.

        Returns:
            The main screen.
        """
        return Main(self._arguments)

    def action_help_quit(self) -> None:
        """Override Textual's default handling of ctrl+c."""
        if load_configuration().allow_traditional_quit:
            self.exit()
        else:
            super().action_help_quit()


### hike.py ends here
