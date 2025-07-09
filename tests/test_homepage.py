

def test_homepage_title(home_page):
    home_page.assert_title_is("PrestaShop Live Demo")

def test_homepage_url(home_page):
    home_page.assert_url_is("https://demo.prestashop.com/#/en/front")

def test_contact_link_is_visible_with_text(home_page):
    home_page.is_visible_with_text(home_page.contact_link, 'Contact us')
