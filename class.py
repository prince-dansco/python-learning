# Create a Python program for a school.
# Requirements
# Create a class called Person.
# Add the following attributes:
# name
# age
# Add a method called introduce() that prints:
# My name is John and I am 20 years old.
# Create a class called Student that inherits from Person.
# Add a new attribute called course.
# Override the introduce() method to display:
# My name is John.
# I am studying Python.

# Create a class called Teacher that inherits from Person.
# Override the introduce() method to display:
# I am Mr James.
# I teach Backend Development.
# Create objects for:
# One student
# One teacher
# Call the introduce() method for both objects.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cours = cours

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old. i am studying {self.cours}")
class Student(Person):
     

    
student1 = Student("John", 20, "Python")
student2 = Student("Jame", 60, "javascript")
teacher = Teacher("James", 40, "Backend Development")

student1.introduce()
student2.introduce()
teacher.introduce()