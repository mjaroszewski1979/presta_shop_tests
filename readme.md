![caption](https://github.com/mjaroszewski1979/presta_shop_tests/blob/main/presta_shop_tests_img.jpg)

# E-Commerce Web App Test Automation – Presta Shop

### This project contains a suite of automated end-to-end (E2E) tests for a sample e-commerce web application using Playwright and Python.

#### The goal of this project is to implement a maintainable, scalable, and professional-grade test automation framework. It follows the Page Object Model (POM) design pattern and uses a clearly defined folder structure to ensure modularity and separation of concerns. This approach simplifies maintenance, improves readability, and allows seamless integration of future modules or extensions.

## Features
* Pytest Integration – Built with pytest for clean, readable, and maintainable test syntax.
* Page Object Model (POM) – All tests follow the Page Object Model design pattern for modularity, reusability, and scalability.
* Shared BasePage Class – Centralizes common browser actions and reduces code duplication across page objects.
* Locators Folder – Dedicated locators/ directory storing logically grouped selectors associated with each page object.
* Models for Test Data – A models/ folder containing a user_data module for generating user objects. This allows smooth sharing and reusability of dynamically created user data across multiple test modules.
* Data Modules for UI Validation – The data/ folder contains modules defining structured mappings of locators to expected UI values (e.g., verifying product details on the first product page).
* Pytest Fixtures – Defined in conftest.py to initialize and provide page object instances to test functions, ensuring clean test setup and reusability.
* Utility Layer – A utils/ package with helper modules:
  * assertions.py: Provides reusable assertion helpers, such as checking element visibility and verifying multiple locators with expected text.
  * home_page_utils.py: Offers dynamic test data generation using Faker (e.g., unique emails, realistic names, passwords, messages, and birthdates).
* Extensible Framework – Designed to be easily extended with new pages, locators, models, or utilities as the application grows.

## Local Installation
1. Clone the repository
```bash
git clone https://github.com/mjaroszewski1979/presta_shop_tests.git
cd presta_shop_tests
```

2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run tests

To run all E2E tests:

```bash
pytest
```

5. To generate a Playwright HTML report:

```bash
pytest --html=report.html --self-contained-html
```

## Folder Structure
```bash
playwright-python-shop/
├── data/                  # Test data modules for UI validation
│   ├── cart_data.py
│   ├── contact_data.py
│   ├── create_account_data.py
│   ├── first_product_data.py
│   ├── home_page_data.py
│   └── sign_data.py
│
├── locators/              # Page-specific locators organized by UI component
│   ├── accessories_home_page_locators.py
│   ├── accessories_page_locators.py
│   ├── art_page_locators.py
│   ├── cart_page_locators.py
│   ├── clothes_page_locators.py
│   ├── contact_page_locators.py
│   ├── create_account_page_locators.py
│   ├── first_product_page_locators.py
│   ├── home_page_locators.py
│   ├── search_page_locators.py
│   └── sign_page_locators.py
│
├── models/                # Data models for test objects
│   └── user_data.py
│
├── pages/                 # Page Object Model (POM) classes
│   ├── accessories_home_page.py
│   ├── accessories_page.py
│   ├── art_page.py
│   ├── base_page.py
│   ├── cart_page.py
│   ├── clothes_page.py
│   ├── contact_page.py
│   ├── create_account_page.py
│   ├── first_product_page.py
│   ├── home_page.py
│   ├── search_page.py
│   └── sign_page.py
│
├── tests/                 # Pytest test cases
│   ├── test_accessories_page.py
│   ├── test_cart_page.py
│   ├── test_contact_page.py
│   ├── test_create_account_page.py
│   ├── test_first_product_page.py
│   ├── test_homepage.py
│   └── test_sign_page.py
│
├── utils/                 # Utility functions and helpers
│   ├── assertions.py
│   └── home_page_utils.py
│
├── conftest.py            # Pytest fixtures configuration
├── pytest.ini             # Pytest settings
├── requirements.txt       # Python dependencies
├── readme.md              # Project documentation
```

## Technologies Used
* Playwright – Framework for end-to-end browser automation across Chromium, Firefox, and WebKit.
* Python – Main programming language used to implement the test framework.
* Pytest – Testing framework providing clean syntax, fixtures, and reporting capabilities.
* VS Code – Recommended IDE with seamless integration for Python development and Playwright testing.

## Contributing
Fork the repository.

Create a new branch:
```
git checkout -b feature-branch
```

Make your changes and commit:
```
git commit -m 'Add new feature'
```

Push to your branch:
```
git push origin feature-branch
```

Open a pull request.

## Contact
#### For questions or feedback, please contact mjaroszewski1979 on GitHub.

