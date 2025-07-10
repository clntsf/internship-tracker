from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from abc import abstractmethod

from ..scrape_strategy import ScrapeStrategy
from ..data_types import Listing

class XPathScraper(ScrapeStrategy):
    """
    Intermediate ABC specialized in scraping child elements 
    """
    driver: webdriver.Chrome
    url: str
    xpath: str
    field_xpaths: dict[str, str]

    def __init__(self, driver: webdriver.Chrome, url: str, xpath: str, field_xpaths: dict[str, str]):
        self.driver = driver
        self.url = url
        self.xpath = xpath

    def scrape_internships(self) -> list[Listing]:
        self.driver.get(self.url)
        listings_html = self.driver.find_elements(By.XPATH, self.xpath)
        return list(map(self.parse_listing, listings_html))
    
    @abstractmethod
    def parse_listing(self, listing_html: WebElement) -> Listing: