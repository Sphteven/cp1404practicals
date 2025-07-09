"""
emails
Estimate: 45 minutes
Actual:   60 minutes
"""


def main():
    """Loop until user inputs an empty value then it will print list."""
    name_to_email = {}
    emails = []
    email = get_email()
    while email != "":
        full_name = convert_email_to_name(email)
        emails.append(email)
        if check_if_name(full_name) is False:
            full_name = input("Name: ").title()
        name_to_email[full_name] = email
        email = get_email()
    for name, email in name_to_email.items():
        print(f"{name} ({email})")


def get_email():
    """Get email from user"""
    email = input("Email: ")
    return email


def convert_email_to_name(email):
    """Split string into wanted full name strings and returns it."""
    first_iterate = email.split("@")[0]
    second_iterate = first_iterate.split(".")
    try:
        full_name = f"{second_iterate[0]} {second_iterate[1]}"
    except IndexError:
        full_name = f"{second_iterate[0]}"
    full_name = full_name.title()
    return full_name


def check_if_name(full_name):
    """Check with user if this is the desired output."""
    answer = input(f"Is your name {full_name}? (Y/n) ")
    if answer.upper() == "Y" or answer == "":
        return True
    else:
        return False


main()
