from pages.base_page import BasePage
from locators.create_account_page_locators import CreateAccountPageLocators
from utils.home_page_utils import (
    generate_unique_email,
    generate_first_name,
    generate_last_name,
    generate_password,
)

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

    def submit_create_account_form_with_valid_data(self, user_data):
        """
        Fills out and submits the create account form using the provided user data.

        Args:
            user_data: An object containing valid user information (first name, last name, email, password).
        """
        # Wait for the gender radio button to appear and select it
        self.gender_male_radio.wait_for(state="visible", timeout=5000)
        self.gender_male_radio.check()

        # Fill out the first name input with simulated typing delay
        self.first_name_input.fill('')
        self.first_name_input.type(user_data.first_name, delay=100)

        # Fill out the last name input with simulated typing delay
        self.last_name_input.fill('')
        self.last_name_input.type(user_data.last_name, delay=100)

        # Fill out the email input with simulated typing delay
        self.email_input.fill('')
        self.email_input.type(user_data.email, delay=100)

        # Fill out the password input with simulated typing delay
        self.password_input.fill('')
        self.password_input.type(user_data.password, delay=100)

        # Check the required checkboxes for terms acceptance and privacy
        self.terms_and_conditions_checkbox.check()
        self.customer_privacy_checkbox.check()

        # Click the button to submit the form
        self.save_form_button.click()
