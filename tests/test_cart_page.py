# Import Playwright's 'expect' for advanced assertions and waiting conditions.
from playwright.sync_api import expect

# Import custom utility function to assert visibility and text of multiple elements.
from utils.assertions import assert_element_visible_with_text, assert_elements_visible_with_texts

from data.cart_data import get_sign_in_form_data, get_personal_info_form_data, get_address_form_data, get_delivery_form_data, get_payment_form_data


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
    cart_page.first_product_add_to_cart(home_page, first_product_page)
    first_product_page.continue_shopping_button.click()
    home_page.cart_span.click()
    cart_page.remove_from_cart_link.click()
    assert_element_visible_with_text(cart_page.items_info_span, 'There are no more items in your cart')

def test_proceed_to_checkout_link_is_working(home_page, first_product_page, cart_page):
    """
    UI Test: Verify that the 'Proceed to checkout' link navigates the user to the personal information step.

    Steps:
        1. Wait for the first product link on the home page to be visible and click it.
        2. Wait for the 'Add to cart' button to be visible and click it.
        3. Wait for the 'Checkout' link in the product page modal to be visible and click it.
        4. Wait for the 'Proceed to checkout' link on the cart page to be visible and click it.
        5. Assert that the 'Personal Information' header is visible on the checkout page.

    Args:
        home_page: Page Object for the home page.
        first_product_page: Page Object for the first product's details page.
        cart_page: Page Object for the cart and checkout process.
    """
    cart_page.first_product_proceed_to_checkout(home_page, first_product_page)
    assert_element_visible_with_text(cart_page.personal_info_header, 'Personal Information')

def test_checkout_with_sign_in_option_is_working(home_page, first_product_page, cart_page):
    """
    UI Test: Verify that the checkout process allows users to proceed with the sign-in option.

    Steps:
        1. Wait for the first product link on the home page to be visible and click it.
        2. Wait for the 'Add to cart' button to be visible and click it.
        3. Wait for the 'Checkout' link in the product page modal to be visible and click it.
        4. Wait for the 'Proceed to checkout' link on the cart page to be visible and click it.
        5. Wait for the 'Sign in' link to be visible and click it.
        6. Retrieve expected locators and text values for the sign-in form.
        7. Assert that all retrieved elements are visible and contain the expected text.

    Args:
        home_page: Page Object for the home page.
        first_product_page: Page Object for the first product's details page.
        cart_page: Page Object for the cart and checkout process.
    """
    cart_page.first_product_proceed_to_checkout(home_page, first_product_page)
    cart_page.sign_in_link.click()
    locators_and_texts = get_sign_in_form_data(cart_page)
    assert_elements_visible_with_texts(locators_and_texts)

def test_personal_info_form_is_visible_with_text(home_page, first_product_page, cart_page):
    """
    UI Test: Verify that the personal information form in the checkout process is visible and displays all expected text labels.

    Steps:
        1. Wait for the first product link on the home page to be visible and click it.
        2. Wait for the 'Add to cart' button to be visible and click it.
        3. Wait for the 'Checkout' link in the product page modal to be visible and click it.
        4. Wait for the 'Proceed to checkout' link on the cart page to be visible and click it.
        5. Retrieve expected locators and text values for the personal information form.
        6. Assert that all retrieved elements are visible and contain the expected text.

    Args:
        home_page: Page Object for the home page.
        first_product_page: Page Object for the first product's details page.
        cart_page: Page Object for the cart and checkout process.
    """
    cart_page.first_product_proceed_to_checkout(home_page, first_product_page)
    locators_and_texts = get_personal_info_form_data(cart_page)
    assert_elements_visible_with_texts(locators_and_texts)

def test_submitting_personal_info_form_with_valid_data_is_working(home_page, first_product_page, cart_page):
    """
    UI Test: Verify that the address information form can be successfully submitted with valid data.

    Steps:
        1. Wait for the first product link on the home page to be visible and click it.
        2. Wait for the 'Add to cart' button to be visible and click it.
        3. Wait for the 'Checkout' link in the product page modal to be visible and click it.
        4. Wait for the 'Proceed to checkout' link on the cart page to be visible and click it.
        5. Submit the personal information form with valid data.
        6. Submit the address information form with valid data.
        7. Assert that the 'Edit' option is visible, confirming that the form was successfully submitted.

    Args:
        home_page: Page Object for the home page.
        first_product_page: Page Object for the first product's details page.
        cart_page: Page Object for the cart and checkout process.
    """
    cart_page.first_product_proceed_to_checkout(home_page, first_product_page)
    cart_page.submit_personal_info_form_with_valid_data()
    assert_element_visible_with_text(cart_page.personal_info_section, 'Edit')

def test_submitting_and_editing_personal_info_form_with_valid_data_is_working(home_page, first_product_page, cart_page):
    """
    Test Case: Validate submission and editing of the Personal Information form with valid data.
    Steps:
        1. Add the first product to the cart and proceed to checkout.
        2. Fill out the Personal Information form with randomly generated valid user data.
        3. Reopen the Personal Information section for editing.
        4. Verify that the first name input retains the submitted value.
    Expected Result:
        - First name field contains the previously entered valid value.
    """
    cart_page.first_product_proceed_to_checkout(home_page, first_product_page)
    user = cart_page.submit_personal_info_form_with_valid_data()
    cart_page.personal_info_section.click()
    expect(cart_page.first_name_input).to_have_value(user.first_name)

def test_address_form_is_visible_with_text(home_page, first_product_page, cart_page):
    """
    Test Case: Verify that the Address Information form is displayed with correct labels and texts.
    Steps:
        1. Add the first product to the cart and proceed to checkout.
        2. Submit the Personal Information form with valid data.
        3. Retrieve all address form labels and texts.
        4. Verify that all expected elements and texts are visible.
    Expected Result:
        - All Address Information form fields and labels are visible with correct text.
    """
    cart_page.first_product_proceed_to_checkout(home_page, first_product_page)
    cart_page.submit_personal_info_form_with_valid_data()
    locators_and_texts = get_address_form_data(cart_page)
    assert_elements_visible_with_texts(locators_and_texts)

def test_submitting_non_optional_address_info_form_with_valid_data_is_working(home_page, first_product_page, cart_page):
    """
    Test Case: Validate submission of Address Information form using only required fields.
    Steps:
        1. Add the first product to the cart and proceed to checkout.
        2. Submit the Personal Information form with valid data.
        3. Fill out only the required fields in the Address Information form.
        4. Submit the form.
    Expected Result:
        - The user is taken to the Delivery Information step where the 'Continue' button is visible.
    """
    cart_page.first_product_proceed_to_checkout(home_page, first_product_page)
    cart_page.submit_personal_info_form_with_valid_data()
    cart_page.fill_address_form_with_valid_data()
    cart_page.submit_address_form()
    assert_element_visible_with_text(cart_page.delivery_continue_button, 'Continue')

def test_submitting_full_address_info_form_with_valid_data_is_working(home_page, first_product_page, cart_page):
    """
    Test Case: Validate submission of Address Information form with required and optional fields.
    Steps:
        1. Add the first product to the cart and proceed to checkout.
        2. Submit the Personal Information form with valid data.
        3. Fill out both required and optional fields in the Address Information form.
        4. Submit the form.
    Expected Result:
        - The user is taken to the Delivery Information step where the 'Continue' button is visible.
    """
    cart_page.first_product_proceed_to_checkout(home_page, first_product_page)
    cart_page.submit_personal_info_form_with_valid_data()
    cart_page.fill_address_form_with_valid_data(include_optional=True)
    cart_page.submit_address_form()
    assert_element_visible_with_text(cart_page.delivery_continue_button, 'Continue')

def test_submitting_and_editing_non_optional_address_info_form_with_valid_data_is_working(home_page, first_product_page, cart_page):
    """
    Test Case: Validate submission and editing of Address Information form with only required fields.
    Steps:
        1. Add the first product to the cart and proceed to checkout.
        2. Submit the Personal Information form with valid data.
        3. Fill out and submit only the required Address Information fields.
        4. Reopen the Address Information section for editing.
        5. Verify that previously submitted data (e.g., city) is retained.
    Expected Result:
        - Address section correctly displays the submitted city value.
    """
    cart_page.first_product_proceed_to_checkout(home_page, first_product_page)
    cart_page.submit_personal_info_form_with_valid_data()
    user = cart_page.fill_address_form_with_valid_data()
    cart_page.submit_address_form()
    cart_page.section_checkout_address.wait_for(state="visible", timeout=10000)
    cart_page.section_checkout_address.click()
    expect(cart_page.address_delivery_div).to_contain_text(user.city)

def test_delivery_info_form_is_visible_with_text(home_page, first_product_page, cart_page):
    """
    Test Case: Verify that the Delivery Information form is displayed with correct labels and texts.
    Steps:
        1. Add the first product to the cart and proceed to checkout.
        2. Complete Personal Information and Address Information forms.
        3. Retrieve all delivery form labels and texts.
        4. Verify that all expected elements and texts are visible.
    Expected Result:
        - All Delivery Information form fields and labels are visible with correct text.
    """
    cart_page.first_product_proceed_to_checkout(home_page, first_product_page)
    cart_page.submit_personal_info_form_with_valid_data()
    cart_page.fill_address_form_with_valid_data()
    cart_page.submit_address_form()
    locators_and_texts = get_delivery_form_data(cart_page)
    assert_elements_visible_with_texts(locators_and_texts)

def test_delivery_info_form_is_working(home_page, first_product_page, cart_page):
    """
    Test Case: Validate submission of the Delivery Information form.
    Steps:
        1. Add the first product to the cart and proceed to checkout.
        2. Complete Personal Information and Address Information forms.
        3. Submit the Delivery Information form.
    Expected Result:
        - Payment options page is displayed, showing 'Pay by bank wire'.
    """
    cart_page.first_product_proceed_to_checkout(home_page, first_product_page)
    cart_page.submit_personal_info_form_with_valid_data()
    cart_page.fill_address_form_with_valid_data()
    cart_page.submit_address_form()
    cart_page.submit_shipping_form()
    assert_element_visible_with_text(cart_page.bank_wire_label, 'Pay by bank wire')

def test_payment_info_form_is_visible_with_text(home_page, first_product_page, cart_page):
    """
    Test Case: Verify that the Payment Information form is displayed with correct labels and texts.
    Steps:
        1. Add the first product to the cart and proceed to checkout.
        2. Complete Personal Information, Address Information, and Delivery Information forms.
        3. Retrieve all payment form labels and texts.
        4. Verify that all expected elements and texts are visible.
    Expected Result:
        - All Payment Information form fields and labels are visible with correct text.
    """
    cart_page.first_product_proceed_to_checkout(home_page, first_product_page)
    cart_page.submit_personal_info_form_with_valid_data()
    cart_page.fill_address_form_with_valid_data()
    cart_page.submit_address_form()
    cart_page.submit_shipping_form()
    cart_page.bank_wire_label.wait_for(state="visible", timeout=15000)
    locators_and_texts = get_payment_form_data(cart_page)
    assert_elements_visible_with_texts(locators_and_texts)

def test_order_first_product_is_working(home_page, first_product_page, cart_page):
    """
    Test Case: Validate the complete order process for the first product.
    Steps:
        1. Add the first product to the cart and proceed to checkout.
        2. Complete Personal Information, Address Information, and Delivery Information forms.
        3. Submit the Payment Information form.
    Expected Result:
        - Order confirmation page is displayed with the message 'Your order is confirmed'.
    """
    cart_page.first_product_proceed_to_checkout(home_page, first_product_page)
    cart_page.submit_personal_info_form_with_valid_data()
    cart_page.fill_address_form_with_valid_data()
    cart_page.submit_address_form()
    cart_page.submit_shipping_form()
    cart_page.submit_payment_form()
    assert_element_visible_with_text(cart_page.order_confirmed_header, 'Your order is confirmed')




    




