from pages.base_page import BasePage
from locators.contact_page_locators import ContactPageLocators
from utils.home_page_utils import generate_unique_email, generate_random_message

class ContactPage(BasePage):
    """
    Page Object Model for the Contact page.

    Encapsulates interactions and locators specific to the Contact page,
    which is loaded within an iframe identified by '#framelive'.
    Inherits core functionality from BasePage to enable reuse of common actions and assertions.
    """
    
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.contact_form_heading = self.frame.locator(ContactPageLocators.CONTACT_FORM_HEADING)
        self.subject_label = self.frame.locator(ContactPageLocators.SUBJECT_LABEL)
        self.subject_select = self.frame.locator(ContactPageLocators.SUBJECT_SELECT)
        self.email_label = self.frame.locator(ContactPageLocators.EMAIL_LABEL)
        self.email_input = self.frame.locator(ContactPageLocators.EMAIL_INPUT)
        self.attachment_label = self.frame.locator(ContactPageLocators.ATTACHMENT_LABEL)
        self.message_label = self.frame.locator(ContactPageLocators.MESSAGE_LABEL)
        self.message_textarea = self.frame.locator(ContactPageLocators.MESSAGE_TEXTAREA)
        self.send_button = self.frame.locator(ContactPageLocators.SEND_BUTTON)
        self.success_message_li = self.frame.locator(ContactPageLocators.SUCCESS_MESSAGE_LI)

    def submit_contact_form_with_valid_data(self):
        email = generate_unique_email()
        message_text = generate_random_message()
        self.subject_select.wait_for(state="visible", timeout=5000)
        self.subject_select.select_option(value="1")
        self.email_input.fill('')
        self.email_input.type(email, delay=100)
        self.message_textarea.fill('')
        self.message_textarea.type(message_text, delay=100)
        self.send_button.click()


