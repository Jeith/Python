import random 
secret_number = str(random.randint(1, 10))
guessed_number = input("I am thinking of a number between 1 and 10. What is this number? ")
loop = 5
while True:
    if loop == 0:
        print("you've run out of guesses")
        break
    elif guessed_number == secret_number:
        print("Yes! You win!")
        answer = input("Would you like to play again[Y or N]? ")
        if answer == "Y":
            guessed_number = input("I am thinking of a number between 1 and 10. What is this number? ")
            loop = 5
            secret_number = str(random.randint(1, 10))
        elif answer == "N":
            print("Thank you!")
            break
    elif guessed_number > secret_number:
        guessed_number = input(guessed_number + " is too high. You have " + str(loop) + " guesses left. try again: ")
        loop -= 1
    elif guessed_number < secret_number:
        guessed_number = input(guessed_number + " is too low. You have " + str(loop) + " guesses left. try again: ")
        loop -= 1
    else:
        print("Invalid input")