from pages.base_page import BasePage
from locators.contact_page_locators import ContactPageLocators

# Import utility functions for generating realistic test data (e.g., user details).
from utils.home_page_utils import generate_unique_email, generate_random_message, type_text_into_input_field

class ContactPage(BasePage):
    """
    Page Object Model (POM) representation of the Contact Page.

    Inherits shared browser actions from BasePage and initializes locators
    required for interaction with the contact form and its fields.
    All interactions happen inside the iframe identified by '#framelive'.
    """
    
    def __init__(self, page):
        """
        Initialize the ContactPage with page context and locate all UI elements
        of the contact form, such as subject dropdown, email field, message box,
        file attachment, and the send button.

        Args:
            page (playwright.sync_api.Page): Playwright page object for browser interaction.
        """
        super().__init__(page)

        # Locate iframe containing the Contact Page content
        self.frame = page.frame_locator("#framelive")

        # -------------------------------
        # Contact form elements
        # -------------------------------
        self.contact_form_heading = self.frame.locator(ContactPageLocators.CONTACT_FORM_HEADING)

        # Subject dropdown and label
        self.subject_label = self.frame.locator(ContactPageLocators.SUBJECT_LABEL)
        self.subject_select = self.frame.locator(ContactPageLocators.SUBJECT_SELECT)
        self.email_label = self.frame.locator(ContactPageLocators.EMAIL_LABEL)

        # Email field and label
        self.email_input = self.frame.locator(ContactPageLocators.EMAIL_INPUT)

        # File attachment label
        self.attachment_label = self.frame.locator(ContactPageLocators.ATTACHMENT_LABEL)

        # Message textarea and label
        self.message_label = self.frame.locator(ContactPageLocators.MESSAGE_LABEL)
        self.message_textarea = self.frame.locator(ContactPageLocators.MESSAGE_TEXTAREA)

        # Send button
        self.send_button = self.frame.locator(ContactPageLocators.SEND_BUTTON)

        # Success message element
        self.success_message_li = self.frame.locator(ContactPageLocators.SUCCESS_MESSAGE_LI)

    # -------------------------------
    # Form submission methods
    # -------------------------------
    def submit_contact_form_with_valid_data(self):
        """
        Fill and submit the contact form with dynamically generated valid test data.
        Includes selecting a subject, entering a unique email address, and typing
        a randomly generated message. Finally, submits the form by clicking 'Send'.

        Returns:
            tuple: (email, message_text) used in the form submission.
        """
        email = generate_unique_email()
        message_text = generate_random_message()

        # Ensure subject dropdown is visible before selecting
        self.subject_select.wait_for(state="visible", timeout=5000)
        self.subject_select.select_option(value="1")

        # Fill email and message fields
        type_text_into_input_field(self.email_input, email)
        type_text_into_input_field(self.message_textarea, message_text)

        # Submit the form
        self.send_button.click()


