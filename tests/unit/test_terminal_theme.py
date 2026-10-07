"""Tests for working out the terminal's background."""

##############################################################################
# Pytest imports.
from pytest import mark

##############################################################################
# Textual imports.
from textual._xterm_parser import XTermParser

##############################################################################
# Local imports.
from hike.support.terminal_theme import SCHEME_THEMES, is_light


##############################################################################
@mark.parametrize(
    "reply, light",
    (
        (b"\033]11;rgb:ffff/ffff/ffff\033\\", True),
        (b"\033]11;rgb:0000/0000/0000\033\\", False),
        (b"\033]11;rgb:fd/f6/e3\a", True),  # Solarized light, 8-bit, BEL.
        (b"\033]11;rgb:2828/2a2a/3636\033\\", False),  # Dracula.
        (b"\033]11;RGB:FFFF/FFFF/FFFF\033\\", True),
        (b"", None),
        (b"\033[?62;c", None),
    ),
)
def test_is_light(reply: bytes, light: bool | None) -> None:
    """The OSC 11 reply should be decoded to light or dark."""
    assert is_light(reply) is light


##############################################################################
@mark.parametrize(
    "report, theme",
    (
        ("\033[?997;1n", "textual-dark"),
        ("\033[?997;2n", "textual-light"),
    ),
)
def test_colour_scheme_report(report: str, theme: str) -> None:
    """A colour scheme report should parse as one key that maps to a theme."""
    (key,) = XTermParser().feed(report)
    assert SCHEME_THEMES[key.key] == theme  # type: ignore[attr-defined]


### test_terminal_theme.py ends here
