from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)


    def go_to_homepage(self):
        self.visit("https://demo.prestashop.com/#/en/front") 
