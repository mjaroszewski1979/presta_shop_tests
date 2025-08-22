from dataclasses import dataclass
from utils.home_page_utils import (
    generate_unique_email,
    generate_first_name,
    generate_last_name,
    generate_password,
    generate_birthdate
)

@dataclass
class UserData:
    first_name: str
    last_name: str
    email: str
    password: str
    birthday: str

    @classmethod
    def generate_valid(cls):
        return cls(
            first_name=generate_first_name(),
            last_name=generate_last_name(),
            email=generate_unique_email(),
            password=generate_password(),
            birthday=generate_birthdate()
        )
