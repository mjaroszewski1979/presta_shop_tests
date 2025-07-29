def get_create_account_label_data(create_account_page):
    """
    Returns a list of tuples mapping each label element in the 'Create Account' form
    to its expected display text. This is used to validate that form labels are 
    visible and contain correct content.

    Args:
        create_account_page: An instance of the CreateAccountPage with form label locators.

    Returns:
        list[tuple]: A list of (locator, expected_text) pairs for label verification.
    """
    return [
        (create_account_page.form_labels.nth(0), "Social title"),
        (create_account_page.form_labels.nth(1), "First name"),
        (create_account_page.form_labels.nth(2), "Last name"),
        (create_account_page.form_labels.nth(3), "Email"),
        (create_account_page.form_labels.nth(4), "Password"),
        (create_account_page.form_labels.nth(5), "Birthdate"),
    ]
