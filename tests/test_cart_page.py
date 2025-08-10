# Import Playwright's 'expect' for advanced assertions and waiting conditions.
from playwright.sync_api import expect

# Import custom utility function to assert visibility and text of multiple elements.
from utils.assertions import assert_element_visible_with_text, assert_elements_visible_with_texts

from data.cart_data import get_sign_in_form_data





def test_removing_product_from_cart_is_working(home_page, first_product_page, cart_page):
    """
    UI Test: Verify that removing a product from the cart works as expected.

    Steps:
        1. Wait for the first product link on the home page to become visible and click it.
        2. Wait for the "Add to cart" button on the product page to be visible and click it.
        3. Wait for the "Continue shopping" button to appear and click it to return to the home page.
        4. Click on the cart icon to view the cart contents.
        5. Wait for the "Remove from cart" link to be visible and click it.
        6. Verify that the cart is empty by asserting the visibility of the confirmation message.

    Args:
        home_page: Page Object for the home page.
        first_product_page: Page Object for the first product details page.
        cart_page: Page Object for the cart page.
    """
    home_page.first_product_link.first.wait_for(state="visible", timeout=10000)
    home_page.first_product_link.first.click()
    first_product_page.add_to_cart_button.wait_for(state="visible", timeout=10000)
    first_product_page.add_to_cart_button.click()
    first_product_page.continue_shopping_button.wait_for(state="visible", timeout=10000)
    first_product_page.continue_shopping_button.click()
    home_page.cart_span.click()
    cart_page.remove_from_cart_link.wait_for(state="visible", timeout=10000)
    cart_page.remove_from_cart_link.click()
    assert_element_visible_with_text(cart_page.items_info_span, 'There are no more items in your cart')

def test_proceed_to_checkout_link_is_working(home_page, first_product_page, cart_page):
    """
    UI Test: Verify that removing a product from the cart works as expected.

    Steps:
        1. Wait for the first product link on the home page to become visible and click it.
        2. Wait for the "Add to cart" button on the product page to be visible and click it.
        3. Wait for the "Continue shopping" button to appear and click it to return to the home page.
        4. Click on the cart icon to view the cart contents.
        5. Wait for the "Remove from cart" link to be visible and click it.
        6. Verify that the cart is empty by asserting the visibility of the confirmation message.

    Args:
        home_page: Page Object for the home page.
        first_product_page: Page Object for the first product details page.
        cart_page: Page Object for the cart page.
    """
    home_page.first_product_link.first.wait_for(state="visible", timeout=10000)
    home_page.first_product_link.first.click()
    first_product_page.add_to_cart_button.wait_for(state="visible", timeout=10000)
    first_product_page.add_to_cart_button.click()
    first_product_page.checkout_link.wait_for(state="visible", timeout=10000)
    first_product_page.checkout_link.click()
    cart_page.proceed_to_checkout_link.wait_for(state="visible", timeout=10000)
    cart_page.proceed_to_checkout_link.click()
    assert_element_visible_with_text(cart_page.personal_info_header, 'Personal Information')

def test_checkout_with_sign_in_option_is_working(home_page, first_product_page, cart_page):
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
    first_product_page.add_to_cart_button.wait_for(state="visible", timeout=10000)
    first_product_page.add_to_cart_button.click()
    first_product_page.checkout_link.wait_for(state="visible", timeout=10000)
    first_product_page.checkout_link.click()
    cart_page.proceed_to_checkout_link.wait_for(state="visible", timeout=10000)
    cart_page.proceed_to_checkout_link.click()
    cart_page.sign_in_link.wait_for(state="visible", timeout=10000)
    cart_page.sign_in_link.click()
    locators_and_texts = get_sign_in_form_data(cart_page)
    assert_elements_visible_with_texts(locators_and_texts)



    




