from dataclasses import dataclass
from utils.home_page_utils import (
    generate_unique_email, 
    generate_password, 
    generate_first_name, 
    generate_last_name, 
    generate_birthdate,
    generate_company_name,
    generate_vat_number,
    generate_postal_code,
    generate_street_address,
    generate_city_name,
    generate_phone_number
)

@dataclass
class UserData:
    first_name: str
    last_name: str
    email: str
    password: str
    birthday: str
    address: str
    company: str
    vat: str
    city: str
    postcode: str
    phone: str

    @classmethod
    def generate_valid(cls):
        return cls(
            first_name = generate_first_name(),
            last_name = generate_last_name(),
            email = generate_unique_email(),
            password = generate_password(),
            birthday = generate_birthdate(),
            address = generate_street_address(),
            company = generate_company_name(),
            vat = generate_vat_number(),
            city = generate_city_name(),
            postcode = generate_postal_code(),
            phone = generate_phone_number()
        )
