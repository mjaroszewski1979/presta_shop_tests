from pages.base_page import BasePage
from locators.art_page_locators import ArtPageLocators

class ArtPage(BasePage):
    """
    Page Object Model for the Art category page.

    Provides access to UI elements and interactions specific to the Art category.
    The page content is rendered within an iframe identified by '#framelive'.
    Inherits common functionality from BasePage.
    """
    
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.art_div_header = self.frame.locator(ArtPageLocators.ART_DIV_HEADER)