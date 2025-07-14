from pages.base_page import BasePage
from locators.search_page_locators import SearchPageLocators

class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.total_products_para = self.frame.locator(SearchPageLocators.TOTAL_PRODUCTS_PARA)