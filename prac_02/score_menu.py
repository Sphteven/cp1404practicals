def main():
    MENU = ("(G)et a valid score\n"
            "(P)rint result\n"
            "(S)how stars\n"
            "(Q)uit")
    score = get_valid_score()
    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_result(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        choice = input("Enter your choice: ").upper()
    print("See you next time friend.")

def get_valid_score():
    score = int(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter your score: "))
    return score


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"


def print_stars(score):
    for i in range(0, score):
        print("*", end="")
    print("")


main()
