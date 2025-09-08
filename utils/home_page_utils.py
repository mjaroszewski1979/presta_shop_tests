from faker import Faker
import random
import string

# Import Playwright assertions
from playwright.sync_api import expect

# Initialize Faker instance for generating fake data
fake = Faker()

def generate_unique_email(domain="gmail.com") -> str:
    """
    Generates a unique email address using Faker's username generator.

    Args:
        domain (str): The email domain to append. Defaults to "gmail.com".

    Returns:
        str: A unique email address in the format '<username>@<domain>'.
    """
    
    username = fake.user_name()
    return f"{username}@{domain}"

def generate_first_name() -> str:
    """
    Generates a realistic fake first name.
    """
    return fake.first_name()

def generate_last_name() -> str:
    """
    Generates a realistic fake last name.
    """
    return fake.last_name()

def generate_password(min_len: int = 8, max_len: int = 72) -> str:
    """
    Generates a fake password within a given length range.

    Args:
        min_len (int): Minimum password length (default 8).
        max_len (int): Maximum password length (default 72).

    Returns:
        str: A password string containing letters, digits, and special characters.
    """
    if min_len < 8 or max_len > 72 or min_len > max_len:
        raise ValueError("Password length must be between 8 and 72 characters.")

    length = random.randint(min_len, max_len)
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))


def generate_random_message(min_length=50, max_length=100):
    target_length = random.randint(min_length, max_length)
    message = ''
    while len(message) < target_length:
        message += fake.sentence()
    return message[:target_length] 

def generate_birthdate(min_age=18, max_age=90) -> str:
    """
    Generates a random birthdate in the format 'dd/mm/yyyy'.

    Args:
        min_age (int): Minimum age of the generated person.
        max_age (int): Maximum age of the generated person.

    Returns:
        str: Random date string in 'dd/mm/yyyy' format.
    """
    # Losowy wiek w zakresie
    age = random.randint(min_age, max_age)
    birthdate = fake.date_of_birth(minimum_age=age, maximum_age=age)
    return birthdate.strftime("%d/%m/%Y")

def generate_company_name() -> str:
    """
    Generates a fake company name.
    """
    return fake.company()

def generate_vat_number(country_code="FR") -> str:
    """
    Generates a fake VAT number in the format 'FR12 345678901'.
    """
    prefix = country_code
    digits = ''.join(random.choices(string.digits, k=11))
    check_digits = ''.join(random.choices(string.digits, k=2))
    return f"{prefix}{check_digits} {digits}"

def generate_street_address() -> str:
    """
    Generates a fake street name with building number.
    """
    return fake.street_address()

def generate_postal_code() -> str:
    """
    Generates a fake postal code (5 digits).
    """
    return fake.postcode()

def generate_city_name() -> str:
    """
    Generates a fake city name.
    """
    return fake.city()

def generate_phone_number(digits=10) -> str:
    """
    Generates a fake phone number with a specific number of digits.
    """
    return ''.join(random.choices(string.digits, k=digits))

def type_text_into_input_field(locator, text):
    locator.wait_for(state="visible", timeout=15000)
    locator.clear()             
    locator.type(text)

def assert_footer_section(home_page, section_index, expected_title, expected_items, submenu_locator):
    """
    Utility function to validate footer section title and submenu items.

    Args:
        home_page: Page object with footer locators.
        section_index (int): Index of the footer section.
        expected_title (str): Title of the section to validate.
        expected_items (list|str): Expected submenu item(s).
        submenu_locator: Locator for submenu items.

    Steps:
        1. Locate the footer section by its index.
        2. Verify that the section title is visible and matches the expected title.
        3. If multiple submenu items are expected, compare all texts with the expected list.
        4. If only a single submenu item is expected, validate its text directly.
    """
    section_title = home_page.footer_section_title.nth(section_index)
    expect(section_title).to_be_visible()
    expect(section_title).to_have_text(expected_title)
    if isinstance(expected_items, list):
        actual_items = submenu_locator.all_inner_texts()
        assert actual_items == expected_items, f"Expected {expected_items}, but got {actual_items}"
    else:
        actual_item = submenu_locator.inner_text()
        assert actual_item == expected_items, f"Expected {expected_items}, but got {actual_item}"
