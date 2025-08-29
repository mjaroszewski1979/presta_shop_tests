from pages.base_page import BasePage
from locators.create_account_page_locators import CreateAccountPageLocators
# Import utility functions for generating realistic test data (e.g., user details).
from utils.home_page_utils import type_text_into_input_field

class CreateAccountPage(BasePage):
    """
    Page Object Model (POM) representation of the Create Account Page.

    Inherits shared functionality from BasePage for browser interaction
    and initializes locators related to the account creation form 
    displayed within the '#framelive' iframe.
    """
    
    def __init__(self, page):
        """
        Initialize the CreateAccountPage with page context and locate all UI 
        elements of the registration form, including input fields, checkboxes, 
        radio buttons, and form submission controls.

        Args:
            page (playwright.sync_api.Page): Playwright page object for browser interaction.
        """
        super().__init__(page)

        # -------------------------------
        # Form labels
        # -------------------------------
        self.form_labels = self.frame.locator(CreateAccountPageLocators.FORM_LABELS)
        self.custom_checkbox_labels = self.frame.locator(CreateAccountPageLocators.CUSTOM_CHECKBOX_LABELS)

        # -------------------------------
        # Radio buttons (gender selection)
        # -------------------------------
        self.gender_male_radio = self.frame.locator(CreateAccountPageLocators.GENDER_MALE_RADIO)

        # -------------------------------
        # Input fields
        # -------------------------------
        self.first_name_input = self.frame.locator(CreateAccountPageLocators.FIRST_NAME_INPUT)
        self.last_name_input = self.frame.locator(CreateAccountPageLocators.LAST_NAME_INPUT)
        self.email_input = self.frame.locator(CreateAccountPageLocators.EMAIL_INPUT)
        self.password_input = self.frame.locator(CreateAccountPageLocators.PASSWORD_INPUT)

        # -------------------------------
        # Checkboxes
        # -------------------------------
        self.terms_and_conditions_checkbox = self.frame.locator(CreateAccountPageLocators.TERMS_AND_CONDITIONS_CHECKBOX)
        self.customer_privacy_checkbox = self.frame.locator(CreateAccountPageLocators.CUSTOMER_PRIVACY_CHECKBOX)

        # -------------------------------
        # Form submission
        # -------------------------------
        self.save_form_button = self.frame.locator(CreateAccountPageLocators.SAVE_FORM_BUTTON)

    # -------------------------------
    # Form submission methods
    # -------------------------------
    def submit_create_account_form_with_valid_data(self, user_data):
        """
        Fill and submit the account creation form using the provided valid user data.
        Includes gender selection, user details, acceptance of required terms,
        and form submission.

        Args:
            user_data (UserData): Object containing valid user information
                                  (first name, last name, email, password).
        """
        # Ensure gender selection is available before checking
        self.gender_male_radio.wait_for(state="visible", timeout=5000)
        self.gender_male_radio.check()

        # Fill input fields with provided user data     
        type_text_into_input_field(self.first_name_input, user_data.first_name)
        type_text_into_input_field(self.last_name_input, user_data.last_name)
        type_text_into_input_field(self.email_input, user_data.email)
        type_text_into_input_field(self.password_input, user_data.password)

        # Check mandatory agreement checkboxes
        self.terms_and_conditions_checkbox.check()
        self.customer_privacy_checkbox.check()

        # Submit the form
        self.save_form_button.click()
