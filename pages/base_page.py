from playwright.sync_api import Page, expect

class BasePage:
    """
    Base class for all Page Object Models.

    Encapsulates common actions and assertions used across all page classes,
    such as navigation, visibility checks, content assertions, and interactions with DOM elements.
    Provides a consistent and reusable interface to interact with Playwright's Page API.
    """

    def __init__(self, page: Page):
        self.page = page # Reference to the current Playwright page context

    def visit(self, url: str):
        self.page.goto(url) # Navigate to the specified URL

    def wait_for_visible(self, selector: str, timeout: int = 10000):
        self.page.locator(selector).wait_for(state="visible", timeout=timeout) # Wait until the element becomes visible

    def get_title(self) -> str:
        return self.page.title() # Return the current page title

    def get_url(self) -> str:
        return self.page.url # Return the current page URL

    def click(self, selector: str):
        self.page.click(selector) # Click on an element by its selector

    def fill(self, selector: str, text: str):
        self.page.fill(selector, text) # Fill a form input with the given text

    def get_text(self, selector: str) -> str:
        return self.page.inner_text(selector) # Return inner text of the specified element

    def is_visible(self, selector: str) -> bool: 
        return self.page.is_visible(selector) # Check whether the element is visible on the page

    def wait_for_selector(self, selector: str):
        self.page.wait_for_selector(selector) # Wait for the element to be present in the DOM

    def assert_text(self, selector: str, expected_text: str):
        self.wait_for_visible(selector)
        actual = self.get_text(selector)
        assert actual == expected_text, f"Expected '{expected_text}', got '{actual}'" # Assert exact text match

    def assert_title_is(self, expected_title: str):
        actual_title = self.get_title()
        assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'" # Assert page title matches expected

    def assert_url_is(self, expected_url: str):
        actual_url = self.get_url()
        assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'" # Assert URL matches expected

    
