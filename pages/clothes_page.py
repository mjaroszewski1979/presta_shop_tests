from pages.base_page import BasePage
from locators.clothes_page_locators import ClothesPageLocators

class ClothesPage(BasePage):
    """
    Page Object Model for the Clothes category page.

    Provides access to elements and interactions specific to the Clothes category,
    which is rendered inside the '#framelive' iframe. Inherits base functionality
    such as navigation, assertions, and utility methods from BasePage.
    """
    
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.clothes_div_header = self.frame.locator(ClothesPageLocators.CLOTHES_DIV_HEADER)