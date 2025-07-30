class CreateAccountPageLocators:
    """
    CSS selectors for locating UI elements on the create account page.
    Used in the SignPage Page Object.
    """
    FORM_LABELS = 'label.form-control-label'
    CUSTOM_CHECKBOX_LABELS = 'span.custom-checkbox label'
    GENDER_MALE_RADIO = 'input#field-id_gender-1'
    FIRST_NAME_INPUT = 'input#field-firstname'
    LAST_NAME_INPUT = 'input#field-lastname'
    EMAIL_INPUT = 'input#field-email'
    PASSWORD_INPUT = 'input#field-password'
    SAVE_FORM_BUTTON = 'button.form-control-submit'
    TERMS_AND_CONDITIONS_CHECKBOX = 'input[name="psgdpr"]'
    CUSTOMER_PRIVACY_CHECKBOX = 'input[name="customer_privacy"]'
