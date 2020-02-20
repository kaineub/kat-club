fruits = ["apple", "banana", "beans"] # Create a list of fruits (beans are not a fruit but whatever)
print(fruits) # Print out the list (['apple', 'banana', 'beans'])
print(fruits[1]) # Print out the item at index 1. Note that indexing starts at 0 so 1 is actually the second item (banana).
print(fruits[-2]) # Negative indexing counts from the end of the list. -1 is the last item and -2 is the second last item (banana).
print(fruits[0:2]) # Slicing allows us to make a new list from parts of another list. This is everything from index 0 up to but not including index 2 (['apple', 'banana']). 
print(fruits[-2:-1]) # Negative slices also work (['banana']).

fruits[1] = "orange" # We can change specific items in lists similar to regular variables.
print(fruits) # prints ['apple', 'orange', 'beans']

fruits.append("mango") # append() adds an item to the list
print(fruits) # prints ['apple', 'orange', 'beans', 'mango']

fruits.insert(1,"pineapple") # insert() adds an item at a specific index
print(fruits) # prints ['apple', 'pineapple', 'orange', 'beans', 'mango']

# We can check whether an item is in a list using in
if "apple" in fruits:
    print("The list has an apple in it")
    
fruits.remove("beans") # remove() removes the item from the list
print(fruits) # prints ['apple', 'pineapple', 'orange', 'mango'] 

fruits.pop() # pop() removes the last element from the list
print(fruits) # prints ['apple', 'pineapple', 'orange'] 

fruits.pop(1) # We can give an index for pop() to remove the item at that index
print(fruits) # prints ['apple', 'orange'] 

# We can use a for loop to loop through every item in the list
for item in fruits:
    print(item) # print each item on a new line
    