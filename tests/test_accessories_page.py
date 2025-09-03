# Import Playwright's 'expect' for advanced assertions and waiting conditions.
from playwright.sync_api import expect

# Import custom utility function to assert visibility and text of multiple elements.
from utils.assertions import assert_element_visible_with_text


def test_ceramic_checkbox_filter_works(home_page, accessories_home_page):
    """
    Validates that the ceramic checkbox filter works by verifying that the list
    of products updates after the filter is applied.

    Args:
        home_page: Page object representing the home page with navigation locators.
        accessories_home_page: Page object representing the accessories home page
                               with filter locators and product list elements.

    Steps:
        1. Wait for the Accessories link to become visible.
        2. Hover over the Accessories link to display its submenu.
        3. Click on the Accessories Home link.
        4. Select the Ceramic checkbox filter.
        5. Assert that the product list updates and displays the expected text.
    """
    home_page.accessories_link.wait_for(state="visible", timeout=10000)
    home_page.accessories_link.hover()
    home_page.accessories_home_link.click()
    accessories_home_page.ceramic_checkbox.check()
    assert_element_visible_with_text(accessories_home_page.product_list_para, 'There are 4 products.')



    




