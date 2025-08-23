import random

# Import the base page object providing reusable browser interaction methods.
from pages.base_page import BasePage

# Import all locators related to the Cart Page for element identification.
from locators.cart_page_locators import CartPageLocators

# Import user data model for generating valid user credentials.
from models.user_data import UserData

# Import utility functions for generating realistic test data (e.g., user details).
from utils.home_page_utils import type_text_into_input_field

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

        # -------------------------------
        # Cart management elements
        # -------------------------------
        self.remove_from_cart_link = self.frame.locator(CartPageLocators.REMOVE_FROM_CART_LINK)
        self.items_info_span = self.frame.locator(CartPageLocators.ITEMS_INFO_SPAN)

        # -------------------------------
        # Checkout process elements
        # -------------------------------
        self.proceed_to_checkout_link = self.frame.locator(CartPageLocators.PROCEED_TO_CHECKOUT_LINK)
        self.personal_info_header = self.frame.locator(CartPageLocators.PERSONAL_INFO_HEADER)
        self.order_as_guest_link = self.frame.locator(CartPageLocators.ORDER_AS_GUEST_LINK)
        self.sign_in_link = self.frame.locator(CartPageLocators.SIGN_IN_LINK)

        # -------------------------------
        # Sign-in form elements
        # -------------------------------
        self.form_info_para = self.frame.locator(CartPageLocators.FORM_INFO_PARA)
        self.form_email_label = self.frame.locator(CartPageLocators.FORM_EMAIL_LABEL)
        self.form_password_label = self.frame.locator(CartPageLocators.FORM_PASSWORD_LABEL)
        self.forgot_password_link = self.frame.locator(CartPageLocators.FORGOT_PASSWORD_LINK)

        # -------------------------------
        # Personal information form labels
        # -------------------------------
        self.social_title_label = self.frame.locator(CartPageLocators.SOCIAL_TITLE_LABEL)
        self.first_name_label = self.frame.locator(CartPageLocators.FIRST_NAME_LABEL)
        self.last_name_label = self.frame.locator(CartPageLocators.LAST_NAME_LABEL)
        self.email_label = self.frame.locator(CartPageLocators.EMAIL_LABEL)
        self.password_label = self.frame.locator(CartPageLocators.PASSWORD_LABEL)
        self.birthday_label = self.frame.locator(CartPageLocators.BIRTHDAY_LABEL)
        self.checkbox_labels = self.frame.locator(CartPageLocators.CHECKBOX_LABELS)
        self.personal_info_section = self.frame.locator(CartPageLocators.PERSONAL_INFO_SECTION)
        self.personal_info_edit_span = self.frame.locator(CartPageLocators.PERSONAL_INFO_EDIT_SPAN)
        self.personal_info_continue_button = self.frame.locator(CartPageLocators.PERSONAL_INFO_CONTINUE_BUTTON)

        # -------------------------------
        # Personal information form inputs
        # -------------------------------
        self.social_title_checkbox_male = self.frame.locator(CartPageLocators.SOCIAL_TITLE_CHECKBOX_MALE)
        self.social_title_checkbox_female = self.frame.locator(CartPageLocators.SOCIAL_TITLE_CHECKBOX_FEMALE)
        self.first_name_input = self.frame.locator(CartPageLocators.FIRST_NAME_INPUT)
        self.last_name_input = self.frame.locator(CartPageLocators.LAST_NAME_INPUT)
        self.email_input = self.frame.locator(CartPageLocators.EMAIL_INPUT)
        self.password_input = self.frame.locator(CartPageLocators.PASSWORD_INPUT)
        self.birthday_input = self.frame.locator(CartPageLocators.BIRTHDAY_INPUT)
        self.receive_offers_checkbox = self.frame.locator(CartPageLocators.RECEIVE_OFFERS_CHECKBOX)
        self.terms_conditions_checkbox = self.frame.locator(CartPageLocators.TERMS_CONDITIONS_CHECKBOX)
        self.newsletter_checkbox = self.frame.locator(CartPageLocators.NEWSLETTER_CHECKBOX)
        self.customer_privacy_checkbox = self.frame.locator(CartPageLocators.CUSTOMER_PRIVACY_CHECKBOX)


        # -------------------------------
        # Address information form labels
        # -------------------------------
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

        # -------------------------------
        # Address information form inputs
        # -------------------------------
        self.address_company_input = self.frame.locator(CartPageLocators.ADDRESS_COMPANY_INPUT)
        self.address_vat_input = self.frame.locator(CartPageLocators.ADDRESS_VAT_INPUT)
        self.address_input = self.frame.locator(CartPageLocators.ADDRESS_INPUT)
        self.address_postcode_input = self.frame.locator(CartPageLocators.ADDRESS_POSTCODE_INPUT)
        self.address_city_input = self.frame.locator(CartPageLocators.ADDRESS_CITY_INPUT)
        self.address_phone_input = self.frame.locator(CartPageLocators.ADDRESS_PHONE_INPUT)
        self.address_delivery_div = self.frame.locator(CartPageLocators.ADDRESS_DELIVERY_DIV)

        # -------------------------------
        # Shipping information form labels
        # -------------------------------
        self.click_collect_span = self.frame.locator(CartPageLocators.CLICK_COLLECT_SPAN)
        self.my_carrier_span = self.frame.locator(CartPageLocators.MY_CARRIER_SPAN)
        self.delivery_message_label = self.frame.locator(CartPageLocators.DELIVERY_MESSAGE_LABEL)
        self.delivery_continue_button = self.frame.locator(CartPageLocators.DELIVERY_CONTINUE_BUTTON)
        self.section_checkout_delivery = self.frame.locator(CartPageLocators.SECTION_CHECKOUT_DELIVERY)

        # -------------------------------
        # Shipping information form inputs
        # -------------------------------
        self.my_carrier_input = self.frame.locator(CartPageLocators.MY_CARRIER_INPUT)

        # -------------------------------
        # Payment information form labels
        # -------------------------------
        self.bank_wire_label = self.frame.locator(CartPageLocators.BANK_WIRE_LABEL)
        self.cash_on_delivery_label = self.frame.locator(CartPageLocators.CASH_ON_DELIVERY_LABEL)
        self.check_label = self.frame.locator(CartPageLocators.CHECK_LABEL)
        self.terms_of_service_label = self.frame.locator(CartPageLocators.TERMS_OF_SERVICE_LABEL)

        # -------------------------------
        # Payment information form inputs
        # -------------------------------
        self.cash_on_delivery_input = self.frame.locator(CartPageLocators.CASH_ON_DELIVERY_INPUT)
        self.terms_of_service_input = self.frame.locator(CartPageLocators.TERMS_OF_SERVICE_INPUT)
        self.place_order_button = self.frame.locator(CartPageLocators.PLACE_ORDER_BUTTON)

        # -------------------------------
        # Order confirmation elements
        # -------------------------------
        self.order_confirmed_header = self.frame.locator(CartPageLocators.ORDER_CONFIRMED_HEADER)

        # -------------------------------
        # Shared navigation element
        # -------------------------------
        self.continue_button = self.frame.locator(CartPageLocators.CONTINUE_BUTTON)

    # -------------------------------
    # Form submission methods
    # -------------------------------
    def submit_personal_info_form_with_valid_data(self):
        """
        Fill and submit the personal information form using randomly 
        generated valid test data. 
        Includes first name, last name, email, password, and birthday.
        Also checks all required agreement checkboxes before submission.
        """

        user = UserData.generate_valid()

        self.check_gender_checkbox()

        type_text_into_input_field(self.first_name_input, user.first_name)
        type_text_into_input_field(self.last_name_input, user.last_name)
        type_text_into_input_field(self.email_input.first, user.email)
        type_text_into_input_field(self.password_input.first, user.password)
        type_text_into_input_field(self.birthday_input, user.birthday)
        self.receive_offers_checkbox.check() 
        self.terms_conditions_checkbox.check() 
        self.newsletter_checkbox.check() 
        self.customer_privacy_checkbox.check()
        self.personal_info_continue_button.click()

        return user

    def fill_address_form_with_valid_data(self, include_optional: bool = False):
        """
        Fill the address information form with randomly generated valid test data.

        Args:
            include_optional (bool): 
                - False (default) → fill only required fields.
                - True → fill all fields, including optional ones.
        """
        # Required fields
        user = UserData.generate_valid()

        self.section_checkout_address.wait_for(state="visible", timeout=15000)

        type_text_into_input_field(self.address_input, user.address)
        type_text_into_input_field(self.address_postcode_input, user.postcode)
        type_text_into_input_field(self.address_city_input, user.city)

        # Optional fields
        if include_optional:

            type_text_into_input_field(self.address_company_input, user.company)  
            type_text_into_input_field(self.address_vat_input, user.vat)  
            type_text_into_input_field(self.address_phone_input, user.phone)

        return user



    def submit_address_form(self):
        """Click the continue button to submit the address form and move to the next step."""
        self.address_continue_button.click()

    def submit_shipping_form(self):
        """Wait for the shipping section and submit the shipping form by clicking continue."""
        self.section_checkout_delivery.wait_for(state="visible", timeout=15000)
        self.delivery_continue_button.click()

    def submit_payment_form(self):
        """Wait for payment options, select payment and terms, and confirm order placement."""
        self.bank_wire_label.wait_for(state="visible", timeout=15000)
        self.cash_on_delivery_input.check()
        self.terms_of_service_input.check()
        self.place_order_button.click()

    # -------------------------------
    # Helper methods for product checkout
    # -------------------------------
    
    def first_product_add_to_cart(self, home_page, first_product_page):
        """Add the first available product from the home page into the shopping cart."""
        home_page.first_product_link.first.click()
        first_product_page.add_to_cart_button.click()

    def first_product_proceed_to_checkout(self, home_page, first_product_page):
        """Add first product and immediately proceed through initial checkout step."""
        self.first_product_add_to_cart(home_page, first_product_page)
        first_product_page.checkout_link.click()
        self.proceed_to_checkout_link.click()

    # -------------------------------
    # Utility methods
    # -------------------------------
    def check_gender_checkbox(self):
        """Randomly select and check either 'male' or 'female' gender option."""
        choice = random.randint(0, 1)
        if choice == 0:
            self.social_title_checkbox_male.check()
        else:
            self.social_title_checkbox_female.check()






 
