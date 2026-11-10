"""Tests for the location type testing code."""

##############################################################################
# Python imports.
from pathlib import Path

##############################################################################
# httpx imports.
from httpx import URL

##############################################################################
# Pytest imports.
from pytest import mark

##############################################################################
# Local imports.
from hike.data import looks_urllike, maybe_markdown
from hike.types import HikeLocation


##############################################################################
@mark.parametrize(
    "to_test, expected",
    (
        (Path("test.md"), True),
        (Path("test.markdown"), True),
        (Path("test.txt"), False),
        (URL("http://example.com/test.md"), True),
        (URL("http://example.com/test.markdown"), True),
        (URL("http://example.com/test.txt"), False),
        (URL("https://example.com/test.md"), True),
        (URL("https://example.com/test.markdown"), True),
        (URL("https://example.com/test.txt"), False),
    ),
)
def test_maybe_markdown(to_test: HikeLocation, expected: bool) -> None:
    """We should be able to make a good guess at what's a Markdown location."""
    assert maybe_markdown(to_test) is expected


##############################################################################
@mark.parametrize(
    "to_test, expected",
    (
        ("http://example.com/", True),
        ("https://example.com/", True),
        ("http://example", True),
        ("https://example", True),
        ("example.com/", False),
        ("example.com/", False),
        ("", False),
        ("http", False),
        ("https", False),
        ("http://", False),
        ("https://", False),
        ("  http://example.com/  ", True),
        ("  https://example.com/test.md  ", True),
        ("\thttps://example.com/\n", True),
        ("   ", False),
    ),
)
def test_looks_urllike(to_test: str, expected: bool) -> None:
    """We should be able to make a good guess at what's a URL."""
    assert looks_urllike(to_test) is expected


### test_location_types.py ends here
