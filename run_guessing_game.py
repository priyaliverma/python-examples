# def meow():
#     print "meow"
from random import randint


def run_guessing_game():
    secret_number = randint(0,100)

    for i in range(0, 10):
        guess = input("Enter a number: ")

        if secret_number != guess:
            if guess < secret_number:
                print ("Your guess is low")
            else:
                print ("Your guess is high")
        else:
            print ("Your guess is correct")
            print ("You Won")
            return

    print("You lost")

run_guessing_game()