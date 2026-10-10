from utilities  import square, cube

# *************************************************************************
# Task 1: Variables and Data Types
# Create variables for:

# Your favorite movie
# Your favorite musician
# Your age
# Whether you own a computer (True or False)
# Print all the variables with descriptive messages.

# Task 2: Operators
# Given:

# a = 18
# b = 6Perform and display:

# Addition
# Subtraction
# Multiplication
# Division
# Comparison (a >= b)
# Logical operation (a > 10 and b < 10)


# Task 3: Conditional Statements
# Write a program that accepts a student's score and displays:

# "A" for scores 70 and above
# "B" for scores 60–69
# "C" for scores 50–59
# "F" for scores below 50


# Task 4: Loops
# Part A
# Use a for loop to print numbers from 10 to 20.
# Part B
# Use a while loop to print the first 10 odd numbers.

# Module 3: Functions and Modules
# Task 5: Defining Functions
# Create a function:

# def calculate_area(length, width):The function should return the area of a rectangle.
# Call the function with different values and print the results.

# Task 6: Function Arguments and Default Values
# Create a function:

# def introduce_student(name, course="Python Programming"):The function should display:
# Student Name: John
# Course: Python ProgrammingCall the function:

# Using only the student's name.
# Using both the student's name and a custom course.


# Task 7: Custom Modules
# Create a file named:
# utilities.pyAdd the following functions:

# def square(number):
#     return number * number

# def cube(number):
#     return number * number * numberCreate another file named:
# main.pyImport the functions from utilities.py and use them to calculate:

# The square of 8
# The cube of 4




# Your favorite movie
# Your favorite musician
# Your age
# Whether you own a computer (True or False)
# Print all the variables with descriptive messages.

# favorite ={
#     "movie": ""
# }


# Task 1: Variables and Data Types
# # Create variables for:
favorite_movie = "action movie"

favorite_musician= "Dusin oyenka"

age= 38

is_computer = True

print(f'i love {favorite_movie} and {favorite_musician} songs and am {age} i have a  labtop {is_computer}')


# a = 18
# b = 6Perform and display:

# Addition
# Subtraction
# Multiplication
# Division
# Comparison (a >= b)
# Logical operation (a > 10 and b < 10)

a = 18
b = 6

r = b + a
z = b - a
w = b / a
l = b * a
y = b ** a

print(f'{r}  and {z} with {w} also {l} and {y}')

p = a >= b
print(p)

if a > 10 and  b< 10:
    print("true")


    
# Task 4: Loops
# Part A
# Use a for loop to print numbers from 10 to 20.
# Part B
# Use a while loop to print the first 10 odd numbers.

# 

# Using only the student's name.
# Using both the student's name and a custom course.


# Use a for loop to print numbers from 10 to 20.
list = [10,11,12,13,14,15,16,17,18,19,20]
for i in list:
    print(i)

# Use a while loop to print the first 10 odd numbers.
i = 1
while i <= 10:
    print(i)
    i += 2
    # i = i + 2

# module 3: Functions and Modules
# Task 5: Defining Functions
# Create a function:

# def calculate_area(length, width):The function should return the area of a rectangle.
# Call the function with different values and print the results.

# Task 6: Function Arguments and Default Values
# Create a function:

# def introduce_student(name, course="Python Programming"):The function should display:
# Student Name: John
# Course: Python ProgrammingCall the function:

def calculate_area(length, width):
    return length * width

result1 =  calculate_area(23,4)  
result2 =  calculate_area(50,2) 
print(result1, result2) 



def introduce_student(name, course="Python Programming"):
    print(f'my name {name} and am studing {course}')

introduce_student('princewill')    




# Task 7: Custom Modules
# Create a file named:
# utilities.pyAdd the following functions:

# def square(number):
#     return number * number

# def cube(number):
#     return number * number * numberCreate another file named:
# main.pyImport the functions from utilities.py and use them to calculate:

# The square of 8
# The cube of 4

print(square(8))
print(cube(4))



# Task 3: Conditional Statements
# Write a program that accepts a student's score and displays:

# "A" for scores 70 and above
# "B" for scores 60–69
# "C" for scores 50–59
# "F" for8 scores below 50

score = 80

if score >= 70:
    print("A")
elif score >= 60 or score >= 69:
    print("B")    
elif score >= 50 or score >= 59:
    print("C")
elif score <= 50:
    print("F")
else:
    print("try again next year")    