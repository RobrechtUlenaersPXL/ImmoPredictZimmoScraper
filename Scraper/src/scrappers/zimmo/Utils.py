
from typing import Callable
from dataclasses import dataclass


@dataclass
class Scrap:
    """Store a scrap method and its value."""

    function: Callable
    tag: str = None
    clasz: str = None
    title: str = None
    regex: str = None


@dataclass
class ScrapMoreInfo(Scrap):
    """Scrap method that retrieve data from the "More Info" tab of the page."""

    tag: str = 'div'
    clasz: str = 'col-xs-7 info-name'


@dataclass
class ScrapSurface(ScrapMoreInfo):
    """Scrap method that retrieve data with the same regex."""

    regex: str = r"(?P<number>\d*) m²"
