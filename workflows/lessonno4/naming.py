import math

# string data type


# literal assignment

first = 'princewill'
last = 'okon'

print(type(first))
print(type(first) == str)
print(isinstance(first, str))
# print(type(first))

# contructor function

pizza = str('pepperoni')

print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))


# concatenation
fullname = first + "" + last
print(fullname)
fullname += '!'
print(fullname)

# casting a number toa string
decade = str(1980)
print(type(decade))
print(decade)

statment =  'i like rock music from the ' + decade + 's.'
print(statment)


# multiple line
multiline = ''' 
Hey, how are you?

 I was just checking in. 
                             All good?
'''

print(multiline)


# escaping special characters
sentence = 'I\'m back at work!\tHey!\nWhere\'s this at\\located?'
print(sentence)



# string method
print(first)
print(first.lower())
print(first.upper())



print(multiline.title())
print(multiline.replace('good', 'ok'))
print(multiline)



print(len(multiline))
multiline += "                     "
multiline  = '         '+ multiline
print(multiline)


# this is use to remove white space
print(len(multiline.strip()))  
print(len(multiline.lstrip()))  
print(len(multiline.rstrip()))  



print('')
# build a menu 
# the rjust stand fot justify right and the ljust is justify left : center is center 
 title = 'menu'.upper()
 print(title.center(20, '='))
 print('coffee'.ljust(16, '.') + "$1".rjust(4))
 print('muffin'.ljust(16, '.') + "$2".rjust(4))
 print('cheesecake'.ljust(16, '.') + "$4".rjust(4))


# string index value
print('')

print(first[0])
print(first[-1])
print(first[1:-1])
print(first[1:])



# some method return boolean data

print(first.startswith('p'))
print(first.endswith('l'))

# boolean  data type 
myvalue= true
x = bool(false)
print(type(x))
print(isinstance(bool, myvalue))





# numric data type

# interger type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))


# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))


# complex type 
com_value  = 5 + 3j
print(type(com_value))
print(type(com_value.real))
print(type(com_value.imag))
print(type(com_value))






# built-in function for numbers

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1) )



print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))
# print(math.pi)
# print(math.pi)



# casting a string to a number
zipcode = '10001'
zip_value = int(zipcode)
