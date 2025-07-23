# Import Playwright assertions
from playwright.sync_api import expect

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