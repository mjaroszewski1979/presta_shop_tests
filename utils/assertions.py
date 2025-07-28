from playwright.sync_api import expect

def assert_element_visible_with_text(locator, expected_text: str, timeout: int = 5000):
    """
    Asserts that the locator is visible and contains the expected text.

    :param locator: Playwright Locator object.
    :param expected_text: Text expected to be found in the element.
    :param timeout: Optional timeout in milliseconds (default 5000ms).
    """
    locator.wait_for(state="visible", timeout=timeout)
    expect(locator).to_contain_text(expected_text)

def assert_elements_visible_with_texts(locators_and_texts: list[tuple], timeout: int = 5000):
    """
    Asserts that multiple locators are visible and contain expected texts.
    
    :param locators_and_texts: List of tuples (locator, expected_text)
    :param timeout: Timeout for visibility (default 5000ms)
    """
    for locator, expected_text in locators_and_texts:
        locator.wait_for(state="visible", timeout=timeout)
        expect(locator).to_contain_text(expected_text)
