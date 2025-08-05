# Import Playwright's 'expect' for advanced assertions and waiting conditions.
from playwright.sync_api import expect

# Import custom utility function to assert visibility and text of multiple elements.
from utils.assertions import assert_elements_visible_with_texts, assert_element_visible_with_text

# Import test data provider for create account form labels.
from data.first_product_data import get_first_product_data





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






