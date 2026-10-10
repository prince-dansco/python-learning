# Dictionary

band = {
    'vocals':'plant',
    'prit': 'page'
}

band2 = dict(vocals='plant', jfhffn='page')

print(band)
print(band2)
print(type(band))
print(len(band))

# access item
print(band['vocals'])
print(band['prit'])

# list all key
# print(band.key())

# list all value
print(band.values())

print('vocals' in band)

# change values
band['vocals'] = ' lanmp'

band.update({'bass': 'jpj'})
print(band)

print(band.pop('bass'))
print(band)

band['drums'] = 'bonham'
print(band)


# to tuple
print(band.popitem())
print(band)


band['drums'] = 'Bonham'
del band['drums']
print(band)

band2.clear()
print(band2)

del band2

# copy dictionary
# create a reference
# band2 = band 
# print('Bad copy')
# print(band2)
# print(band)

# band2['drums'] = 'Dave'

band2 = band.copy()
band2['drums'] = 'Dave'
print('Good copy')
print(band)
print(band2)

# nested dictionries
member1 ={
    'name':'princewill',
    'instrument':'vocals'
}
member2 ={
    'name':'page',
    'instrument':'guitar'
}

band ={
    'member1': member1,
    'member2': member2


}

print(band)
print(band[member1]['name'])


# sets
nums = {8,1,2,3,4}
num2 = set((,1,2,3,4))
print(nums)
print(num2)
print(type(num2))
print(len(num2))

# no duplicate are allowed
nums = {1,2,2,3}
print(nums)


# True is dupe of 1 , False is a dupe of zero
nums ={1,True, 2 , False, 3,4,0}
print(nums)

# check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set with an index position or a key

# add a new element to a set
nums.add(8)
print(nums)

# add element from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# you can use update with the list ,tuples and dic too

# merge two sets to creat a new set

one ={1,2,3}
two = {5,6,7}
mynewset = one.union(two)
print(mynewset)

# keep only the duplicate
one ={1,2,3}
two = {2,6,7}

one.intersection_update(two)
print(one)

# keep everything except the duplicate
one ={1,2,3}
two = {2,6,7}

one.symmetric_difference_update(two)
print(one)