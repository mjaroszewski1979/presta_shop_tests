from pages.base_page import BasePage
from locators.first_product_page_locators import FirstProductPageLocators

class FirstProductPage(BasePage):
    """
    Page Object Model for the First Product page.

    Provides access to UI elements and interactions specific to the First Product.
    The page content is rendered within an iframe identified by '#framelive'.
    Inherits common functionality from BasePage.
    """
    
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.content_div_header = self.frame.locator(FirstProductPageLocators.CONTENT_DIV_HEADER)