phrase = "Hello World" # This is the phrase that we are going to guess
wordsInPhrase = phrase.split()

guesses = [] # Start with an empty list for our guesses

gameRunning = True # We use a boolean variable to keep the game running

# The loop will run until the game finishes
while gameRunning:
    # for every word in the phrase
    for word in wordsInPhrase:
        # for every letter in that word
        for letter in word:
             # if that letter has been guessed (we use .lower() here to make sure that uppercase and lowercase letters are recognized as the same letter)
            if letter.lower() in guesses:
                # print the letter (without a new line at the end)
                print(letter,end='')
            # otherwise, (the letter has not been guessed)
            else:
                # print an underscore
                print("_",end="")
        # end each word with a space
        print("",end=" ")
    # go to the next line
    print()
    # Keep running the following block while the game is running
    print("Guess a letter") # Ask for a letter
    
    # read the guess from the user
    guess = input()
    # Check if the guess was valid. We don't let them guess a letter twice or guess a word (more than one letter) or guess anything that is not a letter.
    if guess in guesses or len(guess) != 1 or not guess.isalpha():
        # Guess was invalid
        print("Invalid guess")
    else:
        # Guess was valid
        guesses.append(guess) # Add the letter to the list of guesses
    print(guesses) # Print out the current guesses
    
    
    
    