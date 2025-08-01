def get_contact_label_data(contact_page):
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
        (contact_page.contact_form_heading, "Contact us"),
        (contact_page.subject_label, "Subject"),
        (contact_page.email_label, "Email address"),
        (contact_page.attachment_label.first, "Attachment"),
        (contact_page.message_label, "Message"),
    ]
