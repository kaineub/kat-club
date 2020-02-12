# Ask the user for their name
print('What is your name?')
name = input() # This stores the input into a variable into a variable called name
print(type(name)) # Type tells you what data type the variable is. The type is str (short for string).
print()

# Ask the user for their age
print('What is your age?')
age = int(input()) # input() will give us a string but we want a number. Putting int around input() changes the type from str to int (short for integer). This is known as casting from str to int.
print(type(age)) # The type is now int.
print()

# Print out the information that we just got
print('Hello', name + "!") # String addition (also called concatonation). Notice how we need to put the space after the word 'Hello' in the quotes.
print('You are', age, 'years old') # We can also use commas. It will automatically add a space between what we are writing and take care of casting for us. This is the same as the following line
#print('You are ' + str(age) + ' years old')
print('In 5 years, you will be ' + str(age + 5)) # Here we are doing some simple math. We have to cast the result of age + 5 from an int to a str (or we could use a comma).

if age >= 16:
    print('You can get a drivers license')
else:
    print('You cannot get a drivers license')