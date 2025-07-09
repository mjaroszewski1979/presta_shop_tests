from playwright.sync_api import expect

def test_homepage_title(home_page):
    home_page.assert_title_is("PrestaShop Live Demo")

def test_homepage_url(home_page):
    home_page.assert_url_is("https://demo.prestashop.com/#/en/front")

def test_contact_link_is_visible_with_text(home_page):
    home_page.contact_link.wait_for(state="visible", timeout=10000)
    expect(home_page.contact_link).to_have_text("Contact us")

def test_sign_in_span_is_visible_with_text(home_page):
    home_page.sign_in_span.wait_for(state="visible", timeout=10000)
    expect(home_page.sign_in_span).to_have_text("Sign in")

def test_cart_span_is_visible_with_text(home_page):
    home_page.cart_span.wait_for(state="visible", timeout=10000)
    expect(home_page.cart_span).to_have_text("Cart")
