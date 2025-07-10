from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.frame = page.frame_locator("#framelive")
        self.contact_link = self.frame.locator(HomePageLocators.CONTACT_LINK)
        self.sign_in_span = self.frame.locator(HomePageLocators.SIGN_IN_SPAN)
        self.cart_span = self.frame.locator(HomePageLocators.CART_SPAN)
        self.featured_products = self.frame.locator(HomePageLocators.FEATURED_PRODUCTS)


    def go_to_homepage(self):
        self.visit("https://demo.prestashop.com/#/en/front") 
        self.page.wait_for_load_state("networkidle")
        self.frame.locator(HomePageLocators.CONTACT_LINK).wait_for(state="visible")

