from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators

class CartPage(BasePage):
    """
    Page Object Model for the Search results page.

    Provides access to search result-specific elements and interactions.
    The content is rendered inside the '#framelive' iframe.
    Inherits common utility methods and assertions from BasePage.
    """
    
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.remove_from_cart_link = self.frame.locator(CartPageLocators.REMOVE_FROM_CART_LINK)
        self.items_info_span = self.frame.locator(CartPageLocators.ITEMS_INFO_SPAN)