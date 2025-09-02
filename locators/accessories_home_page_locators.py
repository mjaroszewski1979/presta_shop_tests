class AccessoriesHomePageLocators:
    """
    Collection of CSS selectors for the Accessories home page.

    These locators are used to identify and interact with UI elements
    specific to the Accessories section, typically referenced in the 
    corresponding Page Object (e.g., SearchPage).
    """

    # Paragraph element showing product count above the product listing
    PRODUCT_LIST_PARA = 'div#js-product-list-top p'

    # Checkbox filter option for selecting products made of Ceramic
    CERAMIC_CHECKBOX = 'input[data-search-url*="Composition-Ceramic"]'