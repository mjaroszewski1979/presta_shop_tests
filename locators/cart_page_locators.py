class CartPageLocators:
    """
    CSS selectors for locating UI elements on the search results page.
    Used in the SearchPage Page Object.
    """
    REMOVE_FROM_CART_LINK = 'a.remove-from-cart'
    ITEMS_INFO_SPAN = 'div.cart-overview.js-cart span.no-items'
    PROCEED_TO_CHECKOUT_LINK = 'div.checkout.cart-detailed-actions a'
    PERSONAL_INFO_HEADER = 'section#checkout-personal-information-step h1'
    ORDER_AS_GUEST_LINK = 'div.content a[aria-controls="checkout-guest-form"]'
    SIGN_IN_LINK = 'div.content a[aria-controls="checkout-login-form"]'
    FORM_INFO_PARA = 'p.form-informations'
    FORM_EMAIL_LABEL = 'form#login-form label[for="field-email"]'
    FORM_PASSWORD_LABEL = 'form#login-form label[for="field-password"]'
    FORGOT_PASSWORD_LINK = 'div.forgot-password a'