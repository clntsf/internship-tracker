from abc import ABC, abstractmethod
from .data_types import Listing

class ScrapeStrategy(ABC):
    """
    ABC for definable scraping strategies in our program to provide a common interface
    (see GoF Strategy Pattern) for scraping internship data from various job boards.

    one abstract method `scrape_internships` is defined here for getting a list of Listing
    objects from a job listing. this methods takes no parameters, as subclasses are expected to
    be instantiated with all data required for this operation.

    The intention of this class is to allow myself and others to flexibly add listing sources
    and strategies for scraping them without modifying any other code.

    Interface Signature
    ```
    # load the job source, scrape listings and parse each into a Listing object
    def scrape_internships(self) -> list[Listing]: ...
    ```
    """

    @abstractmethod
    def scrape_internships(self) -> list[Listing]: ...