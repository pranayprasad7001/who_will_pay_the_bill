# Importing the random module.
import random

# Taking user's input of everyone in the form of string.
names_string = input("Give me everybody's names, separated by a comma & a space.\n")

# Using split string method.
names = names_string.split(", ")

# Finding the length of the list.
num = len(names)

# Generating the random number from zero upto the length of the list.
random_no = random.randint(0, num - 1)

# Printing the person who is going to pay.
print(f"{names[random_no]} is going to buy the meal today!")


