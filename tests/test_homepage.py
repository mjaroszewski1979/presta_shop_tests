# Import Playwright assertions
from playwright.sync_api import expect

# Import test data and helper function
from data.home_page_data import FOOTER_SECTIONS
from utils.home_page_utils import generate_unique_email

def test_homepage_title(home_page):
    """
    Verify that the homepage title is correct.
    """
    home_page.assert_title_is("PrestaShop Live Demo")

def test_homepage_url(home_page):
    """
    Verify that the homepage URL is correct.
    """
    home_page.assert_url_is("https://demo.prestashop.com/#/en/front")

def test_contact_link_is_visible_with_text(home_page):
    """
    Ensure the 'Contact us' link is visible and contains the correct text.
    """
    expect(home_page.contact_link).to_have_text("Contact us")

def test_contact_link_is_working(home_page, contact_page):
    """
    Verify that clicking the 'Contact us' link navigates to the contact page.
    """
    home_page.contact_link.click()
    expect(contact_page.contact_form_heading).to_have_text("Contact us")

def test_sign_in_span_is_visible_with_text(home_page):
    """
    Verify that the 'Sign in' span is visible with correct label.
    """
    expect(home_page.sign_in_span).to_have_text("Sign in")

def test_sign_in_link_is_working(home_page, sign_page):
    """
    Ensure the 'Sign in' link navigates to the login page.
    """
    home_page.sign_in_span.click()
    expect(sign_page.sign_in_button).to_have_text("Sign in")

def test_cart_span_is_visible_with_text(home_page):
    """
    Verify that the cart span is visible and labeled correctly.
    """
    expect(home_page.cart_span).to_have_text("Cart")

def test_my_store_img_is_visible(home_page):
    """
    Confirm that the store logo image is displayed on the homepage.
    """
    expect(home_page.my_store_img).to_be_visible()

def test_clothes_link_is_visible_with_text(home_page):
    """
    Check that the 'Clothes' category link is visible and labeled correctly.
    """
    expect(home_page.clothes_link).to_contain_text("Clothes")

def test_clothes_link_is_working(home_page, clothes_page):
    """
    Verify that clicking the 'Clothes' link navigates to the correct page.
    """
    home_page.clothes_link.click()
    expect(clothes_page.clothes_div_header).to_contain_text("Clothes")

def test_clothes_men_link_is_visible_with_text(home_page):
    """
    Verify that the 'Men' subcategory under 'Clothes' is visible and labeled correctly.
    """
    home_page.clothes_link.hover()
    #home_page.clothes_men_link.wait_for(state="visible", timeout=10000)
    expect(home_page.clothes_men_link).to_contain_text("Men")

def test_clothes_women_link_is_visible_with_text(home_page):
    """
    Verify that the 'Women' subcategory under 'Clothes' is visible and labeled correctly.
    """
    home_page.clothes_link.hover()
    #home_page.clothes_women_link.wait_for(state="visible", timeout=10000)
    expect(home_page.clothes_women_link).to_contain_text("Women")

def test_accessories_link_is_visible_with_text(home_page):
    """
    Ensure 'Accessories' category is displayed and correctly labeled.
    """
    expect(home_page.accessories_link).to_contain_text("Accessories")

def test_accessories_link_is_working(home_page, accessories_page):
    """
    Check that the 'Accessories' link navigates to the appropriate category page.
    """
    home_page.accessories_link.click()
    expect(accessories_page.accessories_div_header).to_contain_text("Accessories")

def test_accessories_stationery_link_is_visible_with_text(home_page):
    """
    Verify that 'Stationery' submenu under Accessories is visible.
    """
    home_page.accessories_link.hover()
    #home_page.accessories_stationery_link.wait_for(state="visible", timeout=10000)
    expect(home_page.accessories_stationery_link).to_contain_text("Stationery")

def test_accessories_home_link_is_visible_with_text(home_page):
    """
    Verify that 'Home Accessories' submenu under Accessories is visible.
    """
    home_page.accessories_link.hover()
    #home_page.accessories_home_link.wait_for(state="visible", timeout=10000)
    expect(home_page.accessories_home_link).to_contain_text("Home Accessories")

def test_art_link_is_visible_with_text(home_page):
    """
    Ensure 'Art' category link is visible.
    """
    expect(home_page.art_link).to_contain_text("Art")

def test_art_link_is_working(home_page, art_page):
    """
    Verify that clicking the 'Art' link loads the correct content.
    """
    home_page.art_link.click()
    expect(art_page.art_div_header).to_contain_text("Art")

def test_first_product_link_is_working(home_page, first_product_page):
    """
    Verify that clicking the 'First Product' link loads the correct content.
    """
    home_page.first_product_link.first.click()
    expect(first_product_page.content_div_header).to_contain_text("Hummingbird printed t-shirt")

def test_homepage_displays_8_featured_products(home_page):
    """
    Ensure exactly 8 featured products are displayed on the homepage.
    """
    expect(home_page.featured_products).to_have_count(8)

def test_homepage_displays_2_sale_products(home_page):
    """
    Ensure exactly 2 sale products are displayed on the homepage.
    """
    home_page.sale_products.first.scroll_into_view_if_needed()
    expect(home_page.sale_products).to_have_count(2)

def test_carousel_initial_slide_text(home_page):
    """
    Validate the text of the first carousel slide.
    """
    first_heading = home_page.carousel_headings.nth(0)
    expect(first_heading).to_have_text("Sample 1")

def test_carousel_second_slide_text(home_page):
    """
    Validate the text of the second carousel slide after navigation.
    """
    home_page.carousel_next_icon.click()
    second_heading = home_page.carousel_headings.nth(1)
    expect(second_heading).to_have_text("Sample 2")

def test_search_catalog_input(home_page, search_page):
    """
    Test the search functionality with the keyword 'Hummingbird'.
    """
    home_page.search_catalog_input.wait_for(state="visible", timeout=5000)
    home_page.search_catalog_input.fill('')
    home_page.search_catalog_input.type('Hummingbird', delay=100)
    home_page.search_catalog_input.click()
    home_page.search_catalog_input.press("Enter")
    search_page.total_products_para.wait_for(state="visible", timeout=5000)
    expect(search_page.total_products_para).to_contain_text('There are 5 products.')

def test_language_select(home_page):
    """
    Verify that switching language to Spanish updates the UI correctly.
    """
    home_page.language_dropdown_button.click()
    home_page.language_option_spanish.click()
    expect(home_page.featured_products_h2.first).to_contain_text('Productos Destacados')

def test_device_width_desktop(home_page):
    """
    Validate desktop view width.
    """
    home_page.device_li.first.click()
    expect(home_page.body_index).to_have_css("width", "1280px")

def test_device_width_tablet_h(home_page):
    """
    Validate horizontal tablet view width.
    """
    home_page.device_li.nth(1).click()
    expect(home_page.body_index).to_have_css("width", "1024px")

def test_device_width_tablet_v(home_page):
    """
    Validate vertical tablet view width.
    """
    home_page.device_li.nth(2).click()
    expect(home_page.body_index).to_have_css("width", "768px")

def test_device_width_mobile(home_page):
    """
    Validate mobile view width.
    """
    home_page.device_li.nth(3).click()
    expect(home_page.body_index).to_have_css("width", "375px")

def test_start_now_button_is_visible_with_text(home_page):
    """
    Verify the visibility and label of the 'Start now' button.
    """
    expect(home_page.start_now_button).to_contain_text("Start now")

def test_explore_bo_button_is_visible_with_text(home_page):
    """
    Verify the visibility and label of the 'Explore back office' button.
    """
    expect(home_page.explore_bo_button).to_contain_text("Explore back office")

def test_hide_header_span(home_page):
    """
    Confirm that clicking 'hide header' hides the header section.
    """
    expect(home_page.header_div).to_be_visible(timeout=5000)
    home_page.hide_header_span.click()
    expect(home_page.header_div).not_to_be_visible()

def test_banner_image_is_visible(home_page):
    """
    Confirm that the main banner image is visible.
    """
    expect(home_page.banner_image).to_be_visible()

def test_subscribe_with_valid_email_works(home_page):
    """
    Test newsletter subscription flow with a generated valid email.
    """
    email = generate_unique_email()
    home_page.subscribe_input.wait_for(state="visible", timeout=10000)
    home_page.subscribe_input.fill('')
    home_page.subscribe_input.type(email, delay=100)
    home_page.subscribe_button.click()
    home_page.subscribe_info_para.wait_for(state="visible", timeout=10000)
    expect(home_page.subscribe_info_para).to_contain_text("You have successfully subscribed to this newsletter.")


def assert_footer_section(home_page, section_index, expected_title, expected_items, submenu_locator):
    """
    Utility function to validate footer section title and submenu items.
    """
    section_title = home_page.footer_section_title.nth(section_index)
    expect(section_title).to_be_visible()
    expect(section_title).to_have_text(expected_title)
    if isinstance(expected_items, list):
        actual_items = submenu_locator.all_inner_texts()
        assert actual_items == expected_items, f"Expected {expected_items}, but got {actual_items}"
    else:
        actual_item = submenu_locator.inner_text()
        assert actual_item == expected_items, f"Expected {expected_items}, but got {actual_item}"


def test_footer_products_section(home_page):
    """
    Validate the 'Products' section in the page footer.
    """
    section = FOOTER_SECTIONS["products"]
    assert_footer_section(
        home_page,
        section_index=section["index"],
        expected_title=section["title"],
        expected_items=section["items"],
        submenu_locator=home_page.footer_products_submenu_items
    )


def test_footer_our_company_section(home_page):
    """
    Validate the 'Our Company' section in the page footer.
    """
    section = FOOTER_SECTIONS["our_company"]
    assert_footer_section(
        home_page,
        section_index=section["index"],
        expected_title=section["title"],
        expected_items=section["items"],
        submenu_locator=home_page.footer_our_company_submenu_items
    )


def test_footer_your_account_section(home_page):
    """
    Validate the 'Your Account' section in the page footer.
    """
    section = FOOTER_SECTIONS["your_account"]
    assert_footer_section(
        home_page,
        section_index=section["index"],
        expected_title=section["title"],
        expected_items=section["items"],
        submenu_locator=home_page.footer_your_account_submenu_items
    )


def test_footer_store_info_section(home_page):
    """
    Validate the 'Store Information' section in the page footer.
    """
    section = FOOTER_SECTIONS["store_info"]
    assert_footer_section(
        home_page,
        section_index=section["index"],
        expected_title=section["title"],
        expected_items=section["items"],
        submenu_locator=home_page.footer_store_info_submenu_items
    )













