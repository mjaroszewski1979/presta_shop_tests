from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url)

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        return self.page.inner_text(selector)

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    def wait_for_selector(self, selector: str):
        self.page.wait_for_selector(selector)

    def assert_text(self, selector: str, expected_text: str):
        actual = self.get_text(selector)
        assert actual == expected_text, f"Expected '{expected_text}', got '{actual}'"
