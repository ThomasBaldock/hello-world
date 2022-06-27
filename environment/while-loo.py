import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(0,10)

isGuessRight = False

while isGuessRight != True: #when it is not true that the guess is right
    guess = input("Guess a number between 1 and 10: ") #ask user to guess a number
    if int(guess) == number:  #if guess is equal to random number then...
        print("You guessed {}. That is correct! You win!".format(guess)) #they win
        isGuessRight = True #and now guess is right is true, so loop ends
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
                            #if guess is not equal to random number then repeat loop