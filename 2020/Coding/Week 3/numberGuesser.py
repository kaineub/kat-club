# We are going to hard code the first guess in here
guess = 5

# Get the program to make the first guess
print("Is the number", str(guess) + " or is it higher or lower?")
answer = input() # Get a response from the user

# We have 4 possible situations
if answer == "yes": # 1: the guess was correct
    print("I have found the number")
elif answer == "higher": # 2: the guess was too low
    print("Is the number", str(guess+1) + "?")
elif answer == "lower": # 3: the guess was too high
    print("Is the number", str(guess-1) + "?")
else: # 4: The user gave an incorrect response
    print("Invalid response")