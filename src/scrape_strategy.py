from abc import ABC, abstractmethod
from .data_types import Listing
from typing import Iterable

class ScrapeStrategy(ABC):
    """
    ABC for definable scraping strategies in our program to provide a common interface
    (see GoF Strategy Pattern) for scraping internship data from various job boards.

    Abstract methods here are defined for:
    - scraping the webpage (desired arguments/path parameters can be added as properties
    to subclasses and used in this method) and returning a list of parseable html listing elements
    - parsing an individual element into a Listing dataclass for use elsewhere

    The intention of this class is to allow myself and others to flexibly add listing sources and
    strategies for scraping them without modifying any other code.
    """

    @abstractmethod
    def get_listings_html(self) -> list[str]: ...

    @abstractmethod
    def parse_listing(self, listing_html: str) -> Listing: ...

    def scrape_internships(self) -> Iterable[Listing]:
        listings = self.get_listings_html()
        return map(self.parse_listing, listings)