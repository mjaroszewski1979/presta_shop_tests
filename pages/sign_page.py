from pages.base_page import BasePage
from locators.sign_page_locators import SignPageLocators

class SignPage(BasePage):
    """
    Page Object Model (POM) representation of the Sign In page.

    Encapsulates locators and actions related to the user authentication form.
    The main content is rendered inside the '#framelive' iframe.
    Inherits navigation, interaction, and assertion functionality from BasePage.
    """
    
    def __init__(self, page):
        """
        Initialize the SignPage with page context and locate all relevant 
        UI elements for the sign-in process.

        Args:
            page (playwright.sync_api.Page): Playwright page object for browser interaction.
        """
        super().__init__(page)

        # -------------------------------
        # Authentication form elements
        # -------------------------------
        self.sign_in_button = self.frame.locator(SignPageLocators.SIGN_IN_BUTTON)
        self.email_input = self.frame.locator(SignPageLocators.EMAIL_INPUT)
        self.auth_alert_li = self.frame.locator(SignPageLocators.AUTH_ALERT_LI)

        # -------------------------------
        # Password reset functionality
        # -------------------------------
        self.forgot_password_link = self.frame.locator(SignPageLocators.FORGOT_PASSWORD_LINK)
        self.send_reset_link_button = self.frame.locator(SignPageLocators.SEND_RESET_LINK_BUTTON)
        self.reset_password_success_para = self.frame.locator(SignPageLocators.RESET_PASSWORD_SUCCESS_PARA)

        # -------------------------------
        # Account creation navigation
        # -------------------------------
        self.create_account_link = self.frame.locator(SignPageLocators.CREATE_ACCOUNT_LINK)