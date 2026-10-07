"""Work out if the terminal has a light or a dark background."""

##############################################################################
# Python imports.
import os
import re
from enum import Enum
from select import select

##############################################################################
# Textual imports.
from textual._ansi_sequences import ANSI_SEQUENCES_KEYS

##############################################################################
# The OSC 11 query asks the terminal for its background colour.
_QUERY = b"\033]11;?\033\\"
_REPLY = re.compile(rb"rgb:([0-9a-f]+)/([0-9a-f]+)/([0-9a-f]+)", re.IGNORECASE)

##############################################################################
# DEC mode 2031 asks the terminal to report when its colour scheme changes.
WATCH_COLOUR_SCHEME = "\033[?2031h"
UNWATCH_COLOUR_SCHEME = "\033[?2031l"


##############################################################################
class _ColourScheme(Enum):
    """Key names for the terminal's colour scheme reports."""

    DARK = "terminal_colour_scheme_dark"
    LIGHT = "terminal_colour_scheme_light"


SCHEME_THEMES = {
    _ColourScheme.DARK.value: "textual-dark",
    _ColourScheme.LIGHT.value: "textual-light",
}
"""Map the colour scheme report keys to the theme to use."""

# Teach Textual's input parser the reports, so that they arrive as keys we
# can act on rather than as stray characters.
ANSI_SEQUENCES_KEYS["\033[?997;1n"] = (_ColourScheme.DARK,)  # type: ignore[index]
ANSI_SEQUENCES_KEYS["\033[?997;2n"] = (_ColourScheme.LIGHT,)  # type: ignore[index]


##############################################################################
def is_light(reply: bytes) -> bool | None:
    """Decide if an OSC 11 reply describes a light background.

    Args:
        reply: The raw reply from the terminal.

    Returns:
        `True` if light, `False` if dark, `None` if the reply can't be parsed.
    """
    if (match := _REPLY.search(reply)) is None:
        return None
    red, green, blue = (
        int(channel, 16) / (16 ** len(channel) - 1) for channel in match.groups()
    )
    return (0.2126 * red + 0.7152 * green + 0.0722 * blue) > 0.5


##############################################################################
def terminal_theme(timeout: float = 0.1) -> str | None:
    """Pick a Textual theme that matches the terminal's background.

    Args:
        timeout: How long to wait for the terminal to reply.

    Returns:
        `textual-light` or `textual-dark`, or `None` if the terminal didn't say.

    Notes:
        This has to be called before Textual takes over the terminal.
    """
    try:
        import termios
        import tty
    except ImportError:  # Windows.
        return None
    try:
        terminal = os.open("/dev/tty", os.O_RDWR | os.O_NOCTTY)
    except OSError:
        return None
    reply = b""
    try:
        settings = termios.tcgetattr(terminal)
        try:
            tty.setraw(terminal)
            os.write(terminal, _QUERY)
            while select([terminal], [], [], timeout)[0]:
                reply += os.read(terminal, 64)
                if reply.endswith((b"\033\\", b"\a")):
                    break
        finally:
            termios.tcsetattr(terminal, termios.TCSADRAIN, settings)
    except termios.error:
        return None
    finally:
        os.close(terminal)
    if (light := is_light(reply)) is None:
        return None
    return "textual-light" if light else "textual-dark"


### terminal_theme.py ends here
