"""Provides the history for the navigation panel."""

##############################################################################
# Python imports.
from pathlib import Path
from typing import cast

##############################################################################
# Textual imports.
from textual import on, work
from textual.content import Content
from textual.widgets.option_list import Option

##############################################################################
# Textual-enhanced imports.
from textual_enhanced.binding import HelpfulBinding
from textual_enhanced.dialogs import Confirm
from textual_enhanced.widgets import EnhancedOptionList

##############################################################################
# Local imports.
from ...icons import LOCAL_FILE_ICON, REMOTE_FILE_ICON
from ...messages import (
    ClearHistory,
    DeduplicateHistory,
    OpenFromHistory,
    RemoveHistoryEntry,
)
from ...types import HikeHistory, HikeLocation


##############################################################################
class Location(Option):
    """A location within the history."""

    def __init__(self, location_id: int, location: HikeLocation) -> None:
        """Initialise the location object.

        Args:
            location_id: The ID of the location within the history.
            location: The location.
        """
        self.location_id = location_id
        """The ID of the location within the history."""
        super().__init__(
            Content.from_markup(
                f"{LOCAL_FILE_ICON} [bold]{location.name}[/]\n[dim]{location.parent}[/]"
                if isinstance(location, Path)
                else f"{REMOTE_FILE_ICON} [bold]{Path(location.path).name}[/]"
                f"\n[dim]{Path(location.path).parent}\n{location.host}[/]"
            ),
            id=str(location_id),
        )


##############################################################################
class HistoryView(EnhancedOptionList):
    """The display of history."""

    DEFAULT_CSS = """
    HistoryView {
        height: 1fr;
        border: none;
        text-wrap: nowrap;
        text-overflow: ellipsis;
        &:focus {
            border: none;
        }
    }
    """

    HELP = """
    ## Document viewing history

    This is your document viewing history. Here you can revisit locations
    you've viewed, and also remove individual or all locations.
    """

    BINDINGS = [
        HelpfulBinding(
            "delete",
            "remove",
            "Remove",
            show=False,
            tooltip="Remove the highlighted location from history",
        ),
        HelpfulBinding(
            "backspace",
            "clear",
            "Clear",
            show=False,
            tooltip="Clear all locations from history",
        ),
        HelpfulBinding(
            "d",
            "deduplicate",
            "Deduplicate",
            show=False,
            tooltip="Deduplicate the history",
        ),
    ]

    def update(self, history: HikeHistory) -> None:
        """Update the content of the history view.

        Args:
            history: The history to update with.
        """
        self.clear_options().add_options(
            Location(location_id, location)
            for location_id, location in reversed(list(enumerate(history)))
        )
        # If history has been updated, that implies something new has been
        # added to the start; so in that case we jump the highlight to the
        # top.
        if self.option_count:
            with self.prevent(EnhancedOptionList.OptionHighlighted):
                self.highlighted = 0

    @on(EnhancedOptionList.OptionHighlighted)
    def visit_from_history(self, message: EnhancedOptionList.OptionHighlighted) -> None:
        """Visit a location from history.

        Args:
            message: The message to say which option was selected.
        """
        message.stop()
        assert isinstance(message.option, Location)
        self.post_message(OpenFromHistory(message.option.location_id))

    def highlight_location(self, location: int) -> None:
        """Highlight an item in the history.

        Args:
            location: The ID of the location to highlight.
        """
        self.highlighted = self.get_option_index(str(location))

    def check_action(self, action: str, parameters: tuple[object, ...]) -> bool | None:
        """Check if an action is possible to perform right now.

        Args:
            action: The action to perform.
            parameters: The parameters of the action.

        Returns:
            `True` if it can perform, `False` or `None` if not.
        """
        if action == "remove":
            return bool(self.option_count) and self.highlighted is not None
        if action in ("clear", "deduplicate"):
            return bool(self.option_count)
        return True

    @work
    async def action_remove(self) -> None:
        """Remove an item of history."""
        if not self.check_action("remove", ()):
            return
        if await self.app.push_screen_wait(
            Confirm(
                "Remove?", "Are you sure you want to remove this location from history?"
            )
        ):
            assert self.highlighted is not None
            location = cast(Location, self.get_option_at_index(self.highlighted))
            self.post_message(RemoveHistoryEntry(location.location_id))

    @work
    async def action_clear(self) -> None:
        """Clear all items from history."""
        if not self.check_action("clear", ()):
            return
        if await self.app.push_screen_wait(
            Confirm(
                "Clear?", "Are you sure you want to clear all locations from history?"
            )
        ):
            self.post_message(ClearHistory())

    @work
    async def action_deduplicate(self) -> None:
        """Deduplicate history."""
        if not self.check_action("deduplicate", ()):
            return
        if await self.app.push_screen_wait(
            Confirm("Deduplicate?", "Are you sure you want to deduplicate the history?")
        ):
            self.post_message(DeduplicateHistory())


### history.py ends here
