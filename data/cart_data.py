def get_sign_in_form_data(cart_page):
    """
    Returns a list of tuples mapping each label element in the 'Contact' form
    to its expected display text. This is used to validate that form labels are 
    visible and contain correct content.

    Args:
        contact_page: An instance of the ContactPage with form label locators.

    Returns:
        list[tuple]: A list of (locator, expected_text) pairs for label verification.
    """
    return [
        (cart_page.form_email_label, "Email"),
        (cart_page.form_password_label, "Password"),
        (cart_page.forgot_password_link, "Forgot your password?"),

    ]
