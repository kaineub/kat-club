from random import random, randint # We have to import functions from the random package

# We need the computer to make an initial guess. It'll be a random number between 1 and 10
#guess = int(random()*10) + 1 # The random() function gives a random decimal number between 0 and 1. We multiply it by a constant and then round it down using int(). Because int() always rounds down, we add a 1 to the result.
guess = randint(1,10) # randint() generates a random number between 0 

# Ask them to think of a number between 1 and 10
print("Pick a number between 1 and 10")

# We want the program to run until it guesses the number. We can track this using a variable
numberFound = False

# Use a while loop to keep the program running until the number is found
while not numberFound: # The loop runs until numberFound becomes True
    # Get the program to make the guess
    print("Is the number", str(guess) + " or is it higher or lower?")
    answer = input() # Get a response from the user
    
    # We have 4 possible situations
    if answer == "yes": # 1: the guess was correct
        print("I have found the number")
        numberFound = True # Change numberFound to True so the loop is exited
    elif answer == "higher": # 2: the guess was too low
        guess = guess + 1 # Increase the guess by 1
    elif answer == "lower": # 3: the guess was too high
        guess = guess - 1 # Decrease the guess by 1
    else: # 4: The user gave an incorrect response
        print("Invalid response")
        