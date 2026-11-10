"""Functions for testing location types."""

##############################################################################
# Python imports.
from functools import singledispatch
from pathlib import Path

##############################################################################
# httpx imports.
from httpx import URL, AsyncClient, HTTPStatusError, RequestError

##############################################################################
from typing_extensions import TypeIs

##############################################################################
# Local imports.
from .. import USER_AGENT
from ..types import HikeLocation
from .config import load_configuration


##############################################################################
@singledispatch
def maybe_markdown(location: object) -> bool:
    """Does the given location look like it might be a Markdown file?

    Args:
        location: The location to test.

    Returns:
        `True` if the location looks like it's Markdown, `False` if not.
    """
    return False


##############################################################################
@maybe_markdown.register
def _(location: Path) -> bool:
    return location.suffix.lower() in load_configuration().markdown_extensions


##############################################################################
@maybe_markdown.register
def _(location: str) -> bool:
    return maybe_markdown(Path(location))


##############################################################################
@maybe_markdown.register
def _(location: URL) -> bool:
    return maybe_markdown(location.path)


##############################################################################
async def can_be_negotiated_to_markdown(location: HikeLocation) -> bool:
    """Can the given location be negotiated to Markdown?

    Args:
        location: The location to test.

    Returns:
        `True` if the location can be negotiated to Markdown, `False` if
        not.
    """
    if isinstance(location, Path):
        return False
    async with AsyncClient() as client:
        try:
            response = await client.head(
                location,
                follow_redirects=True,
                headers={
                    "user-agent": USER_AGENT,
                    "Accept": ",".join(
                        load_configuration().markdown_content_types + ["*/*;q=0.1"]
                    ),
                },
            )
        except RequestError:
            return False
    try:
        response.raise_for_status()
    except HTTPStatusError:
        return False
    if content_type := response.headers.get("content-type"):
        return any(
            content_type.startswith(accepted_type)
            for accepted_type in load_configuration().markdown_content_types
        )
    return False


##############################################################################
def looks_urllike(candidate: str) -> bool:
    """Does the given value look like a URL?

    Args:
        candidate: The candidate to test.

    Returns:
        `True` if the string looks like a URL, `False` if not.
    """
    url = URL(candidate.strip())
    return url.is_absolute_url and url.scheme in ("http", "https")


##############################################################################
def is_editable(location: HikeLocation) -> TypeIs[Path]:
    """Is the given location one that can be edited?

    Args:
        location: The location to test.

    Returns:
        `True` if the location can be edited, `False` if not.
    """
    return isinstance(location, Path)


### location_types.py ends here
