import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.contact_page import ContactPage
from pages.sign_page import SignPage
from pages.search_page import SearchPage
from pages.clothes_page import ClothesPage
from pages.accessories_page import AccessoriesPage
from pages.art_page import ArtPage

# ----------- Playwright Fixtures -----------

@pytest.fixture(scope="session")
def playwright_context():
    """
    Creates a Playwright context for the test session.
    Ensures Playwright is initialized once per test session.
    """
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_context):
    """
    Launches a Chromium browser instance in headless mode.
    This fixture is shared across all tests within the session.
    """
    browser = playwright_context.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    """
    Provides a new browser context and page for each test function.
    Ensures test isolation and automatic cleanup after execution.
    """
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

# ----------- Page Object Fixtures -----------

@pytest.fixture
def home_page(page):
    """
    Initializes the HomePage object and navigates to the homepage.
    Returns:
        HomePage: An instance of the HomePage POM.
    """
    home = HomePage(page)
    home.go_to_homepage()
    return home

@pytest.fixture
def contact_page(page):
    """
    Initializes the ContactPage object without additional setup.
    Returns:
        ContactPage: An instance of the ContactPage POM.
    """
    contact = ContactPage(page)
    return contact

@pytest.fixture
def sign_page(page):
    """
    Initializes the SignPage object for authentication-related tests.
    Returns:
        SignPage: An instance of the SignPage POM.
    """
    sign = SignPage(page)
    return sign

@pytest.fixture
def search_page(page):
    """
    Initializes the SearchPage object for search result assertions.
    Returns:
        SearchPage: An instance of the SearchPage POM.
    """
    search = SearchPage(page)
    return search

@pytest.fixture
def clothes_page(page):
    """
    Initializes the ClothesPage object for accessing clothing category views.
    Returns:
        ClothesPage: An instance of the ClothesPage POM.
    """
    clothes = ClothesPage(page)
    return clothes

@pytest.fixture
def accessories_page(page):
    """
    Initializes the AccessoriesPage object for accessory-related test cases.
    Returns:
        AccessoriesPage: An instance of the AccessoriesPage POM.
    """
    accessories = AccessoriesPage(page)
    return accessories

@pytest.fixture
def art_page(page):
    """
    Initializes the ArtPage object for tests involving the art category.
    Returns:
        ArtPage: An instance of the ArtPage POM.
    """
    art = ArtPage(page)
    return art
