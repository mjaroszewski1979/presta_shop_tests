class ContactPageLocators:
    """
    Collection of CSS selectors for the Contact page.

    These locators are used to identify and interact with form fields, labels, 
    and messages within the ContactPage Page Object.
    """

    # Heading element of the contact form section
    CONTACT_FORM_HEADING = 'div.form-group h3'

    # Label for subject selection dropdown
    SUBJECT_LABEL = 'label[for="id_contact"]'

    # Dropdown select element for choosing subject
    SUBJECT_SELECT = 'select#id_contact'

    # Label for the email input field
    EMAIL_LABEL = 'label[for="email"]'

    # Input field for entering email address
    EMAIL_INPUT = 'input#email'

    # Label for file attachment upload
    ATTACHMENT_LABEL = 'label[for="file-upload"]'

    # Label for the message textarea
    MESSAGE_LABEL = 'label[for="contactform-message"]'

    # Textarea for entering message content
    MESSAGE_TEXTAREA = 'textarea#contactform-message'

    # Button to submit the contact form
    SEND_BUTTON = 'input[name="submitMessage"]'

    # Success message displayed after form submission
    SUCCESS_MESSAGE_LI = 'div.alert-success li'
