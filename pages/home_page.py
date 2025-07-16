from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.contact_link = self.frame.locator(HomePageLocators.CONTACT_LINK)
        self.sign_in_span = self.frame.locator(HomePageLocators.SIGN_IN_SPAN)
        self.cart_span = self.frame.locator(HomePageLocators.CART_SPAN)
        self.my_store_img = self.frame.locator(HomePageLocators.MY_STORE_IMG)
        self.clothes_link = self.frame.locator(HomePageLocators.CLOTHES_LINK)
        self.clothes_men_link = self.frame.locator(HomePageLocators.CLOTHES_MEN_LINK)
        self.clothes_women_link = self.frame.locator(HomePageLocators.CLOTHES_WOMEN_LINK)
        self.accessories_link = self.frame.locator(HomePageLocators.ACCESSORIES_LINK)
        self.accessories_stationery_link = self.frame.locator(HomePageLocators.ACCESSORIES_STATIONERY_LINK)
        self.accessories_home_link = self.frame.locator(HomePageLocators.ACCESSORIES_HOME_LINK)
        self.art_link = self.frame.locator(HomePageLocators.ART_LINK)
        self.featured_products = self.frame.locator(HomePageLocators.FEATURED_PRODUCTS)
        self.featured_products_h2 = self.frame.locator(HomePageLocators.FEATURED_PRODUCTS_H2)
        self.sale_products = self.frame.locator(HomePageLocators.SALE_PRODUCTS)
        self.carousel_headings = self.frame.locator(HomePageLocators.CAROUSEL_HEADINGS)
        self.carousel_next_icon = self.frame.locator(HomePageLocators.CAROUSEL_NEXT_ICON)
        self.search_catalog_input = self.frame.locator(HomePageLocators.SEARCH_CATALOG_INPUT)
        self.language_dropdown_button = self.frame.locator(HomePageLocators.LANGUAGE_DROPDOWN_BUTTON)
        self.language_option_spanish = self.frame.locator(HomePageLocators.LANGUAGE_OPTION_SPANISH)
        self.device_li = self.page.locator(HomePageLocators.DEVICE_LI)
        self.body_index = self.frame.locator(HomePageLocators.BODY_INDEX)
        self.header_div = self.page.locator(HomePageLocators.HEADER_DIV)
        self.hide_header_span = self.page.locator(HomePageLocators.HIDE_HEADER_SPAN)
        self.start_now_button = self.page.locator(HomePageLocators.START_NOW_BUTTON)
        self.explore_bo_button = self.page.locator(HomePageLocators.EXPLORE_BO_BUTTON)


    def go_to_homepage(self):
        self.visit("https://demo.prestashop.com/#/en/front") 
        self.frame.locator(HomePageLocators.CONTACT_LINK).wait_for(state="visible")
        self.frame.locator(HomePageLocators.MY_STORE_IMG).wait_for(state="visible")
        self.frame.locator(HomePageLocators.CLOTHES_LINK).wait_for(state="visible")
        self.frame.locator(HomePageLocators.LANGUAGE_DROPDOWN_BUTTON).wait_for(state="visible")

    




