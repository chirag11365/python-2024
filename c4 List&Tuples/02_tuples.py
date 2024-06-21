# A tuple is an immutable data type in python.
a = () # empty tuple
a = (1,) # tuple with only one element needs a comma
a = (1,7,2) # tuple with more than one element

# a = (1, 7, 2)
# • a.count (1): a count (1) will return number of times 1 occurs in a.
# • a.index (1) will return the index of first occurrence of 1 in a

# ques 1..
# Write a program to store seven fruits in a list entered by the user.

# Initialize an empty list to store the fruits
fruits = []

# Get input from the user for seven fruits
for i in range(7):
    fruit = input(f"Enter fruit {i + 1}: ")
    fruits.append(fruit)

# Print the list of fruits
print("List of fruits:", fruits)
# 🍎🍌🍇🍓🍊🍍🍑