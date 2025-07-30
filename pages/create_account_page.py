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
        self.gender_male_radio = self.frame.locator(CreateAccountPageLocators.GENDER_MALE_RADIO)
        self.first_name_input = self.frame.locator(CreateAccountPageLocators.FIRST_NAME_INPUT)
        self.last_name_input = self.frame.locator(CreateAccountPageLocators.LAST_NAME_INPUT)
        self.email_input = self.frame.locator(CreateAccountPageLocators.EMAIL_INPUT)
        self.password_input = self.frame.locator(CreateAccountPageLocators.PASSWORD_INPUT)
        self.terms_and_conditions_checkbox = self.frame.locator(CreateAccountPageLocators.TERMS_AND_CONDITIONS_CHECKBOX)
        self.customer_privacy_checkbox = self.frame.locator(CreateAccountPageLocators.CUSTOMER_PRIVACY_CHECKBOX)
        self.save_form_button = self.frame.locator(CreateAccountPageLocators.SAVE_FORM_BUTTON)
