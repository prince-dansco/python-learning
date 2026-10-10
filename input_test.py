# from functions import reduce


# x = int(input("Enter first nuber"))

# y = int(input("Enter second nuber"))

# z = x + y

# print(z)

# ch = input("enter a char")[0]
# print(ch)
# ch = input("enter a char")[0]
# print(ch)

# i = 1
# while i <=5:
#     print("youtube ", end="" )
#     j = 1
#     while j<=4:
#         print("books ", end="")
#         j =j+1
#     i = i +1
#     print()

# x = "  PRINCE"

# for i in x:
#     print(i)

# av = 5
# x = int(input("how many cadies you want?"))

# i = 1
# while i <= x:
#     if i > av:
#         print("out of stock")
#         break
#     print("💥")
#     i += 1


# for i in range(1, 101):
#     if i % 3 == 0 or i % 5==0:
#         continue

#          print(i) 


# for i in range(4):        
#     for j in range(4):    
#         print("# ", end="") 
#     print()    

# for i in range(4):        
#     for j in range(4 + i):    
#         print("# ", end="") 
#     print()    
# for i in range(4):        
#     for j in range(i + 1):    
#         print("# ", end="") 
#     print()    




# nums = [ 12,16,21,26, 26]

# for num in nums:
#     if num % 5 == 0:
#         print(num)
#         break 
# else:
#         print("not found")    


# def fib(n):
#     a = 0
#     b= 1

#     if n == 1:
#        print(a)
#     else:   
#        print(a)
#        print(b)

    # for i in range(2,n):


    #     c = a + b 
    #     a =b
    #     b =c
    #     print(c)


# fib(100)        

# factorial of  a number

# def fact(n):
#     f =1


#     for i in range(1,n + 1):
#         f = f * i
#      return f   



# x =4
# result = fact(x)

# print(result)


# recursion: is a function calling it self


# def fact(n):
#     if (n == 0):
#         return 1

#     return n * fact(n-1)


# result = fact(5)
# print(result)


# annanimose  function without a name

# f = lambda a: a*a

# result = f(5)

# print(result)

# def is_even(n):
#     return n % 2 == 0




# nums = [3,2,6,5,8,9]
# evens = list(filter(lambda n: n%2==0, nums))
# double = list(map( lambda n : n * 2, evens))
# sum = reduce(lambda a,b: a+b  , double)
# print(evens, double, sum)



# decorator


# def div(a,b):
#    print(a/b)

# def smart_div(func):

#     def inner(a,b):
#         if a<b:
#             a,b =b,a
#         return func(a,b)    

#     return inner

# div =smart_div(div) 

# div(2,4)   


# contructor function
# class computer:

#     def __init__(self,cpu , ram):
#         self.cpu =cpu
#         self.ram =ram
#         print('in init')

#     def config(self):
#         print("is 16gb 17b", self.cpu, self.ram)

# com1 = computer("is", 16)
# com2 = computer("Ryzen 3", 8)
# com1.config()
# com2.config()

# class computer:
#     def __init__(self):
#         self.name = "prince"
#         self.age = 26


#     def update(self):
#         self.age = 30

#     def compare(self, other):
#         if self.age == other.age:
#             return True    
#         else:
#             return False

# c1 = computer()      
# c2 = computer() 

# # c1.name = "akpan"
# # c1.age = 38
# if c1.compare(c2):
#     print("they are same")
# else:
#     print("they are different")


# c1.update()

# print(c1.name)     
# print(c2.name)     


# class car:
#     wheels = 4
#     def __init__(self):
#         self.mil = 10
#         self.com = BNW

# c1 = car()
# c2 = car()


# car.wheels = 8

# print()



# class student:
#     school = "Dansco Hub"
#     def __init__(self, m1, m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

    # def avg(self):
    #     return (self.m1 + self.m2 + self.m3)/ 3
    # def get_m1(self):
    #     return self.m1

    # def set_m1(self):
    #     return self.m1 = value
    # @classmethod
    # def get_school_name(cls):
    #     return cls.school

    # @staticmethod
    # def info():
    #     print("this is student class .. in abc molude")

    
# a1= student(34,67,32)
# a1= student(19,32,12)


# print(a1.avg())
# print(a1.get_school_name())
# print(a1.info())


# class pycham:
#     def execute(self):
#         print("compliling")
#         print("Running")



# class MyEditor:
#     def execute(self):
#         print("spell check")
#         print("convention check")
#         print("compliling")
#         print("Running")

# class labtop:

#     def code(self,ide):
#         ide.execute()

# ide = pycham()
# ide = MyEditor()


# lap1 = labtop()
# lap1.code(ide)



# class student:
#     def __init__(self, m1,m2):
    #     self.m1 =m1
    #     self.m2 =m2

    # def __add__(self, other):
    #     m1 = self.m1 = other.m1
    #     m2 = self.m2 = other.m2
    #     s3 = student(m1, m2)

    #     return s3
    #  def __gt__(self, other):
    #     r1 = self


# s1 = student(58,69)        
# s2 = student(78,99)        

# s3 =s1 + s2

# print(s3.m1)


# class Q:
#     def show(self):
#         print("in Q show")
# class P(Q):
#     def show(self):
#         print("in P show")
    
# a1 = P()
# a1.show()


# class computer():
#     def process(self):
#         pass

# nums = [8,2,3,4,5]
# print(next(nums))
# for i in nums:
#     print(i)

# iterator
# class TopTen:
#     def __init__(self):
#         self.num = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num <= 10:
#             val = self.num
#             self.num += 1
#             return val
#         else:
#             raise StopIteration

# values = TopTen()
 
# for i in values:
#     print(i)

# print(next(values))

# Generator

# def topten():
#     yield 1
#     yield 3
#     yield 5
#     yield 7

# values = topten()
# print(values.__next__())
# print(values.__next__())

# for i in values:
#     print(i)


# def topten():
#     n=1

#     while n <= 10:
#         sq = n * n
#         yield sq
#         n += 1

# values = topten()

# for i in values:
#     print(i)


# errors 
# there are three type of errors, runtimeError,compilingError,

# a =5
# b =2

# try:
#     print("resource open")
#     print(a/b)
#     k = int(input("Enter a number"))
#     print(k)
# except ZeroDivisionError as e:
#     print("not by zero", e) 
# except ValueError as e:
#     print("invalid input", e) 

# except Exception as e:
#     print('something went wrong')    
# finally:
#     print("resource closed")


# thread when you break down task into pieces it is called thread
# from time import  sleep
# from threading import *
# class Hello:
#     def run(Thread):
#         for i in  range(5):
#             print("Hello")
#             sleep(1)
# class Hi:
#     def run(Thread):
#         for i in  range(5):
#             print("Hi")
#             sleep(1)

# t1 = Hello()
# t2 = Hi()

# t1.start()
# sleep(0.2)
# t2.start()

# t1.join()
# t2.join()

# print("Bye")

# linear search♈♈

# pos = -1
# def search(list, n):
#     i = 0

#     while i< len(list):
#         if list[i] ==  n:
#             globals()['pos'] = i
#             return True
#         i = i + 1   
#     return False    

# list = [5,6,7,8,9,0]
# n = 9

# if search(list, n):
#     print("Found at",pos)  
# else:
#     print("Not Found")         


# binary search ♈♈
# all value must be sorted 

# pos = -1

# def search(list, n):
#     i =0
#     u = len(list)-1
    
#     while i <= u:
#         mid = (1+u) // 2 

#         if list[mid] == n:
#             globals()['pos'] = mid
#             return True
#         else:
#             if list[mid] < n:
#                 i = mid -1
#             else:
#                 s = mid + 1    
#     return False

# list = [4,6,78,89,97,65,43,23,21]
# n = 6

# if search(list, n):
#          print("Found at",pos)  
# else:
#        print("Not Found")
    

# bb search ♈♈
# swap iteration
# def sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j] > nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp



# nums= [5,6,8,2,56,73]
# sort(nums)

# print(nums)


# selection sort ♈♈

def sort(nums):

    for i in range(5):

        minIndex = i

        for j in range(i, 6):

            if nums[j] < nums[minIndex]:
                minIndex = j

        temp = nums[i]
        nums[i] = nums[minIndex]
        nums[minIndex] = temp

        print(nums)


nums = [5,3,8,6,7,2]

sort(nums)

print(nums)