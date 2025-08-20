# Import the base page object providing reusable browser interaction methods.
from pages.base_page import BasePage

# Import all locators related to the Cart Page for element identification.
from locators.cart_page_locators import CartPageLocators

# Import utility functions for generating realistic test data (e.g., user details).
from utils.home_page_utils import (
    generate_unique_email, 
    generate_password, 
    generate_first_name, 
    generate_last_name, 
    generate_birthdate,
    generate_company_name,
    generate_vat_number,
    generate_postal_code,
    generate_street_address,
    generate_city_name,
    generate_phone_number)

class CartPage(BasePage):
    """
    Page Object Model (POM) representation of the Cart Page.
    Inherits common browser actions from BasePage and initializes locators specific to the cart,
    checkout process, and personal information forms.
    """
    def __init__(self, page):
        """
        Initialize the CartPage with page context and locate all relevant UI elements 
        within the cart and checkout frames.

        Args:
            page (playwright.sync_api.Page): Playwright page object for browser interaction.
        """
        super().__init__(page)

        # Locate iframe containing the cart page content
        self.frame = page.frame_locator("#framelive")

        # Cart management elements
        self.remove_from_cart_link = self.frame.locator(CartPageLocators.REMOVE_FROM_CART_LINK)
        self.items_info_span = self.frame.locator(CartPageLocators.ITEMS_INFO_SPAN)

        # Checkout process elements
        self.proceed_to_checkout_link = self.frame.locator(CartPageLocators.PROCEED_TO_CHECKOUT_LINK)
        self.personal_info_header = self.frame.locator(CartPageLocators.PERSONAL_INFO_HEADER)
        self.order_as_guest_link = self.frame.locator(CartPageLocators.ORDER_AS_GUEST_LINK)
        self.sign_in_link = self.frame.locator(CartPageLocators.SIGN_IN_LINK)

        # Sign-in form elements
        self.form_info_para = self.frame.locator(CartPageLocators.FORM_INFO_PARA)
        self.form_email_label = self.frame.locator(CartPageLocators.FORM_EMAIL_LABEL)
        self.form_password_label = self.frame.locator(CartPageLocators.FORM_PASSWORD_LABEL)
        self.forgot_password_link = self.frame.locator(CartPageLocators.FORGOT_PASSWORD_LINK)

        # Personal information form labels
        self.social_title_label = self.frame.locator(CartPageLocators.SOCIAL_TITLE_LABEL)
        self.first_name_label = self.frame.locator(CartPageLocators.FIRST_NAME_LABEL)
        self.last_name_label = self.frame.locator(CartPageLocators.LAST_NAME_LABEL)
        self.email_label = self.frame.locator(CartPageLocators.EMAIL_LABEL)
        self.password_label = self.frame.locator(CartPageLocators.PASSWORD_LABEL)
        self.birthday_label = self.frame.locator(CartPageLocators.BIRTHDAY_LABEL)
        self.checkbox_labels = self.frame.locator(CartPageLocators.CHECKBOX_LABELS)
        self.personal_info_edit_span = self.frame.locator(CartPageLocators.PERSONAL_INFO_EDIT_SPAN)
        self.personal_info_continue_button = self.frame.locator(CartPageLocators.PERSONAL_INFO_CONTINUE_BUTTON)

        # Personal information form inputs
        self.social_title_checkbox_male = self.frame.locator(CartPageLocators.SOCIAL_TITLE_CHECKBOX_MALE)
        self.first_name_input = self.frame.locator(CartPageLocators.FIRST_NAME_INPUT)
        self.last_name_input = self.frame.locator(CartPageLocators.LAST_NAME_INPUT)
        self.email_input = self.frame.locator(CartPageLocators.EMAIL_INPUT)
        self.password_input = self.frame.locator(CartPageLocators.PASSWORD_INPUT)
        self.birthday_input = self.frame.locator(CartPageLocators.BIRTHDAY_INPUT)
        self.receive_offers_checkbox = self.frame.locator(CartPageLocators.RECEIVE_OFFERS_CHECKBOX)
        self.terms_conditions_checkbox = self.frame.locator(CartPageLocators.TERMS_CONDITIONS_CHECKBOX)
        self.newsletter_checkbox = self.frame.locator(CartPageLocators.NEWSLETTER_CHECKBOX)
        self.customer_privacy_checkbox = self.frame.locator(CartPageLocators.CUSTOMER_PRIVACY_CHECKBOX)

        # Address information form labels
        self.address_first_name_label = self.frame.locator(CartPageLocators.ADDRESS_FIRST_NAME_LABEL)
        self.address_last_name_label = self.frame.locator(CartPageLocators.ADDRESS_LAST_NAME_LABEL)
        self.address_company_label = self.frame.locator(CartPageLocators.ADDRESS_COMPANY_LABEL)
        self.address_vat_label = self.frame.locator(CartPageLocators.ADDRESS_VAT_LABEL)
        self.address_label = self.frame.locator(CartPageLocators.ADDRESS_LABEL)
        self.address_postcode_label = self.frame.locator(CartPageLocators.ADDRESS_POSTCODE_LABEL)
        self.address_city_label = self.frame.locator(CartPageLocators.ADDRESS_CITY_LABEL)
        self.address_country_label = self.frame.locator(CartPageLocators.ADDRESS_COUNTRY_LABEL)
        self.address_phone_label = self.frame.locator(CartPageLocators.ADDRESS_PHONE_LABEL)
        self.same_address_label = self.frame.locator(CartPageLocators.SAME_ADDRESS_LABEL)
        self.address_continue_button = self.frame.locator(CartPageLocators.ADDRESS_CONTINUE_BUTTON)
        self.address_info_edit_span = self.frame.locator(CartPageLocators.ADDRESS_INFO_EDIT_SPAN)
        self.section_checkout_address = self.frame.locator(CartPageLocators.SECTION_CHECKOUT_ADDRESS)

        # Address information form inputs
        self.address_company_input = self.frame.locator(CartPageLocators.ADDRESS_COMPANY_INPUT)
        self.address_vat_input = self.frame.locator(CartPageLocators.ADDRESS_VAT_INPUT)
        self.address_input = self.frame.locator(CartPageLocators.ADDRESS_INPUT)
        self.address_postcode_input = self.frame.locator(CartPageLocators.ADDRESS_POSTCODE_INPUT)
        self.address_city_input = self.frame.locator(CartPageLocators.ADDRESS_CITY_INPUT)
        self.address_phone_input = self.frame.locator(CartPageLocators.ADDRESS_PHONE_INPUT)

        # Shipping information form labels
        self.click_collect_span = self.frame.locator(CartPageLocators.CLICK_COLLECT_SPAN)
        self.my_carrier_span = self.frame.locator(CartPageLocators.MY_CARRIER_SPAN)
        self.delivery_message_label = self.frame.locator(CartPageLocators.DELIVERY_MESSAGE_LABEL)
        self.delivery_continue_button = self.frame.locator(CartPageLocators.DELIVERY_CONTINUE_BUTTON)
        self.section_checkout_delivery = self.frame.locator(CartPageLocators.SECTION_CHECKOUT_DELIVERY)


        # Shipping information form inputs
        self.my_carrier_input = self.frame.locator(CartPageLocators.MY_CARRIER_INPUT)

        # Payment information form labels
        self.bank_wire_label = self.frame.locator(CartPageLocators.BANK_WIRE_LABEL)
        self.cash_on_delivery_label = self.frame.locator(CartPageLocators.CASH_ON_DELIVERY_LABEL)
        self.check_label = self.frame.locator(CartPageLocators.CHECK_LABEL)
        self.terms_of_service_label = self.frame.locator(CartPageLocators.TERMS_OF_SERVICE_LABEL)

        # Payment information form inputs
        self.cash_on_delivery_input = self.frame.locator(CartPageLocators.CASH_ON_DELIVERY_INPUT)
        self.terms_of_service_input = self.frame.locator(CartPageLocators.TERMS_OF_SERVICE_INPUT)
        self.place_order_button = self.frame.locator(CartPageLocators.PLACE_ORDER_BUTTON)

        self.order_confirmed_header = self.frame.locator(CartPageLocators.ORDER_CONFIRMED_HEADER)




        # Continue button for progressing through checkout steps
        self.continue_button = self.frame.locator(CartPageLocators.CONTINUE_BUTTON)

    def submit_personal_info_form_with_valid_data(self):
        """
        Fill and submit the personal information form using randomly 
        generated valid test data. 
        Includes first name, last name, email, password, and birthday.
        Also checks all required agreement checkboxes before submission.
        """
        first_name= generate_first_name()
        last_name = generate_last_name()
        email = generate_unique_email()
        password = generate_password()
        birthday = generate_birthdate()

        self.social_title_checkbox_male.wait_for(state="visible", timeout=5000)
        self.social_title_checkbox_male.check()

        self.first_name_input.fill('')
        self.first_name_input.type(first_name, delay=100)
        self.last_name_input.fill('')
        self.last_name_input.type(last_name, delay=100)
        self.email_input.first.fill('')
        self.email_input.first.type(email, delay=100)
        self.password_input.first.fill('')
        self.password_input.first.type(password, delay=100)
        self.birthday_input.fill('')
        self.birthday_input.type(birthday, delay=100)
        self.receive_offers_checkbox.check() 
        self.terms_conditions_checkbox.check() 
        self.newsletter_checkbox.check() 
        self.customer_privacy_checkbox.check()
        self.personal_info_continue_button.click()

    def submit_address_form_with_valid_data(self):
        """
        Fill and submit the address information form with randomly 
        generated valid test data. 
        Includes company details, VAT number, street address, postcode, 
        city, and phone number.
        """
        company = generate_company_name()
        vat = generate_vat_number()
        address = generate_street_address()
        postcode = generate_postal_code()
        city = generate_city_name()
        phone = generate_phone_number()

        self.section_checkout_address.wait_for(state="visible", timeout=15000)
        
        self.address_company_input.fill('')
        self.address_company_input.type(company, delay=100)
        self.address_vat_input.fill('')
        self.address_vat_input.type(vat, delay=100)
        self.address_input.fill('')
        self.address_input.type(address, delay=100)
        self.address_postcode_input.fill('')
        self.address_postcode_input.type(postcode, delay=100)
        self.address_city_input.fill('')
        self.address_city_input.type(city, delay=100)
        self.address_phone_input.fill('')
        self.address_phone_input.type(phone, delay=100)
        self.address_continue_button.click()

    def submit_shipping_form(self):

        self.section_checkout_delivery.wait_for(state="visible", timeout=15000)
        self.delivery_continue_button.click()

    def submit_payment_form(self):

        self.bank_wire_label.wait_for(state="visible", timeout=15000)
        self.cash_on_delivery_input.check()
        self.terms_of_service_input.check()
        self.place_order_button.click()



 
