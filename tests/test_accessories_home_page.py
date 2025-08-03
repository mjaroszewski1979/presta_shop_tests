# Import Playwright's 'expect' for advanced assertions and waiting conditions.
from playwright.sync_api import expect

# Import custom utility function to assert visibility and text of multiple elements.
from utils.assertions import assert_element_visible_with_text





def test_ceramic_checkbox_filter_works(home_page, accessories_home_page):
    """
    Validates that the ceramic checkbox filter works - after performing check the list of products changes
    """
    home_page.accessories_link.wait_for(state="visible", timeout=10000)
    home_page.accessories_link.hover()
    home_page.accessories_home_link.wait_for(state="visible", timeout=10000)
    home_page.accessories_home_link.click()
    accessories_home_page.ceramic_checkbox.wait_for(state="visible", timeout=5000)
    accessories_home_page.ceramic_checkbox.check()
    assert_element_visible_with_text(accessories_home_page.product_list_para, 'There are 4 products.')



    




