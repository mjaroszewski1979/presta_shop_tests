# Import Playwright's 'expect' for advanced assertions and waiting conditions.
from playwright.sync_api import expect

# Import custom utility function to assert visibility and text of multiple elements.
from utils.assertions import assert_elements_visible_with_texts, assert_element_visible_with_text

# Import test data provider for create account form labels.
from data.contact_data import get_contact_label_data




def test_contact_form_is_visible_with_text(home_page, contact_page):
    """
    Validates that the 'Contact Us' form is visible and all expected labels are correctly displayed.
    """
    home_page.contact_link.click()
    locators_and_texts = get_contact_label_data(contact_page)
    expect(contact_page.send_button).to_be_visible()
    assert_elements_visible_with_texts(locators_and_texts)

def test_contact_form_is_working_with_valid_data(home_page, contact_page):
    """
    Validates that the 'Contact Us' form is working with correct data supplied
    """
    home_page.contact_link.wait_for(state="visible", timeout=5000)
    home_page.contact_link.click()
    contact_page.submit_contact_form_with_valid_data()
    assert_element_visible_with_text(contact_page.success_message_li, 'Your message has been successfully sent to our team.')

    




