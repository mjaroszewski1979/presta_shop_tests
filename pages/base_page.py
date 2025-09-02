from playwright.sync_api import Page

class BasePage:
    """
    Base class for all Page Object Models.

    Encapsulates common actions and assertions used across all page classes,
    such as navigation, visibility checks, content assertions, and interactions with DOM elements.
    Provides a consistent and reusable interface to interact with Playwright's Page API.
    """

    def __init__(self, page: Page):
        """
        Initialize the BasePage with the current Playwright page context.
        Exposes direct access to the main page instance and default iframe.

        Args:
            page (playwright.sync_api.Page): Playwright page object for browser interaction.
        """
        self.page = page # Reference to the current Playwright page context

        # -------------------------------
        # Default iframe reference for pages rendered inside '#framelive'
        # Centralized here to reduce code duplication across child classes
        # -------------------------------
        self.frame = page.frame_locator("#framelive")

    def visit(self, url: str):
        """
        Navigate to a specified URL.

        Args:
            url (str): The target URL to open in the browser.
        """
        self.page.goto(url) 

    def wait_for_visible(self, selector: str, timeout: int = 10000):
        """
        Wait until a specific element becomes visible on the page.

        Args:
            selector (str): CSS or XPath selector of the target element.
            timeout (int, optional): Maximum wait time in ms (default is 10 seconds).
        """
        self.page.locator(selector).wait_for(state="visible", timeout=timeout) 

    def get_title(self) -> str:
        """
        Retrieve the current page title.

        Returns:
            str: The browser tab/page title.
        """
        return self.page.title() 

    def get_url(self) -> str:
        """
        Retrieve the current page URL.

        Returns:
            str: The URL of the active page.
        """
        return self.page.url 

    def click(self, selector: str):
        """
        Click on an element located by a selector.

        Args:
            selector (str): CSS or XPath selector of the element to click.
        """
        self.page.click(selector) 

    def fill(self, selector: str, text: str):
        """
        Fill an input field with the provided text.

        Args:
            selector (str): CSS or XPath selector of the input element.
            text (str): Text to be entered into the field.
        """
        self.page.fill(selector, text) 

    def get_text(self, selector: str) -> str:
        """
        Retrieve the inner text of a given element.

        Args:
            selector (str): CSS or XPath selector of the element.

        Returns:
            str: Inner text value of the element.
        """
        return self.page.inner_text(selector) 

    def is_visible(self, selector: str) -> bool: 
        """
        Check if an element is currently visible on the page.

        Args:
            selector (str): CSS or XPath selector of the element.

        Returns:
            bool: True if element is visible, False otherwise.
        """
        return self.page.is_visible(selector) 

    def wait_for_selector(self, selector: str):
        """
        Wait until a specific element is present in the DOM.

        Args:
            selector (str): CSS or XPath selector of the element.
        """
        self.page.wait_for_selector(selector)

    def assert_text(self, selector: str, expected_text: str):
        """
        Assert that an element's inner text matches the expected value.

        Args:
            selector (str): CSS or XPath selector of the element.
            expected_text (str): Expected text value.

        Raises:
            AssertionError: If actual text does not match expected text.
        """
        self.wait_for_visible(selector)
        actual = self.get_text(selector)
        assert actual == expected_text, f"Expected '{expected_text}', got '{actual}'" 

    def assert_title_is(self, expected_title: str):
        """
        Assert that the current page title matches the expected value.

        Args:
            expected_title (str): The expected browser tab/page title.

        Raises:
            AssertionError: If the actual title does not match.
        """
        actual_title = self.get_title()
        assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'" 

    def assert_url_is(self, expected_url: str):
        """
        Assert that the current page URL matches the expected value.

        Args:
            expected_url (str): The expected page URL.

        Raises:
            AssertionError: If the actual URL does not match.
        """
        actual_url = self.get_url()
        assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'" 

    
