"""
emails
Estimate: 45 minutes
Actual:   55 minutes
"""


def main():
    emails_to_name = {}
    emails = []
    email = get_email()
    while email != "":
        full_name = convert_email_to_name(email)
        emails.append(email)
        if check_if_name(full_name) is False:
            full_name = input("Name: ").title()
        emails_to_name[full_name] = email
        email = get_email()
    for name, email in emails_to_name.items():
        print(f"{name} ({email})")


def get_email():
    email = input("Email: ")
    return email


def convert_email_to_name(email):
    first_iterate = email.split("@")[0]
    second_iterate = first_iterate.split(".")
    try:
        full_name = f"{second_iterate[0]} {second_iterate[1]}"
    except IndexError:
        full_name = f"{second_iterate[0]}"
    full_name = full_name.title()
    return full_name


def check_if_name(full_name):
    answer = input(f"Is your name {full_name}? (Y/n) ")
    if answer.upper() == "Y" or answer == "":
        return True
    else:
        return False


main()
