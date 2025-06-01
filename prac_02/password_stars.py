def main():
    password = get_password()
    print_password(password)


def print_password(password):
    for i in password:
        print("*", end="")


def get_password():
    password = input('Enter a password: ')
    while len(password) < 10:
        print('Password must be at least 10 characters long')
        password = input('Enter a password: ')
    return password


main()
