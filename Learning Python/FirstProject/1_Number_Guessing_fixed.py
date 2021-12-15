from random import randint

# 2. Number Guessing

# This is one of the simple python projects yet an exciting one.
# You can even call it a mini-game. Make a program in which the computer
# randomly chooses a number between 1 to 10, 1 to 100, or any range.
# Then give users a hint to guess the number. Every time the user
# guesses wrong, he gets another clue, and his score gets reduced.
# The clue can be multiples, divisible, greater or smaller, or a combination of all.

# You will also need functions to compare the inputted number with the guessed number,
# to compute the difference between the two, and to check whether an actual number
# was inputted or not in this python project.


def compareNumbers(number, solution):
    if (number > solution) or number < solution:
        return number - solution
    else:
        return 0


def computeDifference(number, solution):
    if number > solution:
        return number - solution
    else:
        return solution - number


def multiple(solution):
    if solution % 2 == 0:
        print("The number is multiple of 2")
    elif solution % 5 == 0:
        print("The number is multiple of 5")
    else:
        print("The number is not multiple of 2 nor 5")


def input_number():
    number = 0
    while number < 1 or number > 10:
        try:
            number = int(input("Enter a number from 1 to 10: "))
        except ValueError:
            print("Enter a number you dumbass: ")
    return number


def main():
    # We set the initial score and then we will substract 20 points for each incorrect answer.
    score = 100
    solution = randint(1, 10)
    guess = 0

    multiple(solution)

    while guess != solution:

        guess = input_number()

        if compareNumbers(guess, solution) == 0:
            break
        elif compareNumbers(guess, solution) > 0:
            print("-20 points")
            score -= 20
            print("The number is too big")
        else:
            print("-20 points")
            score -= 20
            print("The number is too small")

        if solution != guess:
            print(
                f"The difference between the two numbers is: {abs(compareNumbers(guess, solution))}"
            )

    print(f"Congratulations!! The solution was {solution}")
    print(f"Your score is: {score}")


if __name__ == "__main__":
    main()
