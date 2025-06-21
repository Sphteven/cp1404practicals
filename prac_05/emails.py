"""
emails
Estimate: 45 minutes
Actual:   55 minutes
"""


def main():
    emails = []
    email = get_email()
    while email != "":
        get_name(email)
        emails.append(email)
        email = get_email()


def get_email():
    email = input("Email: ")
    return email


def get_name(email):
    first_iterate = email.split("@")[0]
    second_iterate = first_iterate.split(".")
    print(second_iterate)
    try:
        full_name = f"{second_iterate[0]} {second_iterate[1]}"
    except IndexError:
        full_name = f"{second_iterate[0]}"
    return full_name


main()
