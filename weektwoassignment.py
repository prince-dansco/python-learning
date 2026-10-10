# 1. using str, int, bool assign a value to it based on the data
#  type then display the type and the
#  value assigned.

stringValue = 'Princewill'
# print(f"Value: {stringValue}, Type: {type(stringValue)}")

numericValue = 100
# print(f"Value: {numericValue}, Type: {type(numericValue)}")

is_single = True


# print(f"Value: {is_single}, Type: {type(is_single)}")

#  using a dictionary list, store different 
#  values with different data types and display
# them using print statements.

# dict

product = {
    "id":1,
    "name":"watch",
    "description":"Dansco tech Watch",
    "price": 345.99,
    "is_active":True
}

# list
nums = [2,3,4,6,7,8,9,]


# print(f"Value: {product}, Type: {type(product)}")
# print(f"Value: {nums}, Type: {type(nums)}")

# Arithmetic Operators

x = 6
y = 20
 
t = y + x 
r = y - x
u = y * x
p = y / x
s = y ** x
w = y % x

# print(f"Arithmetic Operators  {t}, {u}, {r},{s},{p},{w}")
# Comparison Operators
a = y == x 
b = y <= x
c = y >= x
d = y > x
e = y < x
g = y != x

# print(f" comparison operator {a},{b},{c},{d},{e},{g}")

# Logical Operators

age = 50

#  True if at least one condition is True
if age > 34 or age < 100:
    print("Age is either > 34 OR < 100 (or both)")

# AND operator - True ONLY if BOTH conditions are True
if age < 34 and age > 40: 
    print("This will never print")
    
#  AND condition - age between 34 and 40?
if age > 34 and age < 40:
    print("Age is between 34 and 40 (exclusive)")

# NOT operator - negates a condition
if not age > 40:  # This means: if age is NOT greater than 40
    print("Age is 40 or less")


# Demonstrate your understanding of conditional statements by using
#  if, elif, and else to build decision-making logic.


grad = int(input("Enter your score (0-100): "))

if 90 <= grad <= 100:
    print("Excellent")
elif 70 <= grad <= 89:
    print("Good")
elif 50 <= grad <= 69:
    print("Average")
elif 0 <= grad <= 49:
    print("Fail")
else:
    print(" Enter number between 0 and 100")




#  Use for and while loops to iterate over
#  sequences and perform repeated actions
#  in Python.

for i in range(1,21):
    print(i)

for i in range(2, 21, 2):
    print(i)
     

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

i = 5
while i >= 1:
    print(i)
    i -= 1

