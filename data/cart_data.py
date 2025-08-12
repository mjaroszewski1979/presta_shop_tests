def get_sign_in_form_data(cart_page):
    """
    Returns a list of tuples mapping each sign-in form element to its expected display text.
    This is used to validate that all sign-in form labels and links are visible and contain
    the correct content.

    Args:
        cart_page: An instance of the CartPage with sign-in form locators.

    Returns:
        list[tuple]: A list of (locator, expected_text) pairs for element verification.
    """
    return [
        (cart_page.form_email_label, "Email"),
        (cart_page.form_password_label, "Password"),
        (cart_page.forgot_password_link, "Forgot your password?"),

    ]
def get_personal_info_form_data(cart_page):
    """
    Returns a list of tuples mapping each personal information form element to its expected 
    display text. This is used to validate that all personal information fields, checkboxes, 
    and action buttons are visible and contain the correct content during the checkout process.

    Args:
        cart_page: An instance of the CartPage with personal information form locators.

    Returns:
        list[tuple]: A list of (locator, expected_text) pairs for element verification.
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
