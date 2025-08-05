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
        self.current_price_span = self.frame.locator(FirstProductPageLocators.CURRENT_PRICE_SPAN)
        self.description_short_para = self.frame.locator(FirstProductPageLocators.DESCRIPTION_SHORT_PARA)
        self.size_span = self.frame.locator(FirstProductPageLocators.SIZE_SPAN)
        self.size_select = self.frame.locator(FirstProductPageLocators.SIZE_SELECT)
        self.color_variant_span = self.frame.locator(FirstProductPageLocators.COLOR_VARIANT_SPAN)
        self.color_black_input = self.frame.locator(FirstProductPageLocators.COLOR_BLACK_INPUT)
        self.quantity_label = self.frame.locator(FirstProductPageLocators.QUANTITY_LABEL)
        self.social_sharing_span = self.frame.locator(FirstProductPageLocators.SOCIAL_SHARING_SPAN)
        self.reassurance_div = self.frame.locator(FirstProductPageLocators.REASSURANCE_DIV)
        self.description_long_para = self.frame.locator(FirstProductPageLocators.DESCRIPTION_LONG_PARA)
        self.product_details_link = self.frame.locator(FirstProductPageLocators.PRODUCT_DETAILS_LINK)
        self.composition_name = self.frame.locator(FirstProductPageLocators.COMPOSITION_NAME)
        self.composition_value = self.frame.locator(FirstProductPageLocators.COMPOSITION_VALUE)
        self.add_to_cart_button = self.frame.locator(FirstProductPageLocators.ADD_TO_CART_BUTTON)

    def select_size_option(self, size):
        self.size_select.wait_for(state="visible", timeout=5000)
        self.size_select.select_option(size)