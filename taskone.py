# Task 1: Variables and Data Types
# Create variables for:

# Your name
# Your age
# Your favorite food
# Whether you like programming (True or False)
# Print all the variables.

my_name = "princewill"

print(my_name)

age = 12
print(age)

favorite_food = "chicken"
print(favorite_food)


like_programming = True
print(like_programming)


# Given:

# a = 12
# b = 4Display:

# Sum
# Difference
# Product
# Quotient


a = 12
b = 4

x = a + b
print(x)

y = a / b
print(y)

z = a * b
print(z)

w = a - b
print(w)



# Task 3: Conditional Statements
# Write a program that accepts a score and prints:

# "Excellent" if score is 80 or above
# "Good" if score is between 60 and 79
# "Needs Improvement" otherwise


score = 79
if score >= 80:
    print("Excellent")
elif score <= 60 or score  <= 79:
    print("Good")
else:
    print("Needs Improvement")


#     Task 4: Loops
# Print numbers from 1 to 10 using a for loop.

list = [1,2,3,4,5,6,7,8,9,10]

for i in list:
    print(i)


#     Task 5: Functions
# Create a function called greet() that prints "Welcome to Python".
# Task 6: Function Arguments
# Create a function student(name) that prints:


def  greet():
    print("Welcome to Python")

greet()


def  student(name):
    print(f'Hello welcome to Python {name}')

student("prince")

