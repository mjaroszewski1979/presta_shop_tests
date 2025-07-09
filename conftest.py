import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage

@pytest.fixture(scope="session")
def playwright_context():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_context):
    browser = playwright_context.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def home_page(page):
    home = HomePage(page)
    home.go_to_homepage()
    return home
