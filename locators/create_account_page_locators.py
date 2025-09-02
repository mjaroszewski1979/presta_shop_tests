class CreateAccountPageLocators:
    """
    CSS selectors for locating UI elements on the Create Account page.

    These locators are used within the CreateAccountPage Page Object to interact
    with form fields, checkboxes, radio buttons, and submission actions 
    necessary for account creation.
    """

    # Labels for form input fields
    FORM_LABELS = 'label.form-control-label'

    # Labels associated with custom-styled checkboxes
    CUSTOM_CHECKBOX_LABELS = 'span.custom-checkbox label'

    # Radio button for selecting male gender option
    GENDER_MALE_RADIO = 'input#field-id_gender-1'

    # Input field for entering first name
    FIRST_NAME_INPUT = 'input#field-firstname'

    # Input field for entering last name
    LAST_NAME_INPUT = 'input#field-lastname'

    # Input field for entering email address
    EMAIL_INPUT = 'input#field-email'

    # Input field for entering password
    PASSWORD_INPUT = 'input#field-password'

    # Button to submit and save the account creation form
    SAVE_FORM_BUTTON = 'button.form-control-submit'

    # Checkbox to agree to terms and conditions (GDPR compliance)
    TERMS_AND_CONDITIONS_CHECKBOX = 'input[name="psgdpr"]'

    # Checkbox to accept customer privacy policy
    CUSTOMER_PRIVACY_CHECKBOX = 'input[name="customer_privacy"]'
