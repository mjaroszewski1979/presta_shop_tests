from pages.base_page import BasePage
from locators.first_product_page_locators import FirstProductPageLocators

class FirstProductPage(BasePage):
    """
    Page Object Model (POM) representation of the First Product Page.

    Encapsulates locators and interactions for the first product's detail page,
    which is rendered inside the '#framelive' iframe. Provides access to product
    information (name, price, description, composition), customization options 
    (size, color, quantity), and cart-related actions.
    Inherits reusable browser actions and assertions from BasePage.
    """
    def __init__(self, page):
        """
        Initialize the FirstProductPage with page context and locate all UI 
        elements related to the first product, including product details, 
        customization controls, cart actions, and modal confirmation details.

        Args:
            page (playwright.sync_api.Page): Playwright page object for browser interaction.
        """
        super().__init__(page)

        # -------------------------------
        # Product information elements
        # -------------------------------
        self.content_div_header = self.frame.locator(FirstProductPageLocators.CONTENT_DIV_HEADER)
        self.current_price_span = self.frame.locator(FirstProductPageLocators.CURRENT_PRICE_SPAN)
        self.description_short_para = self.frame.locator(FirstProductPageLocators.DESCRIPTION_SHORT_PARA)

        # -------------------------------
        # Product customization controls
        # -------------------------------
        self.size_span = self.frame.locator(FirstProductPageLocators.SIZE_SPAN)
        self.size_select = self.frame.locator(FirstProductPageLocators.SIZE_SELECT)
        self.color_variant_span = self.frame.locator(FirstProductPageLocators.COLOR_VARIANT_SPAN)
        self.color_black_input = self.frame.locator(FirstProductPageLocators.COLOR_BLACK_INPUT)
        self.quantity_label = self.frame.locator(FirstProductPageLocators.QUANTITY_LABEL)

        # -------------------------------
        # Social & reassurance elements
        # -------------------------------
        self.social_sharing_span = self.frame.locator(FirstProductPageLocators.SOCIAL_SHARING_SPAN)
        self.reassurance_div = self.frame.locator(FirstProductPageLocators.REASSURANCE_DIV)

        # -------------------------------
        # Cart interaction elements
        # -------------------------------
        self.description_long_para = self.frame.locator(FirstProductPageLocators.DESCRIPTION_LONG_PARA)
        self.product_details_link = self.frame.locator(FirstProductPageLocators.PRODUCT_DETAILS_LINK)
        self.composition_name = self.frame.locator(FirstProductPageLocators.COMPOSITION_NAME)
        self.composition_value = self.frame.locator(FirstProductPageLocators.COMPOSITION_VALUE)
        self.add_to_cart_button = self.frame.locator(FirstProductPageLocators.ADD_TO_CART_BUTTON)

        # -------------------------------
        # Quick view modal elements
        # -------------------------------
        self.quick_view_link = self.frame.locator(FirstProductPageLocators.QUICK_VIEW_LINK)
        self.modal_body_h1 = self.frame.locator(FirstProductPageLocators.MODAL_BODY_H1)

        # -------------------------------
        # Modal confirmation details
        # -------------------------------
        self.cart_success_message = self.frame.locator(FirstProductPageLocators.CART_SUCCESS_MESSAGE)
        self.continue_shopping_button = self.frame.locator(FirstProductPageLocators.CONTINUE_SHOPPING_BUTTON)
        self.checkout_link = self.frame.locator(FirstProductPageLocators.CHECKOUT_LINK)
        self.modal_product_name = self.frame.locator(FirstProductPageLocators.MODAL_PRODUCT_NAME)
        self.modal_product_price = self.frame.locator(FirstProductPageLocators.MODAL_PRODUCT_PRICE)
        self.modal_product_size = self.frame.locator(FirstProductPageLocators.MODAL_PRODUCT_SIZE)
        self.modal_product_color = self.frame.locator(FirstProductPageLocators.MODAL_PRODUCT_COLOR)
        self.modal_product_quantity = self.frame.locator(FirstProductPageLocators.MODAL_PRODUCT_QUANTITY)
        self.modal_product_count_info = self.frame.locator(FirstProductPageLocators.MODAL_PRODUCT_COUNT_INFO)
        self.modal_subtotal_value = self.frame.locator(FirstProductPageLocators.MODAL_SUBTOTAL_VALUE)
        self.modal_shipping_value = self.frame.locator(FirstProductPageLocators.MODAL_SHIPPING_VALUE)
        self.modal_total_value = self.frame.locator(FirstProductPageLocators.MODAL_TOTAL_VALUE)
        

    # -------------------------------
    # Product customization methods
    # -------------------------------
    def select_size_option(self, size):
        """
        Select a specific size option for the product.

        Args:
            size (str): The size value to select from the dropdown.
        """
        self.size_select.select_option(size)