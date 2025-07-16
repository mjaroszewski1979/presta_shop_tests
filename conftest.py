import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.contact_page import ContactPage
from pages.sign_page import SignPage
from pages.search_page import SearchPage
from pages.clothes_page import ClothesPage

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

@pytest.fixture
def contact_page(page):
    contact = ContactPage(page)
    return contact

@pytest.fixture
def sign_page(page):
    sign = SignPage(page)
    return sign

@pytest.fixture
def search_page(page):
    search = SearchPage(page)
    return search

@pytest.fixture
def clothes_page(page):
    clothes = ClothesPage(page)
    return clothes
