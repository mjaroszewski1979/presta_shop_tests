from pages.base_page import BasePage
from locators.art_page_locators import ArtPageLocators

class ArtPage(BasePage):
    """
    Page Object Model (POM) representation of the Art category page.

    Encapsulates locators and interactions specific to the Art category view.
    The page content is embedded inside an iframe identified by '#framelive'.
    Inherits navigation, interaction, and assertion utilities from BasePage.
    """
    
    def __init__(self, page):
        """
        Initialize the ArtPage with page context and locate all relevant
        UI elements for the Art category section.

        Args:
            page (playwright.sync_api.Page): Playwright page object for browser interaction.
        """
        super().__init__(page)

        # -------------------------------
        # Locate iframe containing Art page content
        # -------------------------------
        self.frame = page.frame_locator("#framelive")

        # -------------------------------
        # Art category header element
        # -------------------------------
        self.art_div_header = self.frame.locator(ArtPageLocators.ART_DIV_HEADER)