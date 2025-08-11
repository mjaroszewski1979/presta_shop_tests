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
def get_personal_info_form_data(cart_page):
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
