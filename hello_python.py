print('Hello capstone!')

# Variables
school = "MCTC"
gpa = 3.7
student_in_class = 22

# if-statements
# REMEMBER COLONS AND INDINTATIONS
if gpa == 4:
    print('WOW!')
elif gpa > 3:
    print('Awesome!')
else:
    print('Cool!')

# lists
schools = ["MCTC", "DCTC", "North Hennepin Technical College"]
# sort alphabetically
schools.sort()
print(schools)

# add to end of list
schools.append('Century College')
#reverse sort by order
schools.reverse()
print(schools)


# ifs and lists
if 'MCTC' in schools:
    print("MCTC is one of the schools in the list")

# strings
class_name = "Software Development Capstone"
print(class_name.upper()) #print in caps
print(len(class_name)) #number of digits
print(class_name.split()) #splits individual words and places them in a list
print(class_name.split('o')) #['S', 'ftware Devel', 'pment Capst', 'ne']

if 'Capstone' in class_name: #case sensitive
    print('This must be the capstone place')

# loops - for loops over range
for x in range(10):
    print(x)

# loops - for loops over sequence
for s in schools:
    print(s.upper())

for letter in school:
    print(letter * 10) #print each letter indiv. but then 10 of each letter

data = [0] * 10
print(data) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

more_data = [None] * 10
print(more_data)

# while loops
# common for input validation and processing data

name = input('Enter your name: ')
while len(name) == 0:
    # more common way of writing the above would be
    # while not name:
    print('Please enter at least one character')
    name = input('Enter your name: ')

# True and False and None
# always use caps to start

start_of_semester = True
winter = False    

if winter:
    print('brr!')
else:
    print('it is not winter')

# Dictionaries
    
class_codes = { 2905: 'Capstone', 2560: 'Web', 2545: 'Java'}

print(class_codes[2560])

for code in class_codes:
    print(code) # print keys
    print(class_codes[code]) # print values

#return key and value
for code, name in class_codes.items():
    print('The class code is ' + str(code) + ' and the name is ' + name)

#same thing but with format string
for code, name in class_codes.items():
    print(f'The class code is {code} and the name is {name}')

#slicing strings and lists (taking chunks)
schools = ["MCTC", "DCTC", "North Hennepin Technical College"]
first_two = schools[0:2]
print(first_two)

school_name = "Minneapolis Community and Technical College"
city = school_name[:11] #start from 0 and go up to but don't include the 11th character

# find last item in a list - common
last_school = schools[-1]
print(last_school)

#slice last two items in a list in a new list
last_two_schools = schools[-2:] #start at second to last item and go to end

#file inputs and outputs
with open('data.txt', 'w') as f: #w to write
    f.writelines(schools)
with open('data.txt') as f:
    print(f.read())

# functions
def get_name():
    print('Heloo, please enter your name!')
    name = input('Your name is: ')
    return name

# remember to actually call the function
name = get_name()


