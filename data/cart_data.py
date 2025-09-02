def get_sign_in_form_data(cart_page):
    """
    Collect locators and expected texts for the sign-in form.

    Returns a list of tuples mapping each sign-in form element to its
    expected display text. This enables verification that all sign-in
    labels, inputs, and links are present and contain correct values.

    Args:
        cart_page: Instance of CartPage exposing sign-in form locators.

    Returns:
        list[tuple]: A list of (locator, expected_text) pairs for validation.
    """
    return [
        (cart_page.form_email_label, "Email"),
        (cart_page.form_password_label, "Password"),
        (cart_page.forgot_password_link, "Forgot your password?"),

    ]
def get_personal_info_form_data(cart_page):
    """
    Collect locators and expected texts for the personal information form.

    Returns a list of tuples mapping each personal info field, checkbox,
    and button to its expected display text. Used to validate checkout 
    registration and account creation process.

    Args:
        cart_page: Instance of CartPage exposing personal info form locators.

    Returns:
        list[tuple]: A list of (locator, expected_text) pairs for validation.
    """
    return [
        (cart_page.social_title_label, "Social title"),
        (cart_page.first_name_label, "First name"),
        (cart_page.last_name_label, "Last name"),
        (cart_page.email_label, "Email"),
        (cart_page.password_label, "Password"),
        (cart_page.birthday_label, "Birthdate"),
        (cart_page.form_info_para, "Create an account"),
        (cart_page.checkbox_labels.first, "Receive offers from our partners"),
        (cart_page.checkbox_labels.nth(1), "I agree to the terms and conditions and the privacy policy"),
        (cart_page.checkbox_labels.nth(2), "Sign up for our newsletter"),
        (cart_page.checkbox_labels.nth(3), "Customer data privacy"),
        (cart_page.continue_button, "Continue"),
    ]

def get_address_form_data(cart_page):
    """
    Collect locators and expected texts for the address form.

    Returns a list of tuples mapping each address-related input field
    and action button to its expected display text. Ensures correct
    content during checkout address entry.

    Args:
        cart_page: Instance of CartPage exposing address form locators.

    Returns:
        list[tuple]: A list of (locator, expected_text) pairs for validation.
    """
    return [
        (cart_page.address_first_name_label, "First name"),
        (cart_page.address_last_name_label, "Last name"),
        (cart_page.address_company_label, "Company"),
        (cart_page.address_vat_label, "VAT number"),
        (cart_page.address_label, "Address"),
        (cart_page.address_city_label, "City"),
        (cart_page.address_country_label, "Country"),
        (cart_page.same_address_label, "Use this address for invoice too"),
        (cart_page.address_continue_button, "Continue"),
    ]

def get_delivery_form_data(cart_page):
    """
    Collect locators and expected texts for the delivery method form.

    Returns a list of tuples mapping each delivery option, message field,
    and action button to its expected display text. Used for verifying 
    shipping method selection during checkout.

    Args:
        cart_page: Instance of CartPage exposing delivery form locators.

    Returns:
        list[tuple]: A list of (locator, expected_text) pairs for validation.
    """
    return [
        (cart_page.click_collect_span, "Click and collect"),
        (cart_page.my_carrier_span, "My carrier"),
        (cart_page.delivery_message_label, "If you would like to add a comment about your order, please write it in the field below."),
        (cart_page.delivery_continue_button, "Continue"),
    ]

def get_payment_form_data(cart_page):
    """
    Collect locators and expected texts for the payment method form.

    Returns a list of tuples mapping each payment option and mandatory
    terms acceptance checkbox to its expected display text. Ensures that 
    payment options are properly rendered during checkout.

    Args:
        cart_page: Instance of CartPage exposing payment form locators.

    Returns:
        list[tuple]: A list of (locator, expected_text) pairs for validation.
    """
    return [
        (cart_page.bank_wire_label, "Pay by bank wire"),
        (cart_page.cash_on_delivery_label, "Pay by Cash on Delivery"),
        (cart_page.check_label, "Pay by Check"),
        (cart_page.terms_of_service_label, "I agree to the terms of service and will adhere to them unconditionally."),
    ]
