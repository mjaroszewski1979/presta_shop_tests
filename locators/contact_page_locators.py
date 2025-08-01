class ContactPageLocators:
    """
    CSS selectors for locating UI elements on the Contact page.
    Used in the ContactPage Page Object.
    """
    CONTACT_FORM_HEADING = 'div.form-group h3'
    SUBJECT_LABEL = 'label[for="id_contact"]'
    EMAIL_LABEL = 'label[for="email"]'
    ATTACHMENT_LABEL = 'label[for="file-upload"]'
    MESSAGE_LABEL = 'label[for="contactform-message"]'
    SEND_BUTTON = 'input[name="submitMessage"]'
