from pages.base_page import BasePage
from locators.accessories_page_locators import AccessoriesPageLocators

class AccessoriesPage(BasePage):
    """
    Page Object Model (POM) representation of the Accessories category page.

    Encapsulates locators and interactions specific to the Accessories page,
    which is displayed inside an iframe identified by '#framelive'.
    Inherits navigation, interaction, and assertion functionality from BasePage.
    """

    def __init__(self, page):
        """
        Initialize the AccessoriesPage with page context and locate all relevant
        UI elements for the Accessories category view.

        Args:
            page (playwright.sync_api.Page): Playwright page object for browser interaction.
        """
        super().__init__(page)

        # -------------------------------
        # Locate iframe containing Accessories page content
        # -------------------------------
        self.frame = page.frame_locator("#framelive")

        # -------------------------------
        # Accessories category header
        # -------------------------------
        self.accessories_div_header = self.frame.locator(AccessoriesPageLocators.ACCESSORIES_DIV_HEADER)