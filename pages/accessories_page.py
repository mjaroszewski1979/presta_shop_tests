from pages.base_page import BasePage
from locators.accessories_page_locators import AccessoriesPageLocators

class AccessoriesPage(BasePage):
    """
    Page Object Model for the Accessories category page.

    Encapsulates the locators and interactions for the Accessories page,
    which is embedded inside an iframe identified by '#framelive'.
    Inherits common page functionality from BasePage.
    """

    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive") # Locate the iframe containing the Accessories page content
        self.accessories_div_header = self.frame.locator(AccessoriesPageLocators.ACCESSORIES_DIV_HEADER)