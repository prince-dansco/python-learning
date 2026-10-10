value  = 1
while value <= 10:
    print(value)
    value += 1

    # break statment
value  = 1
while value <= 10:
    print(value)
if  value == 5:
    break
    value += 1
    # break statment
value  = 1
while value <= 10:
    value += 1
if  value == 5:
    continue
    print(value)
else:
    print('value is now equal to ' + str(value))    

# for loop

names = ['prince', 'john', 'sera']
# for x in names:
    # print(x)

    # for x in 'mississippi':
    #     print(x)

# for x in names:
#     if x == 'sera':
#         break
#         print(x)
# for x in names:
#     if x == 'sera':
#         continue
#         print(x)


# for x in range(4):
#     print(x)

# for x in range(2,4):
#     print(x)

for x in range(0,100, 5):
    print(x)
    else:
        print('Glade that is over')


        names = ['prince', 'john', 'sera']
        actions = ['code', 'eats', 'sleeps']

        # for name in names:
        #     for action in actions:
        #         print(name + ' '+ action + ".")


        for action in actions:
            for name in names:
                print(name + ' '+ action + ".")