fruits = ["apple", "banana", "beans"]
print(fruits)
print(fruits[1])
print(fruits[-2])
print(fruits[0:2])
print(fruits[-2:-1])

fruits[1] = "orange"
print(fruits)

fruits.append("mango")
print(fruits)

fruits.insert(1,"pineapple")
print(fruits)

if "apple" in fruits:
    print("The list has an apple in it")
    
fruits.remove("beans")
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(1)
print(fruits)

for item in fruits:
    print(item)
