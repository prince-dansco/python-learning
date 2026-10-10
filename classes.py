# 1.Task: Create a Simple Car Class
# Objective:
#  Understand and implement basic object-oriented programming concepts — specifically classes, objects, attributes, and methods. Using the attribute as variables, divide them separately into class variables and object variables.
# Instructions:
# Create a class called Car.
# Add the following attributes to the class:
# make (e.g., "Toyota")
# model (e.g., "Corolla")
# year (e.g., 2020)
# speed (default to 0)
# Add the following methods:
# accelerate() → increases the speed by 10.
# brake() → decreases the speed by 10 but not below 0.
# display_info() → prints out all the car's details including current speed.
# Create two different Car objects with different values.
# Call the methods on each object to demonstrate behavior (e.g., accelerate, brake, display info).

# TASK TWO
# 2. Create a system to manage students in Futurelabs who are learning different tech skills. Using OOp.







class Car:
    wheels = 4
    
    def __init__(self, make, model, year, speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
    
    def accelerate(self):
        self.speed += 10
    
    # def brake(self):
    #     self.speed -= 10
    #     if self.speed < 0:
    #         self.speed = 0

    def brake(self):
        while self.speed > 0:
            self.speed -= 2
    
    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Speed: {self.speed} km/h")
        print(f"Wheels: {Car.wheels}")
        print("-" * 30)


car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022, 30)


print("Car 1:")
car1.display_info()
car1.accelerate()
car1.accelerate()
print("After accelerating twice:")
car1.display_info()

print("\nCar 2:")
car2.display_info()
car2.brake()
print("After braking once:")
car2.display_info()









