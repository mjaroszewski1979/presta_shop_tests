# Import Playwright's 'expect' for advanced assertions and waiting conditions.
from playwright.sync_api import expect

# Import custom utility function to assert visibility and text of multiple elements.
from utils.assertions import assert_elements_visible_with_texts, assert_element_visible_with_text

# Import test data provider for create account form labels.
from data.first_product_data import get_first_product_data, get_first_product_composition_data





def test_first_product_section_is_visible_with_text(home_page, first_product_page):
    """
    Validates that the 'Create Account' form is visible and all expected labels are correctly displayed.
    """
    home_page.first_product_link.first.wait_for(state="visible", timeout=10000)
    home_page.first_product_link.first.click()
    locators_and_texts = get_first_product_data(first_product_page)
    assert_elements_visible_with_texts(locators_and_texts)

def test_first_product_color_variant_change_is_working(home_page, first_product_page):
    """
    Validates that the 'Create Account' form is visible and all expected labels are correctly displayed.
    """
    home_page.first_product_link.first.wait_for(state="visible", timeout=10000)
    home_page.first_product_link.first.click()
    first_product_page.color_black_input.wait_for(state="visible", timeout=10000)
    first_product_page.color_black_input.check()
    assert_element_visible_with_text(first_product_page.color_variant_span.nth(1), 'Color: Black')

def test_first_product_size_option_change_is_working(home_page, first_product_page):
    """
    Validates that the 'Create Account' form is visible and all expected labels are correctly displayed.
    """
    home_page.first_product_link.first.wait_for(state="visible", timeout=10000)
    home_page.first_product_link.first.click()
    size_option = "M"
    first_product_page.select_size_option(size_option)
    assert_element_visible_with_text(first_product_page.size_span.first, "Size: " + size_option)

def test_first_product_details_section_is_visible_with_text(home_page, first_product_page):
    """
    Validates that the 'Create Account' form is visible and all expected labels are correctly displayed.
    """
    home_page.first_product_link.first.wait_for(state="visible", timeout=10000)
    home_page.first_product_link.first.click()
    first_product_page.product_details_link.wait_for(state="visible", timeout=10000)
    first_product_page.product_details_link.click()
    locators_and_texts = get_first_product_composition_data(first_product_page)
    assert_elements_visible_with_texts(locators_and_texts)

def test_first_product_quick_view_link_is_working(home_page, first_product_page):
    """
    Validates that the 'Create Account' form is visible and all expected labels are correctly displayed.
    """
    home_page.first_product_link.first.wait_for(state="visible", timeout=10000)
    home_page.first_product_link.first.hover()
    first_product_page.quick_view_link.first.wait_for(state="visible", timeout=10000)
    first_product_page.quick_view_link.first.click()
    assert_element_visible_with_text(first_product_page.modal_body_h1, 'Hummingbird printed t-shirt')

def test_first_product_adding_to_cart_is_working(home_page, first_product_page):
    """
    Validates that the 'Create Account' form is visible and all expected labels are correctly displayed.
    """
    home_page.first_product_link.first.wait_for(state="visible", timeout=10000)
    home_page.first_product_link.first.click()
    first_product_page.add_to_cart_button.wait_for(state="visible", timeout=10000)
    first_product_page.add_to_cart_button.click()
    assert_element_visible_with_text(first_product_page.cart_success_message, 'Product successfully added to your shopping cart')






