from pages.base_page import BasePage
from locators.create_account_page_locators import CreateAccountPageLocators

class CreateAccountPage(BasePage):
    """
    Page Object Model for the Create Account page.

    Encapsulates locators and actions related to the user authentication form,
    displayed within the '#framelive' iframe. Inherits base functionality 
    for navigation, interaction, and assertions from the BasePage class.
    """
    
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.form_labels = self.frame.locator(CreateAccountPageLocators.FORM_LABELS)
        self.custom_checkbox_labels = self.frame.locator(CreateAccountPageLocators.CUSTOM_CHECKBOX_LABELS)
