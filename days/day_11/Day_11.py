# ============================================================
# DAY 11 - LISTS, TUPLES AND SETS
# ============================================================
# Today I am practicing three important Python data types:
#
# 1. Lists  -> ordered and changeable
# 2. Tuples -> ordered but not changeable
# 3. Sets   -> unordered collection of unique items
#
# I am also practicing their methods, indexing, slicing,
# membership checking, and common operations.
# ============================================================


# ============================================================
# PART 1 - LISTS
# ============================================================

# -------------------------
# Creating Lists
# -------------------------

lst = []

print("Empty list:", lst)
print("Length:", len(lst))


# A list can contain multiple values.
fruits = ["apple", "banana", "orange"]
jobs = ["teacher", "developer", "pilot", "designer", "doctor"]
languages = ["java", "python", "html", "css", "c", "c++"]

print("Fruits:", fruits)
print("Number of fruits:", len(fruits))

print("Jobs:", jobs)
print("Number of jobs:", len(jobs))

print("Languages:", languages)
print("Number of languages:", len(languages))


# -------------------------
# Lists with Different Data Types
# -------------------------

# A list can contain different types of data.
lst_1 = [
    "Ayesha",
    30,
    "Teacher",
    {"country": "Pakistan", "is_married": True}
]

print("Mixed list:", lst_1)


# ============================================================
# LIST INDEXING
# ============================================================

# -------------------------
# Positive Indexing
# -------------------------

profession = ["teacher", "developer", "pilot", "designer", "doctor"]

print("First profession:", profession[0])
print("Last profession:", profession[4])


# -------------------------
# Negative Indexing
# -------------------------

# -1 means the last item.
# -2 means the second-last item.

print("Second-last profession:", profession[-2])
print("Fourth-last profession:", profession[-4])


# -------------------------
# Unpacking Lists
# -------------------------

numerals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first, second, *rest, tenth = numerals

print("First:", first)
print("Second:", second)
print("Rest:", rest)
print("Tenth:", tenth)
print("Original list:", numerals)


# ============================================================
# LIST SLICING
# ============================================================

subjects = ["math", "english", "urdu", "science", "computer"]

# Start is included, end is excluded.
print(subjects[1:3])
print(subjects[2:])
print(subjects[:4])
print(subjects[:])

# Step of 2 means take every second item.
print(subjects[::2])


# -------------------------
# Negative Slicing
# -------------------------

subjects = ["math", "english", "urdu", "science", "computer"]

# [-1:-4] gives an empty list because the default
# step is +1 and the start is after the end.
print("Last item:", subjects[-1])
print("Last three:", subjects[-3:])
print("Everything except last two:", subjects[:-2])
print("Copy of list:", subjects[:])
print("Every second item from the end:", subjects[::-2])


# ============================================================
# MODIFYING LISTS
# ============================================================

laptop_type = ["dell", "hp", "macbook", "lenovo", "toshiba"]

print("Before:", laptop_type)

laptop_type[0] = "PS5"
laptop_type[3] = "dell"

print("After:", laptop_type)


# ============================================================
# CHECKING ITEMS IN A LIST
# ============================================================

vegetables = ["carrot", "radish", "tomato", "cucumber", "potato"]

print("Is tomato in the list?", "tomato" in vegetables)
print("Is cabbage in the list?", "cabbage" in vegetables)


# ============================================================
# ADDING ITEMS
# ============================================================

# append() adds an item to the end of the list.

marks = [85, 90, 76, 80, 55]

marks.append(67)
print("After adding 67:", marks)

marks.append(45)
print("After adding 45:", marks)


# -------------------------
# insert()
# -------------------------

grade = ["A", "B", "C", "D", "E", "F"]

grade.insert(1, "A+")
print("After inserting A+:", grade)

grade.insert(3, "B-")
print("After inserting B-:", grade)


# ============================================================
# REMOVING ITEMS
# ============================================================

# remove() removes an item by its value.

juice = ["apple", "mango", "peach", "orange", "plum"]

juice.remove("plum")
print("After removing plum:", juice)

juice.remove("peach")
print("After removing peach:", juice)


# -------------------------
# pop()
# -------------------------

# pop() removes an item using its index.
# It also returns the removed item.

index = [0, 1, 2, 3, 4, 5, 6, 7]

removed_item = index.pop(4)

print("Removed item:", removed_item)
print("List:", index)

index.pop(0)

print("After removing first item:", index)


# ============================================================
# CLEARING AND COPYING
# ============================================================

milk_products = ["milk", "cheese", "buttermilk", "butter"]

milk_products.clear()

print("After clear():", milk_products)


berries = ["strawberry", "mulberry", "blue berry", "rasp berry"]

berries_copy = berries.copy()

print("Original:", berries)
print("Copy:", berries_copy)


# ============================================================
# DELETING ITEMS
# ============================================================

index_1 = [7, 8, 9, 10, 11, 12]

del index_1[3]

print("After deleting index 3:", index_1)

# del can also delete the complete variable.
del index_1


# ============================================================
# JOINING LISTS
# ============================================================

num_one = [1, 2, 3, 4, 5]
zero = [0]
num_two = [-5, -4, -3, -2, -1]

numerals = num_one + zero + num_two

print("Joined list:", numerals)


# -------------------------
# extend()
# -------------------------

fruit = ["apple", "mango"]
juice = ["peach", "plum"]

# extend() adds all items from another list.
# It changes the original list and returns None.

fruit.extend(juice)

print("Fruits:", fruit)


# ============================================================
# count() AND index()
# ============================================================

kingdom = ["prince", "princess", "knight", "assassin"]

print("Knight count:", kingdom.count("knight"))
print("Assassin count:", kingdom.count("assassin"))


genders = ["male", "female", "transgender"]

print("Index of male:", genders.index("male"))
print("Index of female:", genders.index("female"))


# ============================================================
# reverse(), sort() AND sorted()
# ============================================================

numerals = [0, 1, 2, 3, 4, 5, 6]

numerals.reverse()

print("Reversed:", numerals)


fruits = ["mango", "apple", "orange", "peach"]

fruits.sort()

print("Ascending:", fruits)

fruits.sort(reverse=True)

print("Descending:", fruits)


# sorted() creates a new sorted list.
# The original list stays unchanged.

fruit = ["mango", "banana", "kiwi", "peach"]

sorted_fruits = sorted(fruit)

print("Original:", fruit)
print("Sorted copy:", sorted_fruits)


# ============================================================
# SIMPLE LIST PRACTICE
# ============================================================

empty_list = []

print("Empty list:", empty_list)


fruits = ["apple", "banana", "cherry", "mango", "peach"]

print("Fruits:", fruits)


numbers = [1, 2, 3, 4, 5]

print("Number of items:", len(numbers))


profession = ["Teacher", "Pilot", "Developer"]

print("First:", profession[0])
print("Middle:", profession[1])
print("Last:", profession[2])


mixed_data_types = [
    "Ayesha",
    19,
    5.4,
    "married",
    {"address": "Johar Town"}
]

print("Mixed data:", mixed_data_types)


# ============================================================
# IT COMPANIES EXERCISES
# ============================================================

it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
]

print("IT companies:", it_companies)


# Modify companies

it_companies[3] = "Udemy"
it_companies[6] = "Coursera"

print("Modified companies:", it_companies)


# Insert a company

it_companies.insert(2, "Enterprises")

print("After inserting:", it_companies)


# Remove IBM and make the first company uppercase

it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
]

it_companies.remove("IBM")
it_companies[0] = it_companies[0].upper()

print("After removing IBM:", it_companies)


# Join companies with "#;"

it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
]

joined_companies = "#;".join(it_companies)

print("Joined companies:", joined_companies)


# Check if companies exist

it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
]

print("Is Apple present?", "Apple" in it_companies)
print("Is Coursera present?", "Coursera" in it_companies)


# Sorting

profession = ["Teacher", "Pilot", "Developer"]

profession.sort()

print("Sorted professions:", profession)


# Reverse sorting

profession = ["Teacher", "Pilot", "Developer"]

profession.sort(reverse=True)

print("Descending professions:", profession)


# First three companies

it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
]

print("First three:", it_companies[:3])


# Last three companies

print("Last three:", it_companies[-3:])


# Middle companies

# There are 7 companies, so the middle company is index 3.
print("Middle company:", it_companies[3])


# Removing companies

it_companies.remove("Facebook")
print("After removing first:", it_companies)


it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
]

it_companies.remove("Apple")
print("After removing middle company:", it_companies)


it_companies.remove("Amazon")
print("After removing last:", it_companies)


# Remove everything

it_companies.clear()

print("After clear():", it_companies)


# Delete the complete list

it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
]

del it_companies


# ============================================================
# FRONT-END AND BACK-END
# ============================================================

front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]

front_end.extend(back_end)

print("Joined stack:", front_end)


# Copy the joined list

full_stack = front_end.copy()

# Insert Python and SQL after Redux.
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")

print("Full stack:", full_stack)


# ============================================================
# AGE EXERCISES
# ============================================================

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print("Sorted ages:", ages)
print("Minimum age:", min(ages))
print("Maximum age:", max(ages))


# Add minimum and maximum again

ages.append(min(ages))
ages.append(max(ages))

print("Ages after adding min and max:", ages)


# -------------------------
# Median
# -------------------------

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

sorted_ages = sorted(ages)

middle_1 = sorted_ages[len(sorted_ages) // 2 - 1]
middle_2 = sorted_ages[len(sorted_ages) // 2]

median_age = (middle_1 + middle_2) / 2

print("Median age:", median_age)


# -------------------------
# Average
# -------------------------

average_age = sum(ages) / len(ages)

print("Average age:", average_age)


# -------------------------
# Range
# -------------------------

age_range = max(ages) - min(ages)

print("Age range:", age_range)


# ============================================================
# COUNTRY EXERCISES
# ============================================================

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


# -------------------------
# Compare distance from average
# -------------------------

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

min_age = min(ages)
max_age = max(ages)
average_age = sum(ages) / len(ages)

value_1 = abs(min_age - average_age)
value_2 = abs(max_age - average_age)

print("Distance of minimum from average:", round(value_1, 1))
print("Distance of maximum from average:", round(value_2, 1))

if value_1 > value_2:
    print("Minimum age is farther from the average.")
else:
    print("Maximum age is farther from the average.")


# -------------------------
# Split countries
# -------------------------

countries = [
    "China",
    "Russia",
    "USA",
    "Finland",
    "Sweden",
    "Norway",
    "Denmark"
]

# If the number is odd, the first half gets one extra item.
middle = (len(countries) + 1) // 2

first_half = countries[:middle]
second_half = countries[middle:]

print("First half:", first_half)
print("Second half:", second_half)


# -------------------------
# Unpacking countries
# -------------------------

countries = [
    "China",
    "Russia",
    "USA",
    "Finland",
    "Sweden",
    "Norway",
    "Denmark"
]

first, second, third, *scandic_countries = countries

print("First:", first)
print("Second:", second)
print("Third:", third)
print("Scandic countries:", scandic_countries)


# ============================================================
# PART 2 - TUPLES
# ============================================================

# Tuples are ordered like lists,
# but their items cannot be changed after creation.


# -------------------------
# Creating Tuples
# -------------------------

empty_tpl = ()

print("Empty tuple:", empty_tpl)


tpl_1 = ("item 1", "item 2", "item 3")

print("Tuple:", tpl_1)


tpl_2 = ("mango", "banana", "kiwi", "apple")

print("Tuple length:", len(tpl_2))


# ============================================================
# TUPLE INDEXING
# ============================================================

tpl = ("value 1", "value 2", "value 3", "value 4")

first_value = tpl[0]
last_value = tpl[-1]

print("First value:", first_value)
print("Last value:", last_value)


# Negative indexing

print("Last value:", tpl[-1])
print("First value:", tpl[-4])


# ============================================================
# TUPLE SLICING
# ============================================================

tpl_numerals = (0, 1, 2, 3, 4, 5, 6, 7)

print("First four:", tpl_numerals[0:4])
print("From index 4:", tpl_numerals[4:])
print("Up to index 6:", tpl_numerals[:7])


# Negative slicing

print("Last four:", tpl_numerals[-4:])
print("Last three:", tpl_numerals[-3:])
print("Without last item:", tpl_numerals[:-1])


# ============================================================
# TUPLE TO LIST
# ============================================================

tpl = ("apple", "banana", "peach", "plum", "mango")

lst = list(tpl)

print("Tuple:", tpl)
print("Converted list:", lst)


# ============================================================
# MEMBERSHIP IN TUPLES
# ============================================================

tpl = ("apple", "banana", "peach", "plum", "mango")

print("Apple present?", "apple" in tpl)
print("Mango present?", "mango" in tpl)
print("Pineapple present?", "pine apple" in tpl)


# ============================================================
# JOINING TUPLES
# ============================================================

tpl_1 = ("Karachi", "Lahore", "Islamabad")
tpl_2 = ("Multan", "Faisalabad", "Malakand")

total_tpl = tpl_1 + tpl_2

print("Total tuple:", total_tpl)


# ============================================================
# DELETING TUPLES
# ============================================================

tpl_numerals = (0, 1, 2, 3, 4, 5)

del tpl_numerals


# ============================================================
# TUPLE EXERCISES - LEVEL 1
# ============================================================

empty_tpl = ()

print("Empty tuple:", empty_tpl)


siblings_tpl = ("Abeera", "Faiza", "Saif", "Haider")

print("Siblings:", siblings_tpl)


sisters_tpl = ("Abeera", "Faiza")
brothers_tpl = ("Haider", "Saif")

sibling_tpl = sisters_tpl + brothers_tpl

print("All siblings:", sibling_tpl)

print("Number of siblings:", len(sibling_tpl))


parents_tpl = ("Iftikhar", "Shabana")

family_members = sibling_tpl + parents_tpl

print("Family members:", family_members)


# ============================================================
# TUPLE EXERCISES - LEVEL 2
# ============================================================

family_members = (
    "Abeera",
    "Faiza",
    "Saif",
    "Haider",
    "Iftikhar",
    "Shabana"
)

# *siblings collects all remaining values into a list.
*siblings, father, mother = family_members

print("Siblings:", siblings)
print("Father:", father)
print("Mother:", mother)


# -------------------------
# Food tuples
# -------------------------

fruits = ("mango", "apple", "banana", "peach", "plum")
vegetables = ("carrot", "radish", "pea", "potato")
animal_products = ("milk", "cheese", "butter", "meat")

food_stuff_tp = fruits + vegetables + animal_products

print("Food tuple:", food_stuff_tp)


# Convert tuple to list

food_stuff_lt = list(food_stuff_tp)

print("Food list:", food_stuff_lt)


# Find middle item

middle_food = len(food_stuff_tp) // 2

print("Middle tuple item:", food_stuff_tp[middle_food])
print("Middle list item:", food_stuff_lt[middle_food])


# First three and last three

print("First three:", food_stuff_lt[:3])
print("Last three:", food_stuff_lt[-3:])


# Check items

print("Is carrot present?", "carrot" in food_stuff_lt)
print("Is cheese present?", "cheese" in food_stuff_lt)


# Delete tuple

del food_stuff_tp


# -------------------------
# Nordic countries
# -------------------------

nordic_countries = (
    "Denmark",
    "Finland",
    "Iceland",
    "Norway",
    "Sweden"
)

print("Is Estonia Nordic?", "Estonia" in nordic_countries)
print("Is Iceland Nordic?", "Iceland" in nordic_countries)


# ============================================================
# PART 3 - SETS
# ============================================================

# Sets store unique values.
# Sets are unordered, so their printed order may change.


# IMPORTANT:
# {} creates an empty dictionary, NOT an empty set.
empty_set = set()

print("Empty set:", empty_set)


# Creating a set

st = {"mango", "banana", "peach", "apple"}

print("Fruit set:", st)


# ============================================================
# SET LENGTH AND MEMBERSHIP
# ============================================================

st_1 = {0, 1, 2, 3, 4, 5, 6, 7}

print("Set length:", len(st_1))


float_st = {3.12, 2.3, 9.8, 5.7}

print("Is 3.14 present?", 3.14 in float_st)
print("Is 5.7 present?", 5.7 in float_st)


# ============================================================
# ADDING ITEMS TO SETS
# ============================================================

st_value = {"value 1", "value 2", "value 3", "value 4"}

st_value.add("value 5")

print("After add():", st_value)


# update() adds multiple items.

fruits = {"apple", "mango", "banana"}
vegetables = {"cabbage", "carrot"}

fruits.update(vegetables)

print("Updated fruit set:", fruits)


# ============================================================
# REMOVING ITEMS FROM SETS
# ============================================================

float_st = {3.12, 2.3, 9.8, 5.7}

float_st.remove(3.12)

print("After remove():", float_st)


# pop() removes an arbitrary item from a set.

st_1 = {0, 1, 2, 3, 4, 5, 6, 7}

removed_value = st_1.pop()

print("Removed item:", removed_value)
print("Set after pop():", st_1)


# clear()

st = {"Ali", "Amna", "Abeera"}

st.clear()

print("After clear():", st)


# del

numerals_st = {0, 1, 2, 3, 4, 5, 6, 7}

del numerals_st


# ============================================================
# LIST TO SET
# ============================================================

lst = ["item 1", "item 2", "item 3", "item 4"]

st = set(lst)

print("Converted set:", st)


# ============================================================
# SET UNION
# ============================================================

name_st = {"Ali", "Amna", "Abeera"}
age_st = {25, 14, 37}

print("Union:", name_st.union(age_st))


# update() modifies the original set.

subject_st = {"English", "Urdu", "Anatomy"}
marks_st = {76, 98, 83}

subject_st.update(marks_st)

print("Updated set:", subject_st)


# ============================================================
# SET INTERSECTION
# ============================================================

even_numbers = {2, 4, 6, 8, 10, 12, 14}
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8}

print("Common numbers:", even_numbers.intersection(whole_numbers))


# ============================================================
# SUBSET AND SUPERSET
# ============================================================

item_st = {"item 1", "item 2", "item 3", "item 4"}
product_st = {"item 2", "item 4"}

# product_st is inside item_st.
print("Is product_st a subset?", product_st.issubset(item_st))

print("Is item_st a superset?", item_st.issuperset(product_st))


# ============================================================
# SET DIFFERENCE
# ============================================================

a_st = {0, 1, 2, 3, 4, 5, 6}
b_st = {1, 2, 3, 4, 5, 6, 7, 8}

print("A - B:", a_st.difference(b_st))
print("B - A:", b_st.difference(a_st))


# ============================================================
# SYMMETRIC DIFFERENCE
# ============================================================

whole_st = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
int_st = {1, 2, 3, 4, 5, 6, 7, 8}

print(
    "Symmetric difference:",
    int_st.symmetric_difference(whole_st)
)


# ============================================================
# DISJOINT SETS
# ============================================================

a_st = {0, 1, 2, 3, 4, 5, 6}
b_st = {1, 2, 3, 4, 5, 6, 7, 8}

print("Are sets disjoint?", a_st.isdisjoint(b_st))


# ============================================================
# SET EXERCISES - LEVEL 1
# ============================================================

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


it_companies.add("Twitter")

print("After adding Twitter:", it_companies)


enterprises = {"Tech", "Udemy", "Coursera"}

it_companies.update(enterprises)

print("After adding multiple companies:", it_companies)


it_companies.remove("Oracle")

print("After removing Oracle:", it_companies)


# remove() gives an error if the item does not exist.
# discard() does not give an error if the item does not exist.

it_companies.discard("Twitter")
it_companies.discard("Twitter")

print("After discard():", it_companies)


# ============================================================
# SET EXERCISES - LEVEL 2
# ============================================================

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


# Union

union_set = A.union(B)

print("A union B:", union_set)


# Intersection

print("A intersection B:", A.intersection(B))


# Subset

print("Is A a subset of B?", A.issubset(B))


# Disjoint

print("Are A and B disjoint?", A.isdisjoint(B))


# Union works the same way in either direction.

print("A union B:", A.union(B))
print("B union A:", B.union(A))


# Symmetric difference

print(
    "Symmetric difference:",
    A.symmetric_difference(B)
)


# Delete sets

del A
del B


# Repeat the exercises after recreating the sets

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print("Is A a subset of B?", A.issubset(B))
print("Are A and B disjoint?", A.isdisjoint(B))

print("A union B:", A.union(B))
print("B union A:", B.union(A))

print(
    "Symmetric difference:",
    A.symmetric_difference(B)
)

del A
del B


# ============================================================
# SET EXERCISES - LEVEL 3
# ============================================================

age = [22, 19, 24, 25, 26, 24, 25, 24]

age_set = set(age)

print("Unique ages:", age_set)

print("Length of age list:", len(age))
print("Length of age set:", len(age_set))


if len(age) > len(age_set):
    print("The list has more items.")
else:
    print("The set has more items.")


# ============================================================
# DIFFERENCE BETWEEN DATA TYPES
# ============================================================

# String:
# Stores text and is immutable.
#
# List:
# Ordered, changeable collection.
#
# Tuple:
# Ordered, unchangeable collection.
#
# Set:
# Unordered collection of unique values.


# ============================================================
# UNIQUE WORDS EXERCISE
# ============================================================

sentence = "I am a teacher and I love to inspire and teach people."

# Remove the full stop.
sentence = sentence.replace(".", "")

# Split the sentence into words.
words = sentence.split()

# Convert the words into a set to remove duplicates.
unique_words = set(words)

print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))

# ==========================================
# DAY 11 COMPLETE
# ==========================================