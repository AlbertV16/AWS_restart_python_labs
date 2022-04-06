# while loops
import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1, 10)

isGuessRight = False

'''
Ask user for guess
Check if guess matches the random number
If correct, tell user they were correct and exit loop
If incorrect, tell user they were incorrect and repeat loop
'''

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
