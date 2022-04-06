# Using strings

myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

# Concatenating strings

firstStr = "water"
secondStr = "fall"
thirdStr = firstStr + secondStr
print(thirdStr)

# Using input strings

name = input("What is your name? ")
print(name)

# Formatting output strings

color = input("What is your favourite color? ")
animal = input("What is your favourite animal? ")
print("{}, you like a {} {}!".format(name, color, animal ))