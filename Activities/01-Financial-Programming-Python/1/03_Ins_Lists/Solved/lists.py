# -*- coding: utf-8 -*-
"""Instructor Demo: Lists.

This script showcases basic operations of Python Lists.
"""

# A list in Python is a collection of ordered elements or values, separated by commas, with an index of "zero" for the first element.

# Index: 0 = "green", 1 = "blue", 2 = "red", 3 = "purple"
color_hats = ["green", "blue", "red", "purple"]


# Lists commonly hold values of the same data type or different data types.
# Lists can even hold other lists!

my_favorite_things = ["Chocolate", 9, ["beach", "mountains"], "breakfast_tacos"]

# Create a list of places where our class lives from slack responses.
print("We are a diverse group and come from everywhere...")
where_we_live = [
    "San Francisco, CA",
    "Conway, AR",
    "Orlando, FL",
    "Buffalo, NY",
    "Chicago, IL",
    "Edison, NJ",
    "Avondale, PA",
]
print(where_we_live)
print("---------------")

# Students should use the index of their hometown.
print("My hometown is at index...")
print(where_we_live[2])

# Students can check their work with the index method
print("My cities index is at...")
print(where_we_live)
print(where_we_live.index("Conway, AR"))
print("---------------")


# Set elements from index 2 to index 5 equal to some_of_our_places variable and print
print("We can access a portion of the list with a slice...")
some_of_our_places = where_we_live[2:5]
print(some_of_our_places)
print("---------------")

# Print every other element
print("Printing every other city")
every_other_city = where_we_live[::2]
print(every_other_city)

# Print the last element of the list
print("The last city is...")
last_city = where_we_live[-1]
print(last_city)


# Change a specified element within the list at the given index
print("Change the first element in the list...")
where_we_live[0] = "Las Vegas, NV"
print(where_we_live)

# Add an element to the end of the list
print("Adding a new place to the end of the list...")
where_we_live.append("Honolulu, HI")
print(where_we_live)

# Add an element to the end of the list
print("Removing a new place to the end of the list...")
where_we_live.remove("Honolulu, HI")
print(where_we_live)

# Remove an element from the list based on the given index
print("Removing 'Orlando, FL' based off of its index")
florida_index = where_we_live.index("Orlando, FL")
where_we_live.pop(florida_index)
print(where_we_live)
print("---------------")

# Calculate the number of elements within the list
print("Calculating the number of places...")
print(len(where_we_live))
print("---------------")
