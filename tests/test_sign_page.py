# Import Playwright's 'expect' for handling assertions and state validations.
from playwright.sync_api import expect

# Import a custom assertion helper to validate element visibility and its text.
from utils.assertions import assert_element_visible_with_text

# Import utility to generate a randomized email address for password reset testing.
from utils.home_page_utils import generate_unique_email

def test_sign_in_with_incorrect_credentials(home_page, sign_page):
    """
    Verifies that attempting to sign in with invalid credentials
    triggers the appropriate authentication error message.
    """
    home_page.sign_in_span.wait_for(state="visible", timeout=5000)
    home_page.sign_in_span.click()
    sign_page.email_input.wait_for(state="visible", timeout=5000)
    sign_page.email_input.fill('')
    sign_page.email_input.type('john@gmail.com', delay=100)
    sign_page.password_input.fill('')
    sign_page.password_input.type('password123', delay=100)
    sign_page.sign_in_button.click()
    assert_element_visible_with_text(sign_page.auth_alert_li, 'Authentication failed.')


def test_reset_password_success(home_page, sign_page):
    """
    Validates that submitting a valid email address on the 'Forgot your password' form
    displays a success message indicating that a reset link has been sent.
    """
    email = generate_unique_email()
    home_page.sign_in_span.wait_for(state="visible", timeout=5000)
    home_page.sign_in_span.click()
    sign_page.forgot_password_link.wait_for(state="visible", timeout=5000)
    sign_page.forgot_password_link.click()
    sign_page.email_input.wait_for(state="visible", timeout=5000)
    sign_page.email_input.fill('')
    sign_page.email_input.type(email, delay=100)
    sign_page.send_reset_link_button.click()
    assert_element_visible_with_text(sign_page.reset_password_success_para, 'If this email address has been registered in our store, you will receive a link to reset your password at')