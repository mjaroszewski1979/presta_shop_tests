from faker import Faker

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
