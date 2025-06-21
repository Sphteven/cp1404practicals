"""
emails
Estimate: 45 minutes
Actual:   55 minutes
"""


def main():
    emails = []
    email = get_email()
    while email != "":
        full_name = email_to_name(email)
        emails.append(email)
        if check_if_name(full_name):
            print("yes")
        else:
            print("no")
        email = get_email()


def get_email():
    email = input("Email: ")
    return email


def email_to_name(email):
    first_iterate = email.split("@")[0]
    second_iterate = first_iterate.split(".")
    try:
        full_name = f"{second_iterate[0]} {second_iterate[1]}"
    except IndexError:
        full_name = f"{second_iterate[0]}"
    return full_name


def check_if_name(full_name):
    answer = input(f"Is your name {full_name}? (Y/n) ")
    if answer.upper() == "Y" or answer == "":
        return True
    else:
        return False
main()
