

# list 

print('hello world')

users = ['prince', 'john', 'sara']

data = ['dave', 43, True]

emptylist = []

print(users[0])
print(users[-2])
print(users[1])
print(users.index('sara'))
print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))
# this will add the item to the end o the array or list 
users.append('liva')
print(users)

users += ['jason']
print(users)

# this will add the item to the end o the array or list 
users.extend(['Robert ', 'jimmy'])
print(users)

users.extend(data)
print(users)

# this  add some value in the begining of the liist
users.insert(0, 'Bob')
print(users)

# this is adding the item in the or at the second position in the list
users[2:2] = ['eddie', 'Alex']
print(users)

# this is to replace value in the list 
users[1:3] = ['Robert', 'jpj']
print(users)

# how to remove item
users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] =['dava']
print(users)


users.sort(key=str.lower)
print(users)







nums = [4,56,67,8,98,65,2]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

print(sorted(nums, reverse=True))

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)


print(type(nums))

mylist = list([1, 'Neil', True])
print(mylist)


# Tuples

# there are read only propertices the the value inside can not change

mytuple = tuple(('Dave', 43,True))
anothertuple =(1,7,2,6,8)

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one ,two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple)
