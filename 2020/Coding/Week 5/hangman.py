phrase = "hello world" # This is the phrase that we are going to guess

guesses = [] # Start with an empty list for our guesses

gameRunning = True # We use a boolean variable to keep the game running

while gameRunning:
    # Keep running the following block while the game is running
    print("Guess a letter") # Ask for a letter
    guesses.append(input()) # Add the letter to the list of guesses
    print(guesses) # Print out the current guesses