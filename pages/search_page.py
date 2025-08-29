from pages.base_page import BasePage
from locators.search_page_locators import SearchPageLocators

class SearchPage(BasePage):
    """
    Page Object Model (POM) representation of the Search Results page.

    Provides access to search result-specific elements and interactions.
    The main content is rendered inside the '#framelive' iframe.
    Inherits browser actions, assertions, and utility methods from BasePage.
    """
    
    def __init__(self, page):
        """
        Initialize the SearchPage with page context and locate all relevant 
        UI elements specific to the search results page.

        Args:
            page (playwright.sync_api.Page): Playwright page object for browser interaction.
        """
        super().__init__(page)

        # -------------------------------
        # Locate iframe containing search results content
        # -------------------------------
        self.frame = page.frame_locator("#framelive")

        # -------------------------------
        # Search results summary elements
        # -------------------------------
        self.total_products_para = self.frame.locator(SearchPageLocators.TOTAL_PRODUCTS_PARA)