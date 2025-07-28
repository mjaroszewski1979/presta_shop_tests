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
