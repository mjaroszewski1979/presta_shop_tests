# Import Playwright's 'expect' for advanced assertions and waiting conditions.
from playwright.sync_api import expect

# Import custom utility function to assert visibility and text of multiple elements.
from utils.assertions import assert_elements_visible_with_texts, assert_element_visible_with_text

# Import test data provider for create account form labels.
from data.contact_data import get_contact_label_data




def test_contact_form_is_visible_with_text(home_page, contact_page):
    """
    Validates that the 'Contact Us' form is visible and all expected labels are correctly displayed.

    Args:
        home_page: Page object representing the home page with navigation locators.
        contact_page: Page object representing the Contact page with form locators.

    Steps:
        1. Navigate to the Contact page.
        2. Retrieve expected labels and their texts from the data provider.
        3. Assert that the 'Send' button is visible.
        4. Verify that all labels are present and contain the correct text.
    """
    home_page.contact_link.click()
    locators_and_texts = get_contact_label_data(contact_page)
    expect(contact_page.send_button).to_be_visible()
    assert_elements_visible_with_texts(locators_and_texts)

def test_contact_form_is_working_with_valid_data(home_page, contact_page):
    """
    Validates that the 'Contact Us' form can be successfully submitted with valid data.

    Args:
        home_page: Page object representing the home page with navigation locators.
        contact_page: Page object representing the Contact page with form locators.

    Steps:
        1. Navigate to the Contact page.
        2. Fill in and submit the form with valid data.
        3. Assert that a success message is displayed confirming submission.
    """
    home_page.contact_link.click()
    contact_page.submit_contact_form_with_valid_data()
    assert_element_visible_with_text(contact_page.success_message_li, 'Your message has been successfully sent to our team.')

    




