from dataclasses import dataclass

@dataclass
class Listing:
    listing_name: str
    listing_location: str
    listing_description: str
    posting_company: str
    board_link: str