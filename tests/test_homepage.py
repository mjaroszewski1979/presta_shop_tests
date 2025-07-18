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

def test_sign_in_link_is_working(home_page, sign_page):
    home_page.sign_in_span.wait_for(state="visible", timeout=10000)
    home_page.sign_in_span.click()
    sign_page.sign_in_button.wait_for(state="visible", timeout=10000)
    expect(sign_page.sign_in_button).to_have_text("Sign in")

def test_cart_span_is_visible_with_text(home_page):
    home_page.cart_span.wait_for(state="visible", timeout=10000)
    expect(home_page.cart_span).to_have_text("Cart")

def test_my_store_img_is_visible(home_page):
    home_page.my_store_img.wait_for(state="visible", timeout=10000)
    expect(home_page.my_store_img).to_be_visible()

def test_clothes_link_is_visible_with_text(home_page):
    home_page.clothes_link.wait_for(state="visible", timeout=10000)
    expect(home_page.clothes_link).to_contain_text("Clothes")

def test_clothes_link_is_working(home_page, clothes_page):
    home_page.clothes_link.wait_for(state="visible", timeout=10000)
    home_page.clothes_link.click()
    expect(clothes_page.clothes_div_header).to_contain_text("Clothes")

def test_clothes_men_link_is_visible_with_text(home_page):
    home_page.clothes_link.wait_for(state="visible", timeout=10000)
    home_page.clothes_link.hover()
    home_page.clothes_men_link.wait_for(state="visible", timeout=10000)
    expect(home_page.clothes_men_link).to_contain_text("Men")

def test_clothes_women_link_is_visible_with_text(home_page):
    home_page.clothes_link.wait_for(state="visible", timeout=10000)
    home_page.clothes_link.hover()
    home_page.clothes_women_link.wait_for(state="visible", timeout=10000)
    expect(home_page.clothes_women_link).to_contain_text("Women")

def test_accessories_link_is_visible_with_text(home_page):
    home_page.accessories_link.wait_for(state="visible", timeout=10000)
    expect(home_page.accessories_link).to_contain_text("Accessories")

def test_accessories_link_is_working(home_page, accessories_page):
    home_page.accessories_link.wait_for(state="visible", timeout=10000)
    home_page.accessories_link.click()
    expect(accessories_page.accessories_div_header).to_contain_text("Accessories")

def test_accessories_stationery_link_is_visible_with_text(home_page):
    home_page.accessories_link.wait_for(state="visible", timeout=10000)
    home_page.accessories_link.hover()
    home_page.accessories_stationery_link.wait_for(state="visible", timeout=10000)
    expect(home_page.accessories_stationery_link).to_contain_text("Stationery")

def test_accessories_home_link_is_visible_with_text(home_page):
    home_page.accessories_link.wait_for(state="visible", timeout=10000)
    home_page.accessories_link.hover()
    home_page.accessories_home_link.wait_for(state="visible", timeout=10000)
    expect(home_page.accessories_home_link).to_contain_text("Home Accessories")

def test_art_link_is_visible_with_text(home_page):
    home_page.art_link.wait_for(state="visible", timeout=10000)
    expect(home_page.art_link).to_contain_text("Art")

def test_art_link_is_working(home_page, art_page):
    home_page.art_link.wait_for(state="visible", timeout=10000)
    home_page.art_link.click()
    expect(art_page.art_div_header).to_contain_text("Art")

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

def test_search_catalog_input(home_page, search_page):
    home_page.search_catalog_input.wait_for(state="visible", timeout=5000)
    home_page.search_catalog_input.fill('')
    home_page.search_catalog_input.type('Hummingbird', delay=100)
    home_page.search_catalog_input.click()
    home_page.search_catalog_input.press("Enter")
    search_page.total_products_para.wait_for(state="visible", timeout=5000)
    expect(search_page.total_products_para).to_contain_text('There are 5 products.')

def test_language_select(home_page):
    home_page.language_dropdown_button.wait_for(state="visible", timeout=5000)
    home_page.language_dropdown_button.click()
    home_page.language_option_spanish.wait_for(state="visible", timeout=5000)
    home_page.language_option_spanish.click()
    home_page.featured_products_h2.first.wait_for(state="visible", timeout=5000)
    expect(home_page.featured_products_h2.first).to_contain_text('Productos Destacados')

def test_device_width_desktop(home_page):
    home_page.device_li.first.wait_for(state="visible", timeout=5000)
    home_page.device_li.first.click()
    home_page.body_index.wait_for(state="visible", timeout=5000)
    expect(home_page.body_index).to_have_css("width", "1280px")

def test_device_width_tablet_h(home_page):
    home_page.device_li.nth(1).wait_for(state="visible", timeout=5000)
    home_page.device_li.nth(1).click()
    home_page.body_index.wait_for(state="visible", timeout=5000)
    expect(home_page.body_index).to_have_css("width", "1024px")

def test_device_width_tablet_v(home_page):
    home_page.device_li.nth(2).wait_for(state="visible", timeout=5000)
    home_page.device_li.nth(2).click()
    home_page.body_index.wait_for(state="visible", timeout=5000)
    expect(home_page.body_index).to_have_css("width", "768px")

def test_device_width_mobile(home_page):
    home_page.device_li.nth(3).wait_for(state="visible", timeout=5000)
    home_page.device_li.nth(3).click()
    home_page.body_index.wait_for(state="visible", timeout=5000)
    expect(home_page.body_index).to_have_css("width", "375px")

def test_start_now_button_is_visible_with_text(home_page):
    home_page.start_now_button.wait_for(state="visible", timeout=10000)
    expect(home_page.start_now_button).to_contain_text("Start now")

def test_explore_bo_button_is_visible_with_text(home_page):
    home_page.explore_bo_button.wait_for(state="visible", timeout=10000)
    expect(home_page.explore_bo_button).to_contain_text("Explore back office")

def test_hide_header_span(home_page):
    expect(home_page.header_div).to_be_visible(timeout=5000)
    home_page.hide_header_span.click()
    expect(home_page.header_div).not_to_be_visible()

def test_banner_image_is_visible(home_page):
    home_page.banner_image.wait_for(state="visible", timeout=10000)
    expect(home_page.banner_image).to_be_visible()

def test_subscribe_with_valid_email_works(home_page):
    home_page.subscribe_input.wait_for(state="visible", timeout=10000)
    home_page.subscribe_input.fill('')
    home_page.subscribe_input.type('mj@gmail.com', delay=100)
    home_page.subscribe_button.click()
    home_page.subscribe_info_para.wait_for(state="visible", timeout=10000)
    expect(home_page.subscribe_info_para).to_contain_text("You have successfully subscribed to this newsletter.")


def assert_footer_section(home_page, section_index, expected_title, expected_items, submenu_locator):
    expect(home_page.footer_section_title.nth(section_index)).to_be_visible()
    expect(home_page.footer_section_title.nth(section_index)).to_have_text(expected_title)
    actual_items = home_page.get_footer_submenu_texts(submenu_locator)
    assert actual_items == expected_items, f"Expected {expected_items}, but got {actual_items}"

def test_footer_products_section(home_page):
    assert_footer_section(
        home_page,
        section_index=0,
        expected_title="Products",
        expected_items=["Prices drop", "New products", "Best sellers"],
        submenu_locator=home_page.footer_products_submenu_items
    )

def test_footer_our_company_section(home_page):
    assert_footer_section(
        home_page,
        section_index=1,
        expected_title="Our company",
        expected_items=[
            "Delivery", "Legal Notice", "Terms and conditions of use", "About us",
            "Secure payment", "Contact us", "Sitemap", "Stores"
        ],
        submenu_locator=home_page.footer_our_company_submenu_items
    )

def test_footer_your_account_section(home_page):
    assert_footer_section(
        home_page,
        section_index=2,
        expected_title="Your account",
        expected_items=["Order tracking", "Sign in", "Create account", "My alerts"],
        submenu_locator=home_page.footer_your_account_submenu_items
    )

def test_footer_store_info_section(home_page):
    expect(home_page.footer_section_title.nth(3)).to_be_visible()
    expect(home_page.footer_section_title.nth(3)).to_have_text("Store information")

    expected_text = "PrestaShop\nFrance\nEmail us: demo@prestashop.com"
    actual_text = home_page.get_footer_store_info_text()
    assert actual_text == expected_text, f"Expected {expected_text}, but got {actual_text}"













