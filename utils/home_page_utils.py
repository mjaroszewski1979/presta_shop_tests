from faker import Faker

fake = Faker()

def generate_unique_email(domain="gmail.com") -> str:
    username = fake.user_name()
    return f"{username}@{domain}"
