# Day 7 - Python Lists


# -----------------------------------------
# 1. Creating an empty list
# -----------------------------------------
# A list stores multiple values in one variable.
# An empty list contains no items.

lst = []

print(lst)
print("Length:", len(lst))


# -----------------------------------------
# 2. Creating lists
# -----------------------------------------

fruits = ["apple", "banana", "orange"]

jobs = ["teacher", "developer", "pilot", "designer", "doctor"]

languages = ["java", "python", "html", "css", "c", "c++"]

print("Fruits:", fruits)
print("Number of fruits:", len(fruits))

print("Jobs:", jobs)
print("Number of jobs:", len(jobs))

print("Languages:", languages)
print("Number of languages:", len(languages))


# -----------------------------------------
# 3. Lists can contain different data types
# -----------------------------------------
# A list can contain strings, numbers,
# booleans, dictionaries, and other values.

mixed_list = [
    "Ayesha",
    30,
    "Teacher",
    {"country": "Pakistan", "is_married": True}
]

print("Mixed list:", mixed_list)


# -----------------------------------------
# 4. Accessing list items using indexing
# -----------------------------------------
# Python starts counting list positions from 0.
#
# 0 = first item
# 1 = second item
# 2 = third item
# ...

profession = ["teacher", "developer", "pilot", "designer", "doctor"]

print(profession[0])
print(profession[4])


# -----------------------------------------
# 5. Accessing items using negative indexing
# -----------------------------------------
# Negative indexes start from the end.
#
# -1 = last item
# -2 = second-last item

print(profession[-2])
print(profession[-4])


# -----------------------------------------
# 6. Simple indexing practice
# -----------------------------------------

colors = ["red", "blue", "green", "yellow"]

print("First color:", colors[0])
print("Last color:", colors[-1])


# -----------------------------------------
# 7. Unpacking list items
# -----------------------------------------
# List unpacking assigns list values
# to separate variables.
#
# *rest collects the remaining values
# into another list.

numerals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first, second, *rest, tenth = numerals

print("First:", first)
print("Second:", second)
print("Rest:", rest)
print("Tenth:", tenth)
print("Original list:", numerals)


# -----------------------------------------
# 8. Slicing lists using positive indexes
# -----------------------------------------
# Slicing allows us to get part of a list.
#
# start:end
# The end position is not included.

subjects = ["math", "english", "urdu", "science", "computer"]

print(subjects[1:3])
print(subjects[2:])
print(subjects[:4])
print(subjects[:])
print(subjects[::2])


# -----------------------------------------
# 9. Slicing lists using negative indexes
# -----------------------------------------

print(subjects[-1:-4])
print(subjects[-3:])
print(subjects[:-2])
print(subjects[:])
print(subjects[::-2])


# -----------------------------------------
# 10. Modifying list items
# -----------------------------------------
# Lists are mutable, which means their
# items can be changed.

laptop_type = ["dell", "hp", "macbook", "lenovo", "toshiba"]

print(laptop_type)

laptop_type[0] = "PS5"
laptop_type[3] = "dell"

print(laptop_type)


# -----------------------------------------
# 11. Checking items in a list
# -----------------------------------------
# The 'in' operator checks whether an
# item exists in a list.

vegetables = ["carrot", "radish", "tomato", "cucumber", "potato"]

print("tomato" in vegetables)
print("cabbage" in vegetables)


# -----------------------------------------
# 12. Adding items using append()
# -----------------------------------------
# append() adds one item to the end of a list.

marks = [85, 90, 76, 80, 55]

marks.append(67)

print(marks)

marks.append(45)

print(marks)


# -----------------------------------------
# 13. Inserting items using insert()
# -----------------------------------------
# insert(index, value) adds an item
# at a specific position.

grades = ["A", "B", "C", "D", "E", "F"]

grades.insert(1, "A+")

print(grades)

grades.insert(3, "B-")

print(grades)


# -----------------------------------------
# 14. Removing an item using remove()
# -----------------------------------------
# remove() removes the first matching value.

juice = ["apple", "mango", "peach", "orange", "plum"]

juice.remove("plum")

print(juice)

juice.remove("peach")

print(juice)


# -----------------------------------------
# 15. Removing items using pop()
# -----------------------------------------
# pop() removes an item using its index.
# It also returns the removed item.

numbers = [0, 1, 2, 3, 4, 5, 6, 7]

removed_number = numbers.pop(4)

print("Removed:", removed_number)
print(numbers)

numbers.pop(0)

print(numbers)


# -----------------------------------------
# 16. Clearing a list using clear()
# -----------------------------------------
# clear() removes all items from a list.

milk_products = ["milk", "cheese", "buttermilk", "butter"]

milk_products.clear()

print(milk_products)


# -----------------------------------------
# 17. Copying a list using copy()
# -----------------------------------------
# copy() creates another list with
# the same items.

berries = ["strawberry", "mulberry", "blueberry", "raspberry"]

berries_copy = berries.copy()

print("Original:", berries)
print("Copy:", berries_copy)


# -----------------------------------------
# 18. Deleting items using del
# -----------------------------------------
# del can remove an item at a specific index.

numbers = [7, 8, 9, 10, 11, 12]

del numbers[3]

print(numbers)


# -----------------------------------------
# 19. Joining lists using +
# -----------------------------------------
# The + operator can combine two or more lists.

num_one = [1, 2, 3, 4, 5]
zero = [0]
num_two = [-5, -4, -3, -2, -1]

numerals = num_one + zero + num_two

print(numerals)


# -----------------------------------------
# 20. Joining lists using extend()
# -----------------------------------------
# extend() adds all items from one list
# to another list.

fruit = ["apple", "mango"]
juice = ["peach", "plum"]

fruit.extend(juice)

print("Fruits:", fruit)


# -----------------------------------------
# 21. Counting items using count()
# -----------------------------------------
# count() tells us how many times
# a value appears in a list.

kingdom = ["prince", "princess", "knight", "assassin"]

print(kingdom.count("knight"))
print(kingdom.count("assassin"))


# -----------------------------------------
# 22. Finding the index of an item
# -----------------------------------------
# index() returns the position of the
# first matching item.

genders = ["male", "female", "transgender"]

print(genders.index("male"))
print(genders.index("female"))


# -----------------------------------------
# 23. Reversing a list
# -----------------------------------------
# reverse() changes the original list
# into reverse order.

numerals = [0, 1, 2, 3, 4, 5, 6]

numerals.reverse()

print(numerals)


# -----------------------------------------
# 24. Sorting a list
# -----------------------------------------
# sort() changes the original list.

fruits = ["mango", "apple", "orange", "peach"]

fruits.sort()

print("Ascending:", fruits)

fruits.sort(reverse=True)

print("Descending:", fruits)


# -----------------------------------------
# 25. sorted() vs sort()
# -----------------------------------------
# sorted() creates a new sorted list
# and keeps the original list unchanged.

fruit = ["mango", "banana", "kiwi", "peach"]

sorted_fruits = sorted(fruit)

print("Original:", fruit)
print("Sorted:", sorted_fruits)


# -----------------------------------------
# 26. Simple list exercise
# -----------------------------------------
# Creating a list with more than 5 items.

fruits = ["apple", "banana", "cherry", "mango", "peach", "orange"]

print(fruits)


# Finding the length of a list

numbers = [1, 2, 3, 4, 5]

print("Length:", len(numbers))


# -----------------------------------------
# 27. Getting the first, middle and last items
# -----------------------------------------

profession = ["Teacher", "Pilot", "Developer"]

print("First:", profession[0])
print("Middle:", profession[1])
print("Last:", profession[2])


# -----------------------------------------
# 28. Creating a mixed data type list
# -----------------------------------------

mixed_data_types = [
    "Ayesha",
    19,
    5.4,
    "married",
    {"address": "Johar Town"}
]

print(mixed_data_types)


# -----------------------------------------
# 29. Creating an IT companies list
# -----------------------------------------

it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
]

print(it_companies)


# -----------------------------------------
# 30. Modifying companies
# -----------------------------------------

it_companies[3] = "Udemy"
it_companies[6] = "Coursera"

print(it_companies)


# -----------------------------------------
# 31. Inserting a company
# -----------------------------------------

it_companies.insert(2, "Enterprises")

print(it_companies)


# -----------------------------------------
# 32. Changing a company name to uppercase
# -----------------------------------------

it_companies[0] = it_companies[0].upper()

print(it_companies)


# -----------------------------------------
# 33. Removing a company
# -----------------------------------------

it_companies.remove("IBM")

print(it_companies)


# -----------------------------------------
# 34. Joining list items with a string
# -----------------------------------------
# join() combines strings from a list
# into one string.

it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
]

companies_string = "#;".join(it_companies)

print(companies_string)


# -----------------------------------------
# 35. Checking if a company exists
# -----------------------------------------

print("Apple" in it_companies)
print("Coursera" in it_companies)


# -----------------------------------------
# 36. Sorting companies
# -----------------------------------------

it_companies.sort()

print(it_companies)


# -----------------------------------------
# 37. Reversing companies in descending order
# -----------------------------------------

it_companies.sort(reverse=True)

print(it_companies)


# -----------------------------------------
# 38. Slicing the first three companies
# -----------------------------------------

it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
]

print(it_companies[:3])


# -----------------------------------------
# 39. Slicing the last three companies
# -----------------------------------------

print(it_companies[-3:])


# -----------------------------------------
# 40. Slicing the middle companies
# -----------------------------------------
# Index 2 starts from Microsoft.
# Index 5 is not included.

print(it_companies[2:5])


# -----------------------------------------
# 41. Removing the first company
# -----------------------------------------

it_companies.remove("Facebook")

print(it_companies)


# -----------------------------------------
# 42. Removing a middle company
# -----------------------------------------

it_companies.remove("Apple")

print(it_companies)


# -----------------------------------------
# 43. Removing the last company
# -----------------------------------------

it_companies.remove("Amazon")

print(it_companies)


# -----------------------------------------
# 44. Removing all companies
# -----------------------------------------

it_companies.clear()

print(it_companies)


# -----------------------------------------
# 45. Joining front-end and back-end lists
# -----------------------------------------

front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]

front_end.extend(back_end)

print("Full stack:", front_end)


# -----------------------------------------
# 46. Copying the joined list
# -----------------------------------------

full_stack = front_end.copy()

# Add Python and SQL after Redux.
# Redux is at index 4, so index 5 is
# the position after it.

full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")

print("Full stack:", full_stack)


# -----------------------------------------
# 47. Working with student ages
# -----------------------------------------

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print("Sorted ages:", ages)
print("Minimum age:", min(ages))
print("Maximum age:", max(ages))


# -----------------------------------------
# 48. Adding minimum and maximum ages again
# -----------------------------------------

ages.append(min(ages))
ages.append(max(ages))

print("Ages:", ages)


# -----------------------------------------
# 49. Finding the median age
# -----------------------------------------
# The median is the middle value of a sorted list.
#
# If there are an even number of values,
# we take the average of the two middle values.

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

middle = len(ages) // 2

if len(ages) % 2 == 0:
    median_age = (ages[middle - 1] + ages[middle]) / 2
else:
    median_age = ages[middle]

print("Median age:", median_age)


# -----------------------------------------
# 50. Finding the average age
# -----------------------------------------
# sum() adds all values in the list.
# len() tells us how many values there are.

average_age = sum(ages) / len(ages)

print("Average age:", average_age)


# -----------------------------------------
# 51. Finding the range of ages
# -----------------------------------------
# Range = maximum value - minimum value.

age_range = max(ages) - min(ages)

print("Range:", age_range)


# -----------------------------------------
# 52. Finding the middle country
# -----------------------------------------

countries = [
    "China",
    "Russia",
    "USA",
    "Finland",
    "Sweden",
    "Norway",
    "Denmark"
]

middle_index = len(countries) // 2

print("Middle country:", countries[middle_index])


# -----------------------------------------
# 53. Comparing minimum and maximum
#     distance from the average
# -----------------------------------------

min_age = min(ages)
max_age = max(ages)
average_age = sum(ages) / len(ages)

value_1 = abs(min_age - average_age)
value_2 = abs(max_age - average_age)

print("Value 1:", round(value_1, 1))
print("Value 2:", round(value_2, 1))


# -----------------------------------------
# 54. Comparing the two values
# -----------------------------------------

if value_1 > value_2:
    print("Value 1 is greater than Value 2")
elif value_1 < value_2:
    print("Value 2 is greater than Value 1")
else:
    print("Both values are equal")


# -----------------------------------------
# 55. Dividing countries into two parts
# -----------------------------------------
# The +1 helps us keep the extra item
# in the first half when the list has
# an odd number of items.

middle = (len(countries) + 1) // 2

first_half = countries[:middle]
second_half = countries[middle:]

print("First half:", first_half)
print("Second half:", second_half)


# -----------------------------------------
# 56. Unpacking the first three countries
# -----------------------------------------
# The * operator collects all remaining
# values into a list.

first, second, third, *scandic_countries = countries

print("First:", first)
print("Second:", second)
print("Third:", third)
print("Remaining countries:", scandic_countries)

# ==========================================
# DAY 7 COMPLETE
# ==========================================