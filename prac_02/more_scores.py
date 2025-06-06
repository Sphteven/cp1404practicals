import random
def main():
    num_of_scores = get_valid_score()
    f = open("results.txt", "w")
    for i in range(num_of_scores):
        number = random.randint(1, 100)
        result = get_result(number)
        f.write(f"{number} is {result} \n")
        print(f"{number} is {result}")
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

def get_valid_score():
    score = int(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter your score: "))
    return score

main()