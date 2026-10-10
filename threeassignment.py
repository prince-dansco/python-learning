# Define a function called "calculate_average" that accepts a 
# list of numbers as input. The function should calculate the average of these numbers and return
#  the result. If the input list is empty, the function should return 0.





def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)


user_input = input("Enter numbers separated by spaces: ")

numbers = [float(num) for num in user_input.split()]
result = calculate_average(numbers)

print("Average:", result)
