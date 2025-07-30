from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
    """
    Page Object Model (POM) representation of the Home Page.
    Inherits common browser actions from BasePage and initializes locators specific to the homepage.
    """
    def __init__(self, page):
        """
        Initialize the HomePage with page context and locate all relevant UI elements within the homepage frame.

        Args:
            page (playwright.sync_api.Page): Playwright page object for browser interaction.
        """
        super().__init__(page)

        # Locate iframe containing the main homepage content
        self.frame = page.frame_locator("#framelive")

        # Top navigation and header elements
        self.contact_link = self.frame.locator(HomePageLocators.CONTACT_LINK)
        self.sign_in_span = self.frame.locator(HomePageLocators.SIGN_IN_SPAN)
        self.sign_out_link = self.frame.locator(HomePageLocators.SIGN_OUT_LINK)
        self.cart_span = self.frame.locator(HomePageLocators.CART_SPAN)
        self.my_store_img = self.frame.locator(HomePageLocators.MY_STORE_IMG)

        # Main category navigation links
        self.clothes_link = self.frame.locator(HomePageLocators.CLOTHES_LINK)
        self.clothes_men_link = self.frame.locator(HomePageLocators.CLOTHES_MEN_LINK)
        self.clothes_women_link = self.frame.locator(HomePageLocators.CLOTHES_WOMEN_LINK)
        self.accessories_link = self.frame.locator(HomePageLocators.ACCESSORIES_LINK)
        self.accessories_stationery_link = self.frame.locator(HomePageLocators.ACCESSORIES_STATIONERY_LINK)
        self.accessories_home_link = self.frame.locator(HomePageLocators.ACCESSORIES_HOME_LINK)
        self.art_link = self.frame.locator(HomePageLocators.ART_LINK)

        # Product and carousel sections
        self.featured_products = self.frame.locator(HomePageLocators.FEATURED_PRODUCTS)
        self.featured_products_h2 = self.frame.locator(HomePageLocators.FEATURED_PRODUCTS_H2)
        self.sale_products = self.frame.locator(HomePageLocators.SALE_PRODUCTS)
        self.carousel_headings = self.frame.locator(HomePageLocators.CAROUSEL_HEADINGS)
        self.carousel_next_icon = self.frame.locator(HomePageLocators.CAROUSEL_NEXT_ICON)

        # Search and language options
        self.search_catalog_input = self.frame.locator(HomePageLocators.SEARCH_CATALOG_INPUT)
        self.language_dropdown_button = self.frame.locator(HomePageLocators.LANGUAGE_DROPDOWN_BUTTON)
        self.language_option_spanish = self.frame.locator(HomePageLocators.LANGUAGE_OPTION_SPANISH)

        # Global layout elements (outside of frame)
        self.device_li = self.page.locator(HomePageLocators.DEVICE_LI)
        self.body_index = self.frame.locator(HomePageLocators.BODY_INDEX)
        self.header_div = self.page.locator(HomePageLocators.HEADER_DIV)
        self.hide_header_span = self.page.locator(HomePageLocators.HIDE_HEADER_SPAN)
        self.start_now_button = self.page.locator(HomePageLocators.START_NOW_BUTTON)
        self.explore_bo_button = self.page.locator(HomePageLocators.EXPLORE_BO_BUTTON)

        # Subscription and banner
        self.banner_image = self.frame.locator(HomePageLocators.BANNER_IMAGE)
        self.subscribe_input = self.frame.locator(HomePageLocators.SUBSCRIBE_INPUT)
        self.subscribe_button = self.frame.locator(HomePageLocators.SUBSCRIBE_BUTTON)
        self.subscribe_info_para = self.frame.locator(HomePageLocators.SUBSCRIBE_INFO_PARA)

        # Footer section
        self.footer_info_para = self.frame.locator(HomePageLocators.FOOTER_INFO_PARA)
        self.footer_section_title = self.frame.locator(HomePageLocators.FOOTER_SECTION_TITLE)
        self.footer_products_submenu_items = self.frame.locator(HomePageLocators.FOOTER_PRODUCTS_SUBMENU_ITEMS)
        self.footer_our_company_submenu_items = self.frame.locator(HomePageLocators.FOOTER_OUR_COMPANY_SUBMENU_ITEMS)
        self.footer_your_account_submenu_items = self.frame.locator(HomePageLocators.FOOTER_YOUR_ACCOUNT_SUBMENU_ITEMS)
        self.footer_store_info_submenu_items = self.frame.locator(HomePageLocators.FOOTER_STORE_INFO_SUBMENU_ITEMS)


    def go_to_homepage(self):
        """
        Navigate to the homepage and wait for essential elements to become visible.
        Ensures the page is fully loaded before any interaction.
        """
        self.visit("https://demo.prestashop.com/#/en/front") 
        self.frame.locator(HomePageLocators.CONTACT_LINK).wait_for(state="visible")
        self.frame.locator(HomePageLocators.MY_STORE_IMG).wait_for(state="visible")
        self.frame.locator(HomePageLocators.CLOTHES_LINK).wait_for(state="visible")
        self.frame.locator(HomePageLocators.LANGUAGE_DROPDOWN_BUTTON).wait_for(state="visible")

    def get_footer_submenu_texts(self, submenu_locator):
        """
        Return all visible text values from a given footer submenu locator.

        Args:
            submenu_locator (Locator): A Playwright locator object representing the submenu.

        Returns:
            list: List of text strings from submenu items.
        """
        return submenu_locator.all_inner_texts()

    def get_footer_store_info_text(self):
        """
        Retrieve the text content of the store information section in the footer.

        Returns:
            str: The inner text of the store info block.
        """
        return self.footer_store_info_submenu_items.inner_text()


    

    




