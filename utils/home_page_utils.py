from faker import Faker
import random
import string

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
