"""Provides the command for opening from a URL."""

##############################################################################
# httpx imports.
from httpx import URL

##############################################################################
# Textual imports.
from textual.widget import Widget

##############################################################################
# Local imports.
from ...data import looks_urllike
from ...messages import OpenLocation
from .base_command import InputCommand


##############################################################################
class OpenURLCommand(InputCommand):
    """View the file at `<url>`"""

    COMMAND = "`<url>`"

    @classmethod
    def handle(cls, text: str, for_widget: Widget) -> bool:
        """Handle the command.

        Args:
            text: The text of the command.
            for_widget: The widget to handle the command for.

        Returns:
            `True` if the command was handled; `False` if not.
        """
        if looks_urllike(text):
            for_widget.post_message(OpenLocation(URL(text.strip())))
            return True
        return False


### open_url.py ends here
