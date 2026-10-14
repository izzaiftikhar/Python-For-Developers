# Day 9 - Python Sets


# -----------------------------------------
# 1. Creating a Set
# -----------------------------------------
# A set is a collection of unique items.
# Sets are unordered, so their items do not have
# a fixed position or index.
#
# IMPORTANT:
# {} creates an empty dictionary, NOT an empty set.
# To create an empty set, use set().

empty_set = set()

print("Empty set:", empty_set)


# Creating a set with values.

fruits_set = {"mango", "banana", "peach", "apple"}

print("Fruits set:", fruits_set)


# -----------------------------------------
# 2. Finding the Length of a Set
# -----------------------------------------
# len() tells us how many unique items
# are present in the set.

numbers_set = {0, 1, 2, 3, 4, 5, 6, 7}

print("Set length:", len(numbers_set))


# -----------------------------------------
# 3. Checking an Item in a Set
# -----------------------------------------
# The 'in' operator checks whether an item
# exists in a set.

float_set = {3.12, 2.3, 9.8, 5.7}

print(3.14 in float_set)
print(5.7 in float_set)


# 'not in' checks that an item does not exist.

print(10.5 not in float_set)


# -----------------------------------------
# 4. Adding an Item to a Set
# -----------------------------------------
# add() adds one item to a set.

value_set = {"value 1", "value 2", "value 3", "value 4"}

value_set.add("value 5")

print("Updated set:", value_set)


# -----------------------------------------
# 5. Adding Multiple Items with update()
# -----------------------------------------
# update() can add multiple items to a set.

fruits = {"apple", "mango", "banana"}

vegetables = {"cabbage", "carrot"}

fruits.update(vegetables)

print("Updated fruits set:", fruits)


# -----------------------------------------
# 6. Removing Items from a Set
# -----------------------------------------
# remove() removes a specific item.
#
# If the item does not exist, remove() raises
# a KeyError.

float_set = {3.12, 2.3, 9.8, 5.7}

float_set.remove(3.12)

print("After remove:", float_set)


# -----------------------------------------
# 7. Removing an Item with pop()
# -----------------------------------------
# pop() removes and returns an arbitrary item.
# Sets are unordered, so we cannot choose which
# item will be removed.

numbers_set = {0, 1, 2, 3, 4, 5, 6, 7}

removed_item = numbers_set.pop()

print("Removed item:", removed_item)
print("Remaining set:", numbers_set)


# -----------------------------------------
# 8. Clearing a Set
# -----------------------------------------
# clear() removes all items from the set.
# The set itself still exists.

names_set = {"Ali", "Amna", "Abeera"}

names_set.clear()

print("Cleared set:", names_set)


# -----------------------------------------
# 9. Deleting a Set
# -----------------------------------------
# del completely removes the set.

numerals_set = {0, 1, 2, 3, 4, 5, 6, 7}

del numerals_set


# -----------------------------------------
# 10. Converting a List to a Set
# -----------------------------------------
# set() can convert a list into a set.
#
# Duplicate items would automatically be removed.

items_list = ["item 1", "item 2", "item 3", "item 4"]

items_set = set(items_list)

print("Set:", items_set)


# -----------------------------------------
# 11. Joining Sets with union()
# -----------------------------------------
# union() combines all unique items from
# two sets.

name_set = {"Ali", "Amna", "Abeera"}

age_set = {25, 14, 37}

combined_set = name_set.union(age_set)

print("Combined set:", combined_set)


# -----------------------------------------
# 12. Joining Sets with update()
# -----------------------------------------
# update() adds items from another set directly
# into the original set.

subjects_set = {"English", "Urdu", "Anatomy"}

marks_set = {76, 98, 83}

subjects_set.update(marks_set)

print("Updated set:", subjects_set)


# -----------------------------------------
# 13. Finding Intersection
# -----------------------------------------
# intersection() returns the items that are
# present in BOTH sets.

even_numbers = {2, 4, 6, 8, 10, 12, 14}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8}

common_numbers = even_numbers.intersection(whole_numbers)

print("Common numbers:", common_numbers)


# -----------------------------------------
# 14. Checking a Subset
# -----------------------------------------
# A set is a subset if ALL of its items
# are also present in another set.

item_set = {"item 1", "item 2", "item 3", "item 4"}

product_set = {"item 2", "item 4"}

print(product_set.issubset(item_set))

# This is False because item_set contains
# items that are not inside product_set.

print(item_set.issubset(product_set))


# -----------------------------------------
# 15. Checking a Superset
# -----------------------------------------
# A set is a superset if it contains all
# the items of another set.

print(item_set.issuperset(product_set))


# -----------------------------------------
# 16. Finding the Difference
# -----------------------------------------
# difference() returns items that exist in
# the first set but not in the second set.

a_set = {0, 1, 2, 3, 4, 5, 6}

b_set = {1, 2, 3, 4, 5, 6, 7, 8}

print("A - B:", a_set.difference(b_set))

print("B - A:", b_set.difference(a_set))


# -----------------------------------------
# 17. Finding Symmetric Difference
# -----------------------------------------
# symmetric_difference() returns items that
# are in either set, but NOT in both sets.

whole_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

integer_set = {1, 2, 3, 4, 5, 6, 7, 8}

print(
    "Symmetric difference:",
    integer_set.symmetric_difference(whole_set)
)


# -----------------------------------------
# 18. Checking Disjoint Sets
# -----------------------------------------
# isdisjoint() checks whether two sets have
# NO items in common.
#
# If they have no common items -> True
# If they have common items -> False

a_set = {0, 1, 2, 3, 4, 5, 6}

b_set = {1, 2, 3, 4, 5, 6, 7, 8}

print("Are sets disjoint?", a_set.isdisjoint(b_set))


# -----------------------------------------
# Sets Exercises - Level 1
# -----------------------------------------


# -----------------------------------------
# 19. Find the Length of IT Companies
# -----------------------------------------

it_companies = {
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
}

print("Number of companies:", len(it_companies))


# -----------------------------------------
# 20. Add Twitter
# -----------------------------------------

it_companies.add("Twitter")

print("After adding Twitter:", it_companies)


# -----------------------------------------
# 21. Add Multiple Companies
# -----------------------------------------

enterprises = {"Tech", "Udemy", "Coursera"}

it_companies.update(enterprises)

print("After adding multiple companies:", it_companies)


# -----------------------------------------
# 22. Remove a Company
# -----------------------------------------

it_companies.remove("Oracle")

print("After removing Oracle:", it_companies)


# -----------------------------------------
# 23. remove() vs discard()
# -----------------------------------------
# remove() raises an error if the item doesn't exist.
#
# discard() does NOT raise an error if the item
# doesn't exist.

company_set = {"Google", "Apple", "Microsoft"}

company_set.discard("Amazon")

print("After discard:", company_set)


# -----------------------------------------
# Sets Exercises - Level 2
# -----------------------------------------


# -----------------------------------------
# 24. Joining A and B
# -----------------------------------------

A = {19, 22, 24, 20, 25, 26}

B = {19, 22, 20, 25, 26, 24, 28, 27}

union_set = A.union(B)

print("A union B:", union_set)


# -----------------------------------------
# 25. Finding A Intersection B
# -----------------------------------------

print("A intersection B:", A.intersection(B))


# -----------------------------------------
# 26. Check if A is a Subset of B
# -----------------------------------------

print("Is A a subset of B?", A.issubset(B))


# -----------------------------------------
# 27. Check if A and B are Disjoint
# -----------------------------------------

print("Are A and B disjoint?", A.isdisjoint(B))


# -----------------------------------------
# 28. Joining A with B and B with A
# -----------------------------------------
# Union is commutative.
# A union B and B union A contain the same items.

union_A_B = A.union(B)

union_B_A = B.union(A)

print("A union B:", union_A_B)

print("B union A:", union_B_A)


# -----------------------------------------
# 29. Symmetric Difference
# -----------------------------------------

print("Symmetric difference:", A.symmetric_difference(B))


# -----------------------------------------
# 30. Delete the Sets
# -----------------------------------------

del A
del B


# -----------------------------------------
# Sets Exercises - Level 3
# -----------------------------------------


# -----------------------------------------
# 31. Convert Ages to a Set
# -----------------------------------------
# Sets automatically remove duplicate values.

ages = [22, 19, 24, 25, 26, 24, 25, 24]

ages_set = set(ages)

print("Ages list:", ages)
print("Ages set:", ages_set)


# -----------------------------------------
# 32. Compare List and Set Lengths
# -----------------------------------------
# The list contains duplicate ages.
# The set contains only unique ages.

ages_list = [22, 19, 24, 25, 26, 24, 25, 24]

print("Length of list:", len(ages_list))
print("Length of set:", len(ages_set))

if len(ages_list) > len(ages_set):
    print("Length of list is bigger than length of set.")
elif len(ages_list) < len(ages_set):
    print("Length of set is bigger than length of list.")
else:
    print("Both have the same length.")


# -----------------------------------------
# 33. Difference Between String, List,
#     Tuple and Set
# -----------------------------------------
#
# String:
# Stores text.
# Example: "Python"
# Strings are immutable.
#
# List:
# Stores ordered items.
# Uses square brackets [].
# Lists are mutable.
#
# Tuple:
# Stores ordered items.
# Uses parentheses ().
# Tuples are immutable.
#
# Set:
# Stores unique items.
# Sets are unordered and mutable.
# Duplicate items are automatically removed.


# -----------------------------------------
# 34. Find Unique Words
# -----------------------------------------
# We can use a set to find unique words
# from a sentence.

sentence = "I am a teacher and I love to inspire and teach people."


# Remove the full stop.

sentence = sentence.replace(".", "")


# split() changes the sentence into a list of words.

words = sentence.split()

print("Words:", words)


# Convert the list into a set.
# Duplicate words will be removed.

unique_words = set(words)

print("Unique words:", unique_words)

print("Number of unique words:", len(unique_words))


# -----------------------------------------
# 35. Extra Set Practice
# -----------------------------------------

python_students = {"Izza", "Ali", "Amna", "Abeera"}

flask_students = {"Izza", "Abeera", "Saif"}

# Students learning both Python and Flask

both_courses = python_students.intersection(flask_students)

print("Students learning both:", both_courses)


# Students learning Python only

python_only = python_students.difference(flask_students)

print("Python only:", python_only)


# All students from both courses

all_students = python_students.union(flask_students)

print("All students:", all_students)

# ==========================================
# DAY 9 COMPLETE
# ==========================================