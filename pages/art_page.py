from pages.base_page import BasePage
from locators.art_page_locators import ArtPageLocators

class ArtPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.art_div_header = self.frame.locator(ArtPageLocators.ART_DIV_HEADER)