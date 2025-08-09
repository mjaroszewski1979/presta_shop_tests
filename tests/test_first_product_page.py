# Import Playwright's 'expect' for advanced assertions and waiting conditions.
from playwright.sync_api import expect

# Import custom utility function to assert visibility and text of multiple elements.
from utils.assertions import assert_elements_visible_with_texts, assert_element_visible_with_text

# Import test data provider for create account form labels.
from data.first_product_data import get_first_product_data, get_first_product_composition_data





def test_first_product_section_is_visible_with_text(home_page, first_product_page):
    """
    UI Test: Verify that the first product page section is visible and displays all expected elements with correct text.

    Steps:
        1. Wait for the first product link on the home page to be visible and click it.
        2. Retrieve expected locators and text values for the first product section.
        3. Assert that all retrieved elements are visible and contain the expected text.

    Args:
        home_page: Page Object for the home page.
        first_product_page: Page Object for the first product's details page.
    """
    home_page.first_product_link.first.wait_for(state="visible", timeout=10000)
    home_page.first_product_link.first.click()
    locators_and_texts = get_first_product_data(first_product_page)
    assert_elements_visible_with_texts(locators_and_texts)

def test_first_product_color_variant_change_is_working(home_page, first_product_page):
    """
    UI Test: Verify that changing the color variant of the first product updates the displayed selection.

    Steps:
        1. Wait for the first product link on the home page to be visible and click it.
        2. Wait for the black color variant option to be visible and select it.
        3. Assert that the selected color is displayed as 'Color: Black'.

    Args:
        home_page: Page Object for the home page.
        first_product_page: Page Object for the first product's details page.
    """
    home_page.first_product_link.first.wait_for(state="visible", timeout=10000)
    home_page.first_product_link.first.click()
    first_product_page.color_black_input.wait_for(state="visible", timeout=10000)
    first_product_page.color_black_input.check()
    assert_element_visible_with_text(first_product_page.color_variant_span.nth(1), 'Color: Black')

def test_first_product_size_option_change_is_working(home_page, first_product_page):
    """
    UI Test: Verify that changing the size option of the first product updates the displayed selection.

    Steps:
        1. Wait for the first product link on the home page to be visible and click it.
        2. Select the size option "M".
        3. Assert that the selected size is displayed as 'Size: M'.

    Args:
        home_page: Page Object for the home page.
        first_product_page: Page Object for the first product's details page.
    """
    home_page.first_product_link.first.wait_for(state="visible", timeout=10000)
    home_page.first_product_link.first.click()
    size_option = "M"
    first_product_page.select_size_option(size_option)
    assert_element_visible_with_text(first_product_page.size_span.first, "Size: " + size_option)

def test_first_product_details_section_is_visible_with_text(home_page, first_product_page):
    """
    UI Test: Verify that the product details section is accessible and displays the expected composition information.

    Steps:
        1. Wait for the first product link on the home page to be visible and click it.
        2. Wait for the 'Product details' link to be visible and click it.
        3. Retrieve expected locators and text values for the composition section.
        4. Assert that all retrieved elements are visible and contain the expected text.

    Args:
        home_page: Page Object for the home page.
        first_product_page: Page Object for the first product's details page.
    """
    home_page.first_product_link.first.wait_for(state="visible", timeout=10000)
    home_page.first_product_link.first.click()
    first_product_page.product_details_link.wait_for(state="visible", timeout=10000)
    first_product_page.product_details_link.click()
    locators_and_texts = get_first_product_composition_data(first_product_page)
    assert_elements_visible_with_texts(locators_and_texts)

def test_first_product_quick_view_link_is_working(home_page, first_product_page):
    """
    UI Test: Verify that the 'Quick View' feature for the first product opens the correct product modal.

    Steps:
        1. Wait for the first product link on the home page to be visible and hover over it.
        2. Wait for the 'Quick View' link to be visible and click it.
        3. Assert that the modal displays the correct product title.

    Args:
        home_page: Page Object for the home page.
        first_product_page: Page Object for the first product's details page.
    """
    home_page.first_product_link.first.wait_for(state="visible", timeout=10000)
    home_page.first_product_link.first.hover()
    first_product_page.quick_view_link.first.wait_for(state="visible", timeout=10000)
    first_product_page.quick_view_link.first.click()
    assert_element_visible_with_text(first_product_page.modal_body_h1, 'Hummingbird printed t-shirt')

def test_first_product_adding_to_cart_is_working(home_page, first_product_page):
    """
    UI Test: Verify that the first product can be successfully added to the shopping cart.

    Steps:
        1. Wait for the first product link on the home page to be visible and click it.
        2. Wait for the 'Add to cart' button to be visible and click it.
        3. Assert that a success message is displayed confirming the product was added.

    Args:
        home_page: Page Object for the home page.
        first_product_page: Page Object for the first product's details page.
    """
    home_page.first_product_link.first.wait_for(state="visible", timeout=10000)
    home_page.first_product_link.first.click()
    first_product_page.add_to_cart_button.wait_for(state="visible", timeout=10000)
    first_product_page.add_to_cart_button.click()
    assert_element_visible_with_text(first_product_page.cart_success_message, 'Product successfully added to your shopping cart')







