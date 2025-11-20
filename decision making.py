food = ("chicken", "spaghetti", "pancit canton", "adobo", "ramen")
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
