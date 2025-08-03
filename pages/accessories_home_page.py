from pages.base_page import BasePage
from locators.accessories_home_page_locators import AccessoriesHomePageLocators

class AccessoriesHomePage(BasePage):
    """
    Page Object Model for the Accessories Homecategory page.

    Encapsulates the locators and interactions for the Accessories page,
    which is embedded inside an iframe identified by '#framelive'.
    Inherits common page functionality from BasePage.
    """

    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive") # Locate the iframe containing the Accessories page content
        self.product_list_para = self.frame.locator(AccessoriesHomePageLocators.PRODUCT_LIST_PARA)
        self.ceramic_checkbox = self.frame.locator(AccessoriesHomePageLocators.CERAMIC_CHECKBOX)