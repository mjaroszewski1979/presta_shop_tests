class HomePageLocators:
    """
    A collection of CSS selectors for locating UI elements on the homepage.
    Used in the HomePage Page Object for Playwright-based E2E tests.
    """

    # Header and top navigation
    CONTACT_LINK = '#contact-link a'
    SIGN_IN_SPAN = 'a[title="Log in to your customer account"] span.hidden-sm-down'
    SIGN_OUT_LINK = 'div.user-info a.logout'
    CART_SPAN = 'div.header span.hidden-sm-down'
    MY_STORE_IMG = 'div#_desktop_logo img.img-fluid'

    # Main category links
    CLOTHES_LINK = 'li#category-3'
    CLOTHES_MEN_LINK = 'li#category-4'
    CLOTHES_WOMEN_LINK = 'li#category-5'
    ACCESSORIES_LINK = 'li#category-6'
    ACCESSORIES_STATIONERY_LINK = 'li#category-7'
    ACCESSORIES_HOME_LINK = 'li#category-8'
    ART_LINK = 'li#category-9'

    # Featured and sale products
    FEATURED_PRODUCTS = 'section.featured-products div.products.row div.js-product.product'
    FEATURED_PRODUCTS_H2 = 'section.featured-products h2'
    SALE_PRODUCTS = 'section.featured-products.clearfix.mt-3 div.products div.js-product.product'

    # Carousel section
    CAROUSEL_HEADINGS = 'ul.carousel-inner li.carousel-item h2.display-1.text-uppercase'
    CAROUSEL_NEXT_ICON = 'span.icon-next'

    # Search and language
    SEARCH_CATALOG_INPUT = 'input.ui-autocomplete-input'
    LANGUAGE_DROPDOWN_BUTTON = 'div.language-selector button.hidden-sm-down'
    LANGUAGE_OPTION_SPANISH = 'a.dropdown-item[data-iso-code="es"]'

    # Device view switcher (responsive UI testing)
    DEVICE_LI = 'ul#devices li a'
    BODY_INDEX = 'body#index'
    HEADER_DIV = 'div#header'
    HIDE_HEADER_SPAN = 'span.hide-header'

    # CTA buttons
    START_NOW_BUTTON = 'div#buttons a.btn-download'
    EXPLORE_BO_BUTTON = 'div#buttons a.btn-explore-bo'

    # Banner and newsletter subscription
    BANNER_IMAGE = 'a.banner img.img-fluid'
    SUBSCRIBE_INPUT = 'div.input-wrapper input'
    SUBSCRIBE_BUTTON = 'input.btn.btn-primary.float-xs-right.hidden-xs-down'
    SUBSCRIBE_INFO_PARA = 'p.alert.alert-success.block_newsletter_alert'

    # Footer content and submenu sections
    FOOTER_INFO_PARA = 'div.footer-container p.hidden-sm-down'
    FOOTER_SECTION_TITLE = "div.footer-container p.hidden-sm-down"
    FOOTER_PRODUCTS_SUBMENU_ITEMS = "ul#footer_sub_menu_1 li"
    FOOTER_OUR_COMPANY_SUBMENU_ITEMS = "ul#footer_sub_menu_2 li"
    FOOTER_YOUR_ACCOUNT_SUBMENU_ITEMS = "ul#footer_account_list li"
    FOOTER_STORE_INFO_SUBMENU_ITEMS = "div#contact-infos"

