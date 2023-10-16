# importing random library
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_item = len(names)
index= random.randint(0,num_item-1)

# Printing the final outcome using "fstring"
print(f"{names[index]} is going to buy the meal today!")
