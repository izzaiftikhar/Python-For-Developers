# Day 8 - Python Tuples


# -----------------------------------------
# 1. Creating a Tuple
# -----------------------------------------
# A tuple is a collection of items.
# Tuples are ordered and cannot be changed after creation.
#
# Tuples are usually written using parentheses ().

empty_tuple = ()

print("Empty tuple:", empty_tuple)


# A tuple can contain multiple items.

tuple_1 = ("item 1", "item 2", "item 3")

print("Tuple:", tuple_1)


# -----------------------------------------
# 2. Simple Tuple Practice
# -----------------------------------------
# Tuples can contain different types of values.

student = ("Izza", 20, 5.4, True)

print(student)


# We can check the type of a tuple using type().

print(type(student))


# -----------------------------------------
# 3. Finding the Length of a Tuple
# -----------------------------------------
# len() tells us how many items are inside a tuple.

tuple_2 = ("mango", "banana", "kiwi", "apple")

print("Tuple length:", len(tuple_2))


# -----------------------------------------
# 4. Accessing Tuple Items
# -----------------------------------------
# Tuple indexing starts from 0.
#
# Index:   0        1         2        3
# Value: mango   banana     kiwi     apple

fruits = ("mango", "banana", "kiwi", "apple")

first_fruit = fruits[0]
last_fruit = fruits[3]

print("First fruit:", first_fruit)
print("Last fruit:", last_fruit)


# We can also use negative indexing.
# -1 means the last item.
# -2 means the second-last item.

print("Last fruit:", fruits[-1])
print("First fruit:", fruits[-4])


# -----------------------------------------
# 5. Slicing Tuples
# -----------------------------------------
# Slicing allows us to get a part of a tuple.
#
# tuple[start:stop]
# The stop index is not included.

tuple_numbers = (0, 1, 2, 3, 4, 5, 6, 7)

print("First four:", tuple_numbers[0:4])

print("From index 4:", tuple_numbers[4:])

print("Up to index 6:", tuple_numbers[:7])


# Negative slicing can also be used.

print("Last three:", tuple_numbers[-3:])

print("All except last:", tuple_numbers[:-1])


# -----------------------------------------
# 6. Changing a Tuple into a List
# -----------------------------------------
# Tuples cannot be changed directly.
# If we need to modify the data, we can convert
# the tuple into a list.

tuple_fruits = ("apple", "banana", "peach", "plum", "mango")

fruit_list = list(tuple_fruits)

print("List:", fruit_list)


# Now the list can be modified.

fruit_list.append("orange")

print("Updated list:", fruit_list)


# -----------------------------------------
# 7. Checking an Item in a Tuple
# -----------------------------------------
# The 'in' operator checks whether an item exists
# inside a tuple.
#
# It returns True or False.

tuple_fruits = ("apple", "banana", "peach", "plum", "mango")

print("apple" in tuple_fruits)
print("mango" in tuple_fruits)
print("pineapple" in tuple_fruits)


# 'not in' checks that an item does not exist.

print("orange" not in tuple_fruits)


# -----------------------------------------
# 8. Joining Tuples
# -----------------------------------------
# We can join two or more tuples using +.

tuple_1 = ("Karachi", "Lahore", "Islamabad")
tuple_2 = ("Multan", "Faisalabad", "Malakand")

total_tuple = tuple_1 + tuple_2

print("Total tuple:", total_tuple)


# -----------------------------------------
# 9. Tuples Cannot Be Changed
# -----------------------------------------
# Tuples are immutable.
# This means we cannot directly change an item.

numbers = (10, 20, 30)

# The following would cause an error:
# numbers[0] = 100


# If we need to change the values,
# we can convert the tuple into a list first.

numbers_list = list(numbers)
numbers_list[0] = 100

print("Changed list:", numbers_list)


# -----------------------------------------
# 10. Deleting a Tuple
# -----------------------------------------
# We can delete the entire tuple using del.

tuple_numbers = (0, 1, 2, 3, 4, 5)

del tuple_numbers

# The tuple no longer exists after using del.


# -----------------------------------------
# Tuple Exercises - Level 1
# -----------------------------------------


# -----------------------------------------
# 11. Create an Empty Tuple
# -----------------------------------------

empty_tuple = ()

print("Empty tuple:", empty_tuple)


# -----------------------------------------
# 12. Create a Tuple of Siblings
# -----------------------------------------
# Imaginary siblings are fine for this exercise.

siblings_tuple = ("Abeera", "Faiza", "Saif", "Haider")

print("Siblings:", siblings_tuple)


# -----------------------------------------
# 13. Join Brothers and Sisters Tuples
# -----------------------------------------

sisters_tuple = ("Abeera", "Faiza")
brothers_tuple = ("Haider", "Saif")

siblings_tuple = sisters_tuple + brothers_tuple

print("All siblings:", siblings_tuple)


# -----------------------------------------
# 14. Find the Number of Siblings
# -----------------------------------------

print("Number of siblings:", len(siblings_tuple))


# -----------------------------------------
# 15. Add Parents to Create Family Members
# -----------------------------------------
# Since tuples cannot be changed directly,
# we create a new tuple by joining them.

parents_tuple = ("Iftikhar", "Shabana")

family_members = siblings_tuple + parents_tuple

print("Family members:", family_members)


# -----------------------------------------
# Tuple Exercises - Level 2
# -----------------------------------------


# -----------------------------------------
# 16. Unpacking a Tuple
# -----------------------------------------
# Tuple unpacking means assigning tuple items
# to separate variables.

family_members = (
    "Abeera",
    "Faiza",
    "Saif",
    "Haider",
    "Iftikhar",
    "Shabana"
)

# Here we use *siblings to collect multiple items.
# father gets the second-last item.
# mother gets the last item.

*siblings, father, mother = family_members

print("Siblings:", siblings)
print("Father:", father)
print("Mother:", mother)


# -----------------------------------------
# 17. Creating Food Tuples
# -----------------------------------------

fruits = ("mango", "apple", "banana", "peach", "plum")

vegetables = ("carrot", "radish", "pea", "potato")

animal_products = ("milk", "cheese", "butter", "meat")


# Join all three tuples.

food_stuff_tuple = fruits + vegetables + animal_products

print("Food stuff:", food_stuff_tuple)


# -----------------------------------------
# 18. Convert Food Tuple to a List
# -----------------------------------------

food_stuff_list = list(food_stuff_tuple)

print("Food stuff list:", food_stuff_list)


# -----------------------------------------
# 19. Find the Middle Item
# -----------------------------------------
# The tuple contains 13 items.
# Since 13 is odd, there is one middle item.
#
# The middle index is:
# len(tuple) // 2

middle_index = len(food_stuff_tuple) // 2

print("Middle item:", food_stuff_tuple[middle_index])
print("Middle item:", food_stuff_list[middle_index])


# -----------------------------------------
# 20. Get the First Three and Last Three Items
# -----------------------------------------

print("First three:", food_stuff_list[:3])

print("Last three:", food_stuff_list[-3:])


# -----------------------------------------
# 21. Check Whether an Item Exists
# -----------------------------------------

print("carrot" in food_stuff_list)

print("cheese" in food_stuff_list)


# -----------------------------------------
# 22. Delete the Food Tuple
# -----------------------------------------

del food_stuff_tuple


# -----------------------------------------
# 23. Check Nordic Countries
# -----------------------------------------

nordic_countries = (
    "Denmark",
    "Finland",
    "Iceland",
    "Norway",
    "Sweden"
)

print("Estonia" in nordic_countries)

print("Iceland" in nordic_countries)


# -----------------------------------------
# 24. More Tuple Practice
# -----------------------------------------
# Let's practice indexing and slicing one more time.

colors = ("red", "blue", "green", "yellow", "purple")

print("First color:", colors[0])
print("Last color:", colors[-1])

print("First three colors:", colors[:3])
print("Last two colors:", colors[-2:])


# -----------------------------------------
# 25. Tuple Length and Membership Practice
# -----------------------------------------

numbers = (10, 20, 30, 40, 50)

print("Number of items:", len(numbers))

print(30 in numbers)
print(100 in numbers)

print(60 not in numbers)

# ==========================================
# DAY 8 COMPLETE
# ==========================================