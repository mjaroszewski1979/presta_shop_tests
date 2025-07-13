from pages.base_page import BasePage
from locators.sign_page_locators import SignPageLocators

class SignPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.sign_in_button = self.frame.locator(SignPageLocators.SIGN_IN_BUTTON)