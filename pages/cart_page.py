from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators

class CartPage(BasePage):
    """
    Page Object Model for the Search results page.

    Provides access to search result-specific elements and interactions.
    The content is rendered inside the '#framelive' iframe.
    Inherits common utility methods and assertions from BasePage.
    """
    
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.remove_from_cart_link = self.frame.locator(CartPageLocators.REMOVE_FROM_CART_LINK)
        self.items_info_span = self.frame.locator(CartPageLocators.ITEMS_INFO_SPAN)
        self.proceed_to_checkout_link = self.frame.locator(CartPageLocators.PROCEED_TO_CHECKOUT_LINK)
        self.personal_info_header = self.frame.locator(CartPageLocators.PERSONAL_INFO_HEADER)
        self.order_as_guest_link = self.frame.locator(CartPageLocators.ORDER_AS_GUEST_LINK)
        self.sign_in_link = self.frame.locator(CartPageLocators.SIGN_IN_LINK)
        self.form_info_para = self.frame.locator(CartPageLocators.FORM_INFO_PARA)
        self.form_email_label = self.frame.locator(CartPageLocators.FORM_EMAIL_LABEL)
        self.form_password_label = self.frame.locator(CartPageLocators.FORM_PASSWORD_LABEL)
        self.forgot_password_link = self.frame.locator(CartPageLocators.FORGOT_PASSWORD_LINK)
        self.social_title_label = self.frame.locator(CartPageLocators.SOCIAL_TITLE_LABEL)
        self.first_name_label = self.frame.locator(CartPageLocators.FIRST_NAME_LABEL)
        self.last_name_label = self.frame.locator(CartPageLocators.LAST_NAME_LABEL)
        self.email_label = self.frame.locator(CartPageLocators.EMAIL_LABEL)
        self.password_label = self.frame.locator(CartPageLocators.PASSWORD_LABEL)
        self.birthday_label = self.frame.locator(CartPageLocators.BIRTHDAY_LABEL)
        self.checkbox_labels = self.frame.locator(CartPageLocators.CHECKBOX_LABELS)
        self.continue_button = self.frame.locator(CartPageLocators.CONTINUE_BUTTON)
