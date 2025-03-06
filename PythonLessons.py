import keyword
import time

print(keyword.kwlist)
print(dir(__builtins__))

#Variables store data
a,b,c = 1,2,3 
varA = "This is too\
        big to fit\
        on a single line so\
        you multi-lined it "

VarB = 'This is quite a long'\
        'thought'

print(a,b,c)

#Datatype
print(type(a))
len(varA) # returns number of characters in the string

#Concactenation
print (varA + VarB)
#index
print(varA[1])

#creating function
def sayHello():
    return str("Hello There!")

#Type Casting
age = "23"
print(int(age))

#helper functions to take input
userEmail = input ('input your email address: ')
userName = input ('input your user name: ')

print("your email is " + str(userEmail) )
print("your  email and username is {} {}".format(userEmail,userName))


#reserved keywords

#python input ouput

#Maths and Logical Operators

a = False
b = True

if not(a) and b:
    print("All True")


#OOP

#class

#control flow
bill_total = 150
discount = 10

if bill_total > 200:
    bill_total -= discount
    print(" Bill is greater than 200") 
elif 100 < bill_total > 200:
    print(" Bill is greater than 100 but less than 200")
else:
    print(" Bill is less than 200")

print("total bill:" + str(bill_total))

http_status = 500

match http_status:
    case 200 | 201:
        print("success")
    case _:
        print("unknown")

#using loop and conditionals

favourites = ['Jollof Rice','Grilled Fish', 'Rice and Beans', 'Pepper Soup', 'Fired Rice', 'Vegetable Soup', 'Ofada Rice' ]
count = 0

for idx, item in enumerate(favourites):
    print(idx, item )

    if favourites == 'Pepper Soup':
        print('Yes one of my favorite meal is', favourites)
        break
        continue 
        pass
    else:
        print('No sorry, not a meal on my list')

while count < len(favourites):
    print('I like this meal:', favourites[count])
    count += 1

#Nested Loop
start_time = time.time()
# outer loop
for 1 in range(10):
    # inner loop
    for j in range(10):
        print(0, end =" ")
    print()   


print((round(time.time() - start_time), 2))


num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
count = 0
for i in num_list:
    print(i)
    if i> 45:
        print("over 45")
    else:
        print("Under 45")    

for i in enumerate(num_list):
    count += 1
    print(i)
    if i == 36:
        print("Number found at position: ", [i])
        #print("number found at" numlist[i])
        break
    else:
        print("number not found")  

print(count)

#function is set of instruction that takes 
# input and returns output
def sum(x,y):
    return x+y

#scope IS TO PROTECT VARIABLES 
#INTO BEEN CHANGED IN OTHER PARTS OF THE PROGRAM
#LEGB
special = 5

def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        #local variable
        double = total * 2
        print(special)

    double_it()

    return total


family_members = {
    1 :
        {
        "id" : "1"
        "first name" : "Bunamin"
        "last name": "Adams"
        "parents":{

        }
           
        }
}

#file are used in store data

import random
f = open("name.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
f.close()
print(random.choice(f_content_list))

f_name = input('Type the file name: ')
f = open(f_name) # "r" omitted as it's the default
f_content = f.read()
f_content_list = f_content.split("\n")
f.close()
print(random.choice(f_content_list))



trial = 'reversal'
new_trial = trial[::-1]
print (new_trial)

#recursion

#comprehensions

#map & filter
def find_object(object):
    item = input("enter item")
    try:
        if object[0] == item[0]:
            return object
    except Exception as e:
        print({e})
    
map_object = map(find_object, favourites)
print(map_object)
for x in map_object:
    print(x)

filter_object = filter(find_object, favourites)


data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)

# List comprehension:
data = [x+3 for x in data]

# Regular for loop:
for x in range(len(data)):
    data[x] = data[x] + 3

# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)

#Object Oriented Programming
member(name, )


def Is_word_bool(boolean):
    if boolean == True or False:
        return "Yes"
    else:
        return "No"


    #test

print(Is_word_bool('name'))