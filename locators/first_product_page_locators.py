class FirstProductPageLocators:
    """
    CSS selectors for locating UI elements on the First Product page.
    Used in the ArtPage Page Object.
    """

    # -------------------------------
    # Product information section
    # -------------------------------
    CONTENT_DIV_HEADER = 'div#content-wrapper h1'
    CURRENT_PRICE_SPAN = 'span.current-price-value'
    DESCRIPTION_SHORT_PARA = 'div#product-description-short-1 p'
    DESCRIPTION_LONG_PARA = 'div#description p'
    PRODUCT_DETAILS_LINK = 'a[aria-controls="product-details"]'
    COMPOSITION_NAME = 'dt.name'
    COMPOSITION_VALUE = 'dd.value'

    # -------------------------------
    # Product variants (size & color)
    # -------------------------------
    SIZE_SPAN = 'div.clearfix.product-variants-item span'
    SIZE_SELECT = 'select#group_1'
    COLOR_VARIANT_SPAN = 'div.clearfix.product-variants-item span.control-label'
    COLOR_BLACK_INPUT = 'input[title="Black"]'

    # -------------------------------
    # Quantity & add to cart
    # -------------------------------
    QUANTITY_LABEL = 'div.product-add-to-cart span.control-label'
    ADD_TO_CART_BUTTON = 'button.add-to-cart'

    # -------------------------------
    # Social sharing & reassurance
    # -------------------------------
    SOCIAL_SHARING_SPAN = 'div.social-sharing span'
    REASSURANCE_DIV = 'div.blockreassurance_product'
    
    # -------------------------------
    # Quick view modal
    # -------------------------------
    QUICK_VIEW_LINK= 'article[data-id-product="1"] a[data-link-action="quickview"]'
    MODAL_BODY_H1 = 'div.modal-body h1'
    CART_SUCCESS_MESSAGE = 'h4#myModalLabel'
    CONTINUE_SHOPPING_BUTTON = 'div.cart-content-btn button'
    CHECKOUT_LINK = 'div.cart-content-btn a'

    # -------------------------------
    # Modal product details
    # -------------------------------
    MODAL_PRODUCT_NAME = 'div.col-md-6 h6'
    MODAL_PRODUCT_PRICE = 'div.col-md-6 p.product-price'
    MODAL_PRODUCT_SIZE = 'div.col-md-6 span.size'
    MODAL_PRODUCT_COLOR = 'div.col-md-6 span.color'
    MODAL_PRODUCT_QUANTITY = 'div.col-md-6 span.product-quantity'

    # -------------------------------
    # Modal cart summary
    # -------------------------------
    MODAL_PRODUCT_COUNT_INFO = 'div.col-md-7 p.cart-products-count'
    MODAL_SUBTOTAL_VALUE = 'div.col-md-7 span.subtotal.value'
    MODAL_SHIPPING_VALUE = 'div.col-md-7 span.shipping.value'
    MODAL_TOTAL_VALUE = 'div.col-md-7 p.product-total span.value'

