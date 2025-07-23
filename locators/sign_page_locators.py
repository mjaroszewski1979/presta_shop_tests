class SignPageLocators:
    """
    CSS selectors for locating UI elements on the sign-in (login) page.
    Used in the SignPage Page Object.
    """
    SIGN_IN_BUTTON = 'button#submit-login'
    EMAIL_INPUT = 'input#field-email'
    PASSWORD_INPUT = 'input#field-password'
    AUTH_ALERT_LI = 'div.help-block li.alert-danger'