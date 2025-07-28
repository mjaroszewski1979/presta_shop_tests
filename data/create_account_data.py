def get_create_account_label_data(create_account_page):
    return [
        (create_account_page.form_labels.nth(0), "Social title"),
        (create_account_page.form_labels.nth(1), "First name"),
        (create_account_page.form_labels.nth(2), "Last name"),
        (create_account_page.form_labels.nth(3), "Email"),
        (create_account_page.form_labels.nth(4), "Password"),
        (create_account_page.form_labels.nth(5), "Birthdate"),
    ]
