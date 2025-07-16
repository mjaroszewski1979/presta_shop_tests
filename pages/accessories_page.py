from pages.base_page import BasePage
from locators.accessories_page_locators import AccessoriesPageLocators

class AccessoriesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.accessories_div_header = self.frame.locator(AccessoriesPageLocators.ACCESSORIES_DIV_HEADER)