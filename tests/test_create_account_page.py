# Import Playwright assertions
from playwright.sync_api import expect
from utils.assertions import assert_elements_visible_with_texts
from data.create_account_data import get_create_account_label_data


def test_create_account_form_is_visible_with_text(home_page, sign_page, create_account_page):
    """
    Verify the visibility and label of the 'Create Account' form.
    """
    home_page.sign_in_span.wait_for(state="visible", timeout=5000)
    home_page.sign_in_span.click()
    sign_page.create_account_link.wait_for(state="visible", timeout=5000)
    sign_page.create_account_link.click()
    locators_and_texts = get_create_account_label_data(create_account_page)
    assert_elements_visible_with_texts(locators_and_texts)


