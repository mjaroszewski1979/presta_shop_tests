# Import Playwright assertions
from playwright.sync_api import expect

from utils.home_page_utils import generate_unique_email

def test_sign_in_with_incorrect_credentials(home_page, sign_page):
    home_page.sign_in_span.wait_for(state="visible", timeout=5000)
    home_page.sign_in_span.click()
    sign_page.email_input.wait_for(state="visible", timeout=5000)
    sign_page.email_input.fill('')
    sign_page.email_input.type('john@gmail.com', delay=100)
    sign_page.password_input.fill('')
    sign_page.password_input.type('password123', delay=100)
    sign_page.sign_in_button.click()
    sign_page.auth_alert_li.wait_for(state="visible", timeout=5000)
    expect(sign_page.auth_alert_li).to_contain_text('Authentication failed.')

def test_reset_password_success(home_page, sign_page):
    email = generate_unique_email()
    home_page.sign_in_span.wait_for(state="visible", timeout=5000)
    home_page.sign_in_span.click()
    sign_page.forgot_password_link.wait_for(state="visible", timeout=5000)
    sign_page.forgot_password_link.click()
    sign_page.email_input.wait_for(state="visible", timeout=5000)
    sign_page.email_input.fill('')
    sign_page.email_input.type(email, delay=100)
    sign_page.send_reset_link_button.click()
    sign_page.reset_password_success_para.wait_for(state="visible", timeout=5000)
    expect(sign_page.reset_password_success_para).to_contain_text('If this email address has been registered in our store, you will receive a link to reset your password at')