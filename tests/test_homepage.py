from pages.home_page import HomePage

def test_homepage_title_and_url(page):
    home = HomePage(page)
    home.go_to_homepage()

    home.assert_url_is("https://demo.prestashop.com/#/en/front")
    home.assert_title_is("PrestaShop Live Demo")
