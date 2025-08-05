def get_first_product_data(first_product_page):
    """
    Returns a list of tuples mapping each label element in the 'Contact' form
    to its expected display text. This is used to validate that form labels are 
    visible and contain correct content.

    Args:
        contact_page: An instance of the ContactPage with form label locators.

    Returns:
        list[tuple]: A list of (locator, expected_text) pairs for label verification.
    """
    return [
        (first_product_page.content_div_header, "Hummingbird printed t-shirt"),
        (first_product_page.current_price_span, "€22.94"),
        (first_product_page.description_short_para.first, "Regular fit, round neckline, short sleeves. Made of extra long staple pima cotton. "),
        (first_product_page.size_span.first, "Size: S"),
        (first_product_page.color_variant_span.nth(1), "Color: White"),
        (first_product_page.quantity_label, "Quantity"),
        (first_product_page.social_sharing_span, "Share"),
        (first_product_page.reassurance_div, "Security policy (edit with the Customer Reassurance module) Delivery policy (edit with the Customer Reassurance module) Return policy (edit with the Customer Reassurance module)"),
        (first_product_page.description_long_para, "Symbol of lightness and delicacy, the hummingbird evokes curiosity and joy."),
        (first_product_page.add_to_cart_button, "Add to cart"),
    ]
