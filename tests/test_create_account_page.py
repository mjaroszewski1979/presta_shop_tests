# Import Playwright's 'expect' for advanced assertions and waiting conditions.
from playwright.sync_api import expect

# Import custom utility function to assert visibility and text of multiple elements.
from utils.assertions import assert_elements_visible_with_texts

# Import test data provider for create account form labels.
from data.create_account_data import get_create_account_label_data

# Import user data model for generating valid user credentials.
from models.user_data import UserData



def test_create_account_form_is_visible_with_text(home_page, sign_page, create_account_page):
    """
    UI Test: Verify that the 'Create Account' form is visible and contains all expected labels.

    Steps:
        1. Wait for the 'Sign in' link on the home page to be visible and click it.
        2. Wait for the 'Create account' link on the sign-in page to be visible and click it.
        3. Retrieve all expected form label locators and their corresponding text values.
        4. Assert that all form labels are visible and match the expected text.

    Args:
        home_page: Page Object for the home page.
        sign_page: Page Object for the sign-in page.
        create_account_page: Page Object for the create account page.
    """
    home_page.sign_in_span.wait_for(state="visible", timeout=5000)
    home_page.sign_in_span.click()
    sign_page.create_account_link.wait_for(state="visible", timeout=5000)
    sign_page.create_account_link.click()
    locators_and_texts = get_create_account_label_data(create_account_page)
    assert_elements_visible_with_texts(locators_and_texts)

def test_create_account_form_is_working_with_valid_data(home_page, sign_page, create_account_page):
    """
    UI Test: Verify that a new account can be successfully created using valid user data.

    Steps:
        1. Generate a valid user data object with first name, last name, email, and password.
        2. Wait for the 'Sign in' link on the home page to be visible and click it.
        3. Wait for the 'Create account' link on the sign-in page to be visible and click it.
        4. Fill in the create account form with the generated valid user data and submit it.
        5. Assert that the 'Sign out' link is visible, confirming the account was created successfully.

    Args:
        home_page: Page Object for the home page.
        sign_page: Page Object for the sign-in page.
        create_account_page: Page Object for the create account page.
    """
    user = UserData.generate_valid()
    home_page.sign_in_span.wait_for(state="visible", timeout=5000)
    home_page.sign_in_span.click()
    sign_page.create_account_link.wait_for(state="visible", timeout=5000)
    sign_page.create_account_link.click()
    create_account_page.submit_create_account_form_with_valid_data(user)
    expect(home_page.sign_out_link).to_be_visible()



