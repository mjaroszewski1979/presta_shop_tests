# Import Playwright assertions
from playwright.sync_api import expect
from utils.assertions import assert_element_visible_with_text


def test_social_title_label_is_visible_with_text(home_page, sign_page, create_account_page):
    """
    Verify the visibility and label of the 'Explore back office' button.
    """
    home_page.sign_in_span.wait_for(state="visible", timeout=5000)
    home_page.sign_in_span.click()
    sign_page.create_account_link.wait_for(state="visible", timeout=5000)
    sign_page.create_account_link.click()
    assert_element_visible_with_text(create_account_page.form_labels.first, 'Social title')
    assert_element_visible_with_text(create_account_page.form_labels.nth(1), 'First name')
    assert_element_visible_with_text(create_account_page.form_labels.nth(2), 'Last name')
    assert_element_visible_with_text(create_account_page.form_labels.nth(3), 'Email')
    assert_element_visible_with_text(create_account_page.form_labels.nth(4), 'Password')
    assert_element_visible_with_text(create_account_page.form_labels.nth(5), 'Birthdate')


