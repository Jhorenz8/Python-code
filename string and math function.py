
name = input("Enter your name: ")
greeting = "Hello, " + name + "!"
print(greeting)

print("Your name has", len(name), "characters.")

food = ["chicken", "spaghetti", "pancit canton", "adobo", "ramen"]
addFood = input("Enter food to add: ")
food.append(addFood)  
print(food)
removeFood = input("Enter food to remove: ")
food.remove(removeFood)
print(food)


cars = ("toyota", "honda", "bmw", "corvette", "porsche")
print(cars)
print("2nd car:" + "" + cars[1])
print("last car:" + "" + cars[-1])

print(cars)

physicalHobbies = {
    "swimming",
    "running",
    "biking",
    "sports",
    "swimming",
    "hiking",
}
mentalHobbies = {
    "reading",
    "sports",
    "listening to music",
    "playing video games",
    "watching movies",
    "playing board games"
}

print("\n")

print("Set A: ", physicalHobbies)
print("Set B: ", mentalHobbies)
print("\n")

print("\n")


union = physicalHobbies | mentalHobbies
difference = physicalHobbies - mentalHobbies
intersection = physicalHobbies & mentalHobbies
print("Union: ", union)
print("Difference: ", difference)
print("Intersection: ", intersection)

print("Uppercase:", name.upper())

print("\nNow let's do some math!")

x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)

if y != 0:
    print("Division:", x / y)
else:
    print("Cannot divide by zero!")

print("x raised to the power y:", x ** y)
