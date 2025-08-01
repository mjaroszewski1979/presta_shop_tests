from pages.base_page import BasePage
from locators.contact_page_locators import ContactPageLocators

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
        self.email_label = self.frame.locator(ContactPageLocators.EMAIL_LABEL)
        self.attachment_label = self.frame.locator(ContactPageLocators.ATTACHMENT_LABEL)
        self.message_label = self.frame.locator(ContactPageLocators.MESSAGE_LABEL)
        self.send_button = self.frame.locator(ContactPageLocators.SEND_BUTTON)