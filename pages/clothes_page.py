from pages.base_page import BasePage
from locators.clothes_page_locators import ClothesPageLocators

class ClothesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.clothes_div_header = self.frame.locator(ClothesPageLocators.CLOTHES_DIV_HEADER)