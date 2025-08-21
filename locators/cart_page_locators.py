class CartPageLocators:
    """
    CSS selectors for locating UI elements on the search results page.
    Used in the SearchPage Page Object.
    """

    # Cart management elements
    REMOVE_FROM_CART_LINK = 'a.remove-from-cart'
    ITEMS_INFO_SPAN = 'div.cart-overview.js-cart span.no-items'

    # Checkout process elements
    PROCEED_TO_CHECKOUT_LINK = 'div.checkout.cart-detailed-actions a'
    PERSONAL_INFO_HEADER = 'section#checkout-personal-information-step h1'
    ORDER_AS_GUEST_LINK = 'div.content a[aria-controls="checkout-guest-form"]'
    SIGN_IN_LINK = 'div.content a[aria-controls="checkout-login-form"]'

    # Sign-in form elements
    FORM_INFO_PARA = 'p.form-informations'
    FORM_EMAIL_LABEL = 'form#login-form label[for="field-email"]'
    FORM_PASSWORD_LABEL = 'form#login-form label[for="field-password"]'
    FORGOT_PASSWORD_LINK = 'div.forgot-password a'

    # Personal information form labels
    SOCIAL_TITLE_LABEL = 'div#checkout-guest-form label[for="field-id_gender"]'
    FIRST_NAME_LABEL = 'div#checkout-guest-form label[for="field-firstname"]'
    LAST_NAME_LABEL = 'div#checkout-guest-form label[for="field-lastname"]'
    EMAIL_LABEL = 'div#checkout-guest-form label[for="field-email"]'
    PASSWORD_LABEL = 'div#checkout-guest-form label[for="field-password"]'
    BIRTHDAY_LABEL = 'div#checkout-guest-form label[for="field-birthday"]'
    CHECKBOX_LABELS = 'span.custom-checkbox label'

    # Continue button for progressing through checkout steps
    CONTINUE_BUTTON = 'footer.form-footer.clearfix button[data-link-action="register-new-customer"]'

    # Personal information form inputs
    SOCIAL_TITLE_CHECKBOX_MALE = 'input#field-id_gender-1'
    FIRST_NAME_INPUT = 'input#field-firstname'
    LAST_NAME_INPUT = 'input#field-lastname'
    EMAIL_INPUT = 'input#field-email'
    PASSWORD_INPUT = 'input#field-password'
    BIRTHDAY_INPUT = 'input#field-birthday'
    RECEIVE_OFFERS_CHECKBOX = 'input[name="optin"]'
    TERMS_CONDITIONS_CHECKBOX = 'input[name="psgdpr"]'
    NEWSLETTER_CHECKBOX = 'input[name="newsletter"]'
    CUSTOMER_PRIVACY_CHECKBOX = 'input[name="customer_privacy"]'
    PERSONAL_INFO_CONTINUE_BUTTON = 'button[data-link-action="register-new-customer"]'
    PERSONAL_INFO_SECTION = 'section#checkout-personal-information-step'
    PERSONAL_INFO_EDIT_SPAN = 'section#checkout-personal-information-step span.step-edit'

    # Address information form labels
    ADDRESS_FIRST_NAME_LABEL = 'section.form-fields label[for="field-firstname"]'
    ADDRESS_LAST_NAME_LABEL = 'section.form-fields label[for="field-lastname"]'
    ADDRESS_COMPANY_LABEL = 'section.form-fields label[for="field-company"]'
    ADDRESS_VAT_LABEL = 'section.form-fields label[for="field-vat_number"]'
    ADDRESS_LABEL = 'section.form-fields label[for="field-address1"]'
    ADDRESS_POSTCODE_LABEL = 'section.form-fields label[for="field-postcode"]'
    ADDRESS_CITY_LABEL = 'section.form-fields label[for="field-city"]'
    ADDRESS_COUNTRY_LABEL = 'section.form-fields label[for="field-id_country"]'
    ADDRESS_PHONE_LABEL = 'section.form-fields label[for="field-phone"]'
    SAME_ADDRESS_LABEL = 'section.form-fields label[for="use_same_address"]'
    ADDRESS_CONTINUE_BUTTON = 'footer button[name="confirm-addresses"]'

    # Address information form inputs
    ADDRESS_COMPANY_INPUT = 'input#field-company'
    ADDRESS_VAT_INPUT = 'input#field-vat_number'
    ADDRESS_INPUT = 'input#field-address1'
    ADDRESS_POSTCODE_INPUT = 'input#field-postcode'
    ADDRESS_CITY_INPUT = 'input#field-city'
    ADDRESS_PHONE_INPUT = 'input#field-phone'
    ADDRESS_INFO_EDIT_SPAN = 'section#checkout-addresses-step span.step-edit.text-muted'
    SECTION_CHECKOUT_ADDRESS = 'section#checkout-addresses-step'
    ADDRESS_DELIVERY_DIV = 'article#id_address_delivery-address-7'

    # Shipping information form labels
    CLICK_COLLECT_SPAN = 'label[for="delivery_option_1"] span.h6.carrier-name'
    MY_CARRIER_SPAN = 'label[for="delivery_option_2"] span.h6.carrier-name'
    DELIVERY_MESSAGE_LABEL = 'label[for="delivery_message"]'
    DELIVERY_CONTINUE_BUTTON = 'button[name="confirmDeliveryOption"]'
    SECTION_CHECKOUT_DELIVERY = 'section#checkout-delivery-step'

    # Shipping information form inputs
    MY_CARRIER_INPUT = 'input#delivery_option_2'

    # Payment information form labels
    BANK_WIRE_LABEL = 'div#payment-option-1-container'
    CASH_ON_DELIVERY_LABEL = 'div#payment-option-2-container'
    CHECK_LABEL = 'div#payment-option-3-container'
    TERMS_OF_SERVICE_LABEL = 'form#conditions-to-approve'

    # Payment information form inputs
    CASH_ON_DELIVERY_INPUT = 'input#payment-option-2'
    TERMS_OF_SERVICE_INPUT = 'input[name="conditions_to_approve[terms-and-conditions]"]'
    PLACE_ORDER_BUTTON = 'div#payment-confirmation button'

    ORDER_CONFIRMED_HEADER = 'section#content-hook_order_confirmation h3'

