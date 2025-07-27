# Import Playwright assertions
from playwright.sync_api import expect


def test_social_title_label_is_visible_with_text(home_page, sign_page, create_account_page):
    """
    Verify the visibility and label of the 'Explore back office' button.
    """
    home_page.sign_in_span.wait_for(state="visible", timeout=5000)
    home_page.sign_in_span.click()
    sign_page.create_account_link.wait_for(state="visible", timeout=5000)
    sign_page.create_account_link.click()
    create_account_page.form_labels.first.wait_for(state="visible", timeout=5000)
    expect(create_account_page.form_labels.first).to_contain_text('Social title')

def test_first_name_label_is_visible_with_text(home_page, sign_page, create_account_page):
    """
    Verify the visibility and label of the 'Explore back office' button.
    """
    home_page.sign_in_span.wait_for(state="visible", timeout=5000)
    home_page.sign_in_span.click()
    sign_page.create_account_link.wait_for(state="visible", timeout=5000)
    sign_page.create_account_link.click()
    create_account_page.form_labels.nth(1).wait_for(state="visible", timeout=5000)
    expect(create_account_page.form_labels.nth(1)).to_contain_text('First name')

def test_last_name_label_is_visible_with_text(home_page, sign_page, create_account_page):
    """
    Verify the visibility and label of the 'Explore back office' button.
    """
    home_page.sign_in_span.wait_for(state="visible", timeout=5000)
    home_page.sign_in_span.click()
    sign_page.create_account_link.wait_for(state="visible", timeout=5000)
    sign_page.create_account_link.click()
    create_account_page.form_labels.nth(2).wait_for(state="visible", timeout=5000)
    expect(create_account_page.form_labels.nth(2)).to_contain_text('Last name')
