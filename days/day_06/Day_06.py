# Day 6 - Python Dictionaries


# -----------------------------------------
# 1. Creating a dictionary
# -----------------------------------------
# A dictionary stores data in key:value pairs.
#
# Example:
# "name" is the key
# "Izza" is the value

person = {
    "first_name": "Ayesha",
    "last_name": "Ali",
    "age": 19,
    "country": "Pakistan",
    "skills": "JavaScript"
}

print("Dictionary:", person)


# -----------------------------------------
# 2. Finding the length of a dictionary
# -----------------------------------------
# len() tells us how many key-value pairs
# are stored in the dictionary.

print("Length:", len(person))


# -----------------------------------------
# 3. Accessing dictionary items
# -----------------------------------------
# We can access a value by using its key
# inside square brackets.

print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["country"])
print(person["skills"])


# -----------------------------------------
# 4. Using get() to access dictionary items
# -----------------------------------------
# get() can also be used to access a value.

print(person.get("first_name"))
print(person.get("age"))


# -----------------------------------------
# 5. Using get() for a key that does not exist
# -----------------------------------------
# If the key does not exist, get() returns None
# instead of causing an error.

print(person.get("city"))
print(person.get("subject"))


# -----------------------------------------
# 6. Adding items to a dictionary
# -----------------------------------------
# We can add a new key-value pair by using
# a new key.

person["job"] = "Developer"
person["experience"] = "5 years"

print(person)


# -----------------------------------------
# 7. Modifying existing dictionary items
# -----------------------------------------
# If the key already exists, assigning a new
# value changes the existing value.

person["first_name"] = "Faiza"
person["job"] = "Designer"

print(person)


# -----------------------------------------
# 8. Checking if a key exists
# -----------------------------------------
# The 'in' operator checks whether a key
# exists in a dictionary.

print("job" in person)
print("city" in person)


# -----------------------------------------
# 9. Copying a dictionary
# -----------------------------------------
# copy() creates a separate copy of the dictionary.

person_copy = person.copy()

print("Copied dictionary:", person_copy)


# -----------------------------------------
# 10. Removing an item using pop()
# -----------------------------------------
# pop() removes the specified key and its value.

person.pop("first_name")

print(person)


# -----------------------------------------
# 11. Removing the last item using popitem()
# -----------------------------------------
# popitem() removes the last inserted
# key-value pair.

person.popitem()

print(person)


# -----------------------------------------
# 12. Deleting a specific key using del
# -----------------------------------------
# del can be used to remove a specific
# key-value pair.

del person["last_name"]

print(person)


# -----------------------------------------
# 13. Getting dictionary items
# -----------------------------------------
# items() returns the dictionary's
# key-value pairs.

print(person.items())


# -----------------------------------------
# 14. Getting dictionary keys
# -----------------------------------------
# keys() returns all the keys.

print(person.keys())


# -----------------------------------------
# 15. Getting dictionary values
# -----------------------------------------
# values() returns all the values.

print(person.values())


# -----------------------------------------
# 16. Clearing a dictionary
# -----------------------------------------
# clear() removes all items from the dictionary.

person.clear()

print(person)


# -----------------------------------------
# 17. Creating another dictionary
# -----------------------------------------

data = {
    "key1": "value1",
    "key2": "value2"
}

print(data)


# -----------------------------------------
# 18. Getting dictionary values
# -----------------------------------------

values = data.values()

print(values)


# -----------------------------------------
# 19. Getting dictionary keys
# -----------------------------------------

keys = data.keys()

print(keys)


# -----------------------------------------
# 20. Converting dictionary keys to a list
# -----------------------------------------
# list() converts the dictionary view
# into an actual list.

keys_list = list(data.keys())

print(keys_list)


# -----------------------------------------
# 21. Converting dictionary values to a list
# -----------------------------------------

values_list = list(data.values())

print(values_list)

print(type(values_list))


# -----------------------------------------
# 22. Simple dictionary practice
# -----------------------------------------
# Let's create a small dictionary
# and access its values.

book = {
    "title": "Python Basics",
    "author": "John",
    "pages": 200
}

print("Book title:", book["title"])
print("Book author:", book["author"])
print("Book pages:", book["pages"])


# -----------------------------------------
# 23. Creating an empty dictionary
# -----------------------------------------

dog = {}

print("Dog dictionary:", dog)


# -----------------------------------------
# 24. Adding items to the dog dictionary
# -----------------------------------------

dog["name"] = "Tom"
dog["color"] = "Brown"
dog["breed"] = "German Shepherd"
dog["legs"] = 4
dog["age"] = 2

print(dog)


# -----------------------------------------
# 25. Creating a student dictionary
# -----------------------------------------
# A dictionary can contain different data types.
# The skills value is a list because a student
# can have multiple skills.

student = {
    "first_name": "Ali",
    "last_name": "Hassan",
    "gender": "Male",
    "age": 23,
    "marital_status": False,
    "skills": ["JavaScript", "CSS"],
    "country": "Pakistan",
    "city": "Lahore",
    "address": "Johar Town"
}

print(student)


# -----------------------------------------
# 26. Getting the length of the dictionary
# -----------------------------------------

print("Student dictionary length:", len(student))


# -----------------------------------------
# 27. Getting the student's skills
# -----------------------------------------

print(student["skills"])


# -----------------------------------------
# 28. Checking the type of skills
# -----------------------------------------
# The value stored under "skills" is a list.

print(type(student["skills"]))


# -----------------------------------------
# 29. Adding skills to the skills list
# -----------------------------------------
# Because "skills" contains a list,
# we can use list methods such as append().

student["skills"].append("Python")
student["skills"].append("HTML")

print(student)


# -----------------------------------------
# 30. Getting dictionary keys as a list
# -----------------------------------------

student_keys = list(student.keys())

print(student_keys)


# -----------------------------------------
# 31. Getting dictionary values as a list
# -----------------------------------------

student_values = list(student.values())

print(student_values)


# -----------------------------------------
# 32. Converting dictionary items to a list
# -----------------------------------------
# items() gives us key-value pairs.
#
# Each pair is represented as a tuple.

solution = {
    "key1": "value1",
    "key2": "value2"
}

print(solution.items())

items_list = list(solution.items())

print(items_list)


# -----------------------------------------
# 33. Deleting an item from a dictionary
# -----------------------------------------

student_2 = {
    "first_name": "Ali",
    "last_name": "Hassan",
    "gender": "Male",
    "age": 23,
    "marital_status": False
}

del student_2["marital_status"]

print(student_2)


# -----------------------------------------
# 34. Deleting a complete dictionary
# -----------------------------------------
# del can also delete the entire dictionary.

student_3 = {
    "first_name": "Ali",
    "last_name": "Hassan",
    "gender": "Male",
    "age": 23,
    "marital_status": False
}

del student_3


# -----------------------------------------
# 35. Final dictionary practice
# -----------------------------------------
# Let's practice adding, changing, and
# accessing dictionary values.

profile = {
    "name": "Izza",
    "age": 20,
    "language": "Python"
}

# Add a new item
profile["level"] = "Beginner"

# Change an existing item
profile["age"] = 21

# Access values
print("Name:", profile["name"])
print("Age:", profile["age"])
print("Language:", profile["language"])
print("Level:", profile["level"])

# Check whether a key exists
print("language" in profile)
print("city" in profile)

# ==========================================
# DAY 6 COMPLETE
# ==========================================