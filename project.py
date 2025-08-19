import time
from random import choice, randint
from pyfiglet import Figlet


def main():
    fonts = ["varsity", "big_money-sw", "smslant", "3d-ascii", "peaks"]

    figlet = Figlet()
    randfont = choice(fonts)
    figlet.setFont(font=randfont)
    print(figlet.renderText("Quizly"))
    print("""Your mental arithmetic quiz maker!\n""")
    time.sleep(2)

    print("""Options:
          1. Additions
          2. Additions and Substractions
          3. Multiplications\n
          """)

    option, name = choose_option()

    total = choose_number_questions()

    score_quiz = quiz(option, name, total)
    percentage = round(score_quiz/total * 100, 2)

    print("You had a score of...")
    time.sleep(1)
    print(f"{score_quiz} out of {total}! ({percentage}%)\n")

    print(feedback(score_quiz, total))


def choose_option():
    while True:
        try:
            option = int(
                input("What do you want to practice? (1, 2 or 3) - ").strip()
            )

            options = {1: "Additions",
                       2: "Additions and Substractions",
                       3: "Multiplications"}

            if not (1 <= option <= 3):
                print("Please choose either 1, 2 or 3.\n")
                continue
            break

        except ValueError:
            print("Please enter a number.\n")
            continue

    name = options[option]

    return option, name


def choose_number_questions():
    while True:
        try:
            total = int(input("How many questions should the test have? (Enter a number) - ").strip())

            if total < 1:
                print("It cannot be lower than one.\n")
                continue
            break

        except ValueError:
            print("Please enter a number.\n")
            continue

    return total


def generate_numbers(option):
    if option == 1:
        first = randint(0, 100)
        second = randint(0, 100)
    elif option == 2:
        first = randint(-100, 100)
        second = randint(-100, 100)
    else:
        first = randint(-50, 50)
        second = randint(-11, 11)

    return first, second


def addition_question(first, second):
    result = first + second
    a = input(f"What's {first} + {second}? 🧠 | ").strip()
    return a, result


def add_sub_question(first, second, i):
    if i % 2 == 0:
        result = first - second
        a = input(f"What's {first} - {second}? 🧠 | ").strip()
    else:
        a, result = addition_question(first, second)

    return a, result


def multiplication_question(first, second):
    result = first * second
    a = input(f"What's {first} * {second}? 🧠 | ").strip()
    return a, result


def check_answer(answer, result):
    is_correct = False

    if int(answer) == result:
        print("Correct ✅\n")
        is_correct = True
    else:
        print(f"Incorrect ❌. The answer was {result}.\n")
    return is_correct


def quiz(option, name, length):
    score = 0
    print(f"""
            Quiz - {name} ({length} questions)
          """)

    time.sleep(2)

    for i in range(length):
        i += 1
        print(f"Question {i}:")

        first_number, second_number = generate_numbers(option)

        while True:
            try:
                if option == 1:
                    answer, result = addition_question(first_number, second_number)
                elif option == 2:
                    answer, result = add_sub_question(first_number, second_number, i)
                else:
                    answer, result = multiplication_question(first_number, second_number)

                if check_answer(answer, result):
                    score += 1
                break

            except ValueError:
                print("Your answer needs to be a number!\n")

    input("Press ENTER to finish the quiz...\n")
    return score


def feedback(score, total):
    half = total * 0.5
    eighty = total * 0.8

    if score <= half:
        return "Don't give up! Try practicing more quizzes and you will see better results! 💪"
    elif half < score <= eighty:
        return "Well done! Let's do better together! Practice makes perfect! 🤗"
    elif eighty < score < total:
        return "Amazing! So close to perfection! 🤩"
    elif score == total:
        return "Outstanding! 💯"


if __name__ == "__main__":
    main()
