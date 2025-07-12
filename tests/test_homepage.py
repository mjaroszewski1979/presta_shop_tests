from playwright.sync_api import expect

def test_homepage_title(home_page):
    home_page.assert_title_is("PrestaShop Live Demo")

def test_homepage_url(home_page):
    home_page.assert_url_is("https://demo.prestashop.com/#/en/front")

def test_contact_link_is_visible_with_text(home_page):
    home_page.contact_link.wait_for(state="visible", timeout=10000)
    expect(home_page.contact_link).to_have_text("Contact us")

def test_contact_link_is_working(home_page, contact_page):
    home_page.contact_link.wait_for(state="visible", timeout=10000)
    home_page.contact_link.click()
    contact_page.contact_form_heading.wait_for(state="visible", timeout=10000)
    expect(contact_page.contact_form_heading).to_have_text("Contact us")

def test_sign_in_span_is_visible_with_text(home_page):
    home_page.sign_in_span.wait_for(state="visible", timeout=10000)
    expect(home_page.sign_in_span).to_have_text("Sign in")

def test_cart_span_is_visible_with_text(home_page):
    home_page.cart_span.wait_for(state="visible", timeout=10000)
    expect(home_page.cart_span).to_have_text("Cart")

def test_homepage_displays_8_featured_products(home_page):
    home_page.featured_products.first.wait_for(state="visible", timeout=10000)
    expect(home_page.featured_products).to_have_count(8)

def test_homepage_displays_2_sale_products(home_page):
    home_page.sale_products.first.scroll_into_view_if_needed()
    home_page.sale_products.first.wait_for(state="visible", timeout=10000)
    expect(home_page.sale_products).to_have_count(2)

def test_carousel_initial_slide_text(home_page):
    first_heading = home_page.carousel_headings.nth(0)
    first_heading.wait_for(state="visible", timeout=5000)
    expect(first_heading).to_have_text("Sample 1")

def test_carousel_second_slide_text(home_page):
    home_page.carousel_next_icon.click()
    second_heading = home_page.carousel_headings.nth(1)
    second_heading.wait_for(state="visible", timeout=5000)
    expect(second_heading).to_have_text("Sample 2")




