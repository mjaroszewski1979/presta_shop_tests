# Import Playwright's 'expect' for advanced assertions and waiting conditions.
from playwright.sync_api import expect

# Import custom utility function to assert visibility and text of multiple elements.
from utils.assertions import assert_elements_visible_with_texts

# Import test data provider for create account form labels.
from data.create_account_data import get_create_account_label_data

from models.user_data import UserData



def test_create_account_form_is_visible_with_text(home_page, sign_page, create_account_page):
    """
    Validates that the 'Create Account' form is visible and all expected labels are correctly displayed.
    """
    home_page.sign_in_span.wait_for(state="visible", timeout=5000)
    home_page.sign_in_span.click()
    sign_page.create_account_link.wait_for(state="visible", timeout=5000)
    sign_page.create_account_link.click()
    locators_and_texts = get_create_account_label_data(create_account_page)
    assert_elements_visible_with_texts(locators_and_texts)

def test_create_account_form_is_working_with_valid_data(home_page, sign_page, create_account_page):
    """
    Validates that the 'Create Account' form is visible and all expected labels are correctly displayed.
    """
    user = UserData.generate_valid()
    home_page.sign_in_span.wait_for(state="visible", timeout=5000)
    home_page.sign_in_span.click()
    sign_page.create_account_link.wait_for(state="visible", timeout=5000)
    sign_page.create_account_link.click()
    create_account_page.submit_create_account_form_with_valid_data(user)
    expect(home_page.sign_out_link).to_be_visible()



