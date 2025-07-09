from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.contact_link = HomePageLocators.CONTACT_LINK


    def go_to_homepage(self):
        self.visit("https://demo.prestashop.com/#/en/front") 
