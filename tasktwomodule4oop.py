# TASK TWO
# 2. Create a system to manage students in Futurelabs who are learning different tech skills. Using OOp.


# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
    #     self.age = age
    #     self.course = course

    # def introduce(self):
    #     print(f"Hello, my name is {self.name} and I am {self.age} years old. I am currently studying {self.course}.")

# student1 = Student('Jame', 34, 'python developer')  
# student2 = Student('John',  34,  'React developer')  
# student3 = Student('Joan', 64, 'Javascript developer')  
# student4 = Student('Joel',  42, 'php developer')  

# student1.introduce()
# student2.introduce()
# student3.introduce()
# student4.introduce()

class Student:
    def __init__(self, name, age, course, phone,attendance,remark,progress):
        self.name = name
        self.age = age
        self.course = course
        self.__phone = phone
        self.student_attendance = attendance
        self.student_remark = remark
        self.student_progress = progress
    def get_phone(self):
        return self.__phone

    def display_info(self):
        print(
            f"Hello, my name is {self.name} and I am {self.age} years old. "
            f"I am currently studying {self.course}."
        )

class FutureLabsStudent(Student):


    def attendance(self):
        print(f"Attendance: {self.student_attendance}%")

    def remark(self):
        print(f"Remark: {self.student_remark}")

    def progress(self):
        print(f"Progress: {self.student_progress}")


student1 = FutureLabsStudent(
    "James",
    34,
    "Python Developer",
    "08012345678",
    95,
    "Excellent",
    "Completed OOP"
)

student1.display_info()
student1.attendance()
student1.remark()
student1.progress()

print("Phone:", student1.get_phone())