from pages.base_page import BasePage
from locators.sign_page_locators import SignPageLocators

class SignPage(BasePage):
    """
    Page Object Model for the Sign In page.

    Encapsulates locators and actions related to the user authentication form,
    displayed within the '#framelive' iframe. Inherits base functionality 
    for navigation, interaction, and assertions from the BasePage class.
    """
    
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.sign_in_button = self.frame.locator(SignPageLocators.SIGN_IN_BUTTON)
        self.email_input = self.frame.locator(SignPageLocators.EMAIL_INPUT)
        self.password_input = self.frame.locator(SignPageLocators.PASSWORD_INPUT)
        self.auth_alert_li = self.frame.locator(SignPageLocators.AUTH_ALERT_LI)