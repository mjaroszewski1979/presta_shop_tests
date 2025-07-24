class SignPageLocators:
    """
    CSS selectors for locating UI elements on the sign-in (login) page.
    Used in the SignPage Page Object.
    """
    SIGN_IN_BUTTON = 'button#submit-login'
    EMAIL_INPUT = 'input#email'
    AUTH_ALERT_LI = 'div.help-block li.alert-danger'
    FORGOT_PASSWORD_LINK = 'div.forgot-password a'
    SEND_RESET_LINK_BUTTON = 'button#send-reset-link'
    RESET_PASSWORD_SUCCESS_PARA = 'div#content p'