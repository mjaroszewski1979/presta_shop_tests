class FirstProductPageLocators:
    """
    CSS selectors for locating UI elements on the First Product page.
    Used in the ArtPage Page Object.
    """
    CONTENT_DIV_HEADER = 'div#content-wrapper h1'
    CURRENT_PRICE_SPAN = 'span.current-price-value'
    DESCRIPTION_SHORT_PARA = 'div#product-description-short-1 p'
    SIZE_SPAN = 'div.clearfix.product-variants-item span'
    SIZE_SELECT = 'select#group_1'
    COLOR_VARIANT_SPAN = 'div.clearfix.product-variants-item span.control-label'
    COLOR_BLACK_INPUT = 'input[title="Black"]'
    QUANTITY_LABEL = 'div.product-add-to-cart span.control-label'
    SOCIAL_SHARING_SPAN = 'div.social-sharing span'
    REASSURANCE_DIV = 'div.blockreassurance_product'
    DESCRIPTION_LONG_PARA = 'div#description p'
    PRODUCT_DETAILS_LINK = 'a[aria-controls="product-details"]'
    COMPOSITION_NAME = 'dt.name'
    COMPOSITION_VALUE = 'dd.value'
    ADD_TO_CART_BUTTON = 'button.add-to-cart'
    QUICK_VIEW_LINK= 'article[data-id-product="1"] a[data-link-action="quickview"]'
    MODAL_BODY_H1 = 'div.modal-body h1'