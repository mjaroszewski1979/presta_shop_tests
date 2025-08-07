# Import Playwright's 'expect' for advanced assertions and waiting conditions.
from playwright.sync_api import expect

# Import custom utility function to assert visibility and text of multiple elements.
from utils.assertions import assert_element_visible_with_text





def test_removing_product_from_cart_is_working(home_page, first_product_page, cart_page):
    """
    Validates that the 'Create Account' form is visible and all expected labels are correctly displayed.
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



    




