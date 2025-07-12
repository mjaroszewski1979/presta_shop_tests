from pages.base_page import BasePage
from locators.contact_page_locators import ContactPageLocators

class ContactPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.contact_form_heading = self.frame.locator(ContactPageLocators.CONTACT_FORM_HEADING)