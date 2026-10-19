# Day 10 - Python Conditionals


# -----------------------------------------
# 1. What are Conditionals?
# -----------------------------------------
# Conditionals allow Python to make decisions.
#
# Python checks a condition.
# If the condition is True, the code runs.
# If it is False, Python can check another condition
# or run an else block.


# -----------------------------------------
# 2. if Condition
# -----------------------------------------
# The if statement runs when its condition is True.

a = 4

if a > 0:
    print("a is greater than 0")


# -----------------------------------------
# 3. if-else Condition
# -----------------------------------------
# else runs when the if condition is False.

r = 6

if r > 0:
    print("r is greater than 0")
else:
    print("r is smaller than or equal to 0")


# -----------------------------------------
# 4. if-elif-else Condition
# -----------------------------------------
# elif means "else if".
# It allows us to check another condition.

e = 5

if e > 0:
    print("e is greater than 0")
elif e < 0:
    print("e is smaller than 0")
else:
    print("e is equal to 0")


# -----------------------------------------
# 5. Shorthand if-else
# -----------------------------------------
# A simple if-else can be written on one line.
#
# This is also called a conditional expression.

a = 7

print("a is positive" if a > 0 else "a is not positive")


# -----------------------------------------
# 6. Nested Conditions
# -----------------------------------------
# A nested condition means putting one if statement
# inside another if statement.

a = 4

if a > 0:

    if a % 2 == 0:
        print("a is divisible by 2")
    else:
        print("a is not divisible by 2")

elif a < 0:
    print("a is a negative number")

else:
    print("a is equal to 0")


# -----------------------------------------
# 7. Using AND
# -----------------------------------------
# The 'and' operator means ALL conditions must be True.

marks = 89

if marks >= 90 and marks % 2 == 0:
    print("Grade: A")
elif marks >= 80 and marks % 2 == 0:
    print("Grade: B")
else:
    print("Grade: C")


# -----------------------------------------
# 8. Using OR
# -----------------------------------------
# The 'or' operator means at least ONE condition
# must be True.

a = 7

if a > 0 or a == 0:
    print("a is greater than or equal to 0")
elif a < 0:
    print("a is smaller than 0")


# -----------------------------------------
# 9. Using NOT
# -----------------------------------------
# 'not' reverses a Boolean value.
#
# True becomes False.
# False becomes True.

access_denied = True

if not access_denied:
    print("Access is granted.")
else:
    print("Access is denied.")


# -----------------------------------------
# 10. Simple Condition Practice
# -----------------------------------------

number = 10

if number > 5:
    print("Number is greater than 5")

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# -----------------------------------------
# Important Notes
# -----------------------------------------
#
# if checks a condition.
#
# else runs when the if condition is False.
#
# elif checks additional conditions.
#
# Conditions evaluate to True or False.
#
# Python executes the first matching if/elif block.
#
# Indentation is mandatory in Python.


# =========================================
# Exercises - Level 1
# =========================================


# -----------------------------------------
# 11. Check Driving Age
# -----------------------------------------
# Get the user's age using input().
#
# If the user is 18 or older:
# "You are old enough to drive."
#
# Otherwise, tell them how many years they need to wait.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive.")
else:
    years_left = 18 - age
    print(f"Wait for {years_left} more years to drive.")


# -----------------------------------------
# 12. Compare Two Numbers
# -----------------------------------------
# Get two numbers from the user.

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print("A is greater than B.")
elif a < b:
    print("A is smaller than B.")
else:
    print("A is equal to B.")


# -----------------------------------------
# 13. Compare Two Ages
# -----------------------------------------
# Compare my_age with the user's age.

my_age = 25

your_age = int(input("Enter your age: "))

if my_age > your_age:

    difference = my_age - your_age

    if difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {difference} years older than you.")

elif your_age > my_age:

    difference = your_age - my_age

    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {difference} years older than me.")

else:
    print("We are the same age.")


# =========================================
# Exercises - Level 2
# =========================================


# -----------------------------------------
# 14. Give a Grade According to Marks
# -----------------------------------------
# The conditions should be checked from the
# highest score range to the lowest.

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks.")

elif marks >= 90:
    print("Grade A++")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 50:
    print("Grade D")

else:
    print("Grade F")


# -----------------------------------------
# 15. Find the Season
# -----------------------------------------
# Check the month and determine its season.

month = input("Enter month: ").strip().capitalize()

if month in ["September", "October", "November"]:
    print("Autumn")

elif month in ["December", "January", "February"]:
    print("Winter")

elif month in ["March", "April", "May"]:
    print("Spring")

elif month in ["June", "July", "August"]:
    print("Summer")

else:
    print("Invalid month.")


# -----------------------------------------
# 16. Check a Fruit
# -----------------------------------------
# If the fruit already exists, tell the user.
# Otherwise, add it to the list.

fruits = ["banana", "orange", "mango", "lemon"]

fruit = input("Enter a fruit: ").lower()

if fruit in fruits:
    print("That fruit already exists in the list.")

else:
    fruits.append(fruit)
    print("Modified list:", fruits)


# =========================================
# Self-Practice
# =========================================


# -----------------------------------------
# 17. Store Student Information
# -----------------------------------------
# A dictionary can store information using
# key-value pairs.

student = {
    "Name": "Ali",
    "Age": 19,
    "City": "Faisalabad"
}

print("Student:", student)


# -----------------------------------------
# 18. Store Favorite Colors
# -----------------------------------------
# A tuple can store multiple values.

colors = ("Red", "Blue", "White")

print("Favorite colors:", colors)


# -----------------------------------------
# 19. Check for Mango
# -----------------------------------------
# 'in' can also be used with tuples.

fruits = ("Apple", "Banana", "Peach", "Mango", "Plum")

if "Mango" in fruits:
    print("You like mangoes!")
else:
    print("No mango found!")


# -----------------------------------------
# 20. Check if a Number is Positive,
#     Negative, or Zero
# -----------------------------------------

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")

elif number < 0:
    print("The number is negative.")

else:
    print("The number is zero.")


# -----------------------------------------
# 21. Check if a Number is Even or Odd
# -----------------------------------------
# A number is even when its remainder after
# division by 2 is zero.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# -----------------------------------------
# 22. Simple Login Check
# -----------------------------------------
# This combines strings with conditionals.

correct_password = "python123"

password = input("Enter password: ")

if password == correct_password:
    print("Login successful.")
else:
    print("Incorrect password.")

# ==========================================
# DAY 10 COMPLETE
# ==========================================