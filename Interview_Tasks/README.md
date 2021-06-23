## python
* python installation 3.7 or above *

## Pycharm set up 

#### Documentation with readme.md to store on GIT-HUB

    …or create a new repository on the command line
    echo "# practice" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/TyreeBlakeBailey/practice.git
    git push -u origin main


##### dynamically type language

- testing the python env 'print("text")'
- Python is being used worldwide for websites and applications such as LinkedIn
- It is needed in DevSecOps because it is required for the consultant to have an understanding of the code
- Need to understand the code to add security aspects


- What are variables?
    - Variables work as a placeholder to store data 
      
- String
    - Anything between "" is considered a string
  
- Boolean 
    - True or false value

- Integers, Float
    - Any Number that is given
  

```python
#Create a varible for first name, last name and DOB
#Syntax name of the varoble = va;ue to store in teh variable
# Naming convention to follow

first_name = "Tyree"
last_name =  "Blake-Bailey"
DOB = 111

print(first_name + " " + last_name)
```

```python
#Create a varible for first name, last name and DOB
#Syntax name of the varoble = va;ue to store in teh variable
# Naming convention to follow

first_name = "Tyree"
last_name =  "Blake-Bailey"
date_birth = 111

print(first_name + " " + last_name)
print(date_birth)

#to find out the type of variable we have method called type()
# taking input from teh user - input()
name = input("Please enter name ")
print("Hello " + name)
```

# Operators 


### Arithmetic Operators| Operand | Description | Example |

|:---------: |:----------------------------: |:--------: |
| + | add two operands (variables) together| X + y + 2 |

| - | subtract two operands (variables) | X - y - 2 |

| * | multiply two operands (variables) | X - y - 2 |

| / | divide two operands (variables) | X - y - 2 |

| % | Modulus - remainder of the division of left operand by the right | X - y - 2 |

| + | add two operands (variables) together| X + y + 2 |## Comparison Operators| Operand | Description | Example |
|:---------: |:----------------------------: |:--------: |
| > | True if left operand is greater than the right| x > y |

| < | True if left operand is less than the right| x < y |

| == | True if both operands are equal | x == y |

| != | True if both operands are equal | x != y |

| >= | True if left operand is greater than or equal to the right| x >= y |

| <= | True if left operand is less than or equal to the right| x <= y  |
 
```python
value1 = 6
value2 = 7

print(value2 > value1) #Greater than
print(value1 < value2) #Less than 
print(value1 + value2) # Addition
print(value2 - value1) #Subtraction
print(value1 >= value2) # Greater than or equal to
print(value1 != value2) # Not equal to
print(value2 * value1) #Multiplication
print(value2 / value1) #Division

Name = "Tyree"
Num = 2

# all functions below give the user a boolean value back. 

print(Name.isalpha()) #checks if the value is alphabetical 
print(str(Num).isalpha()) # "isalpha can only take a string value 
print(Name.isdigit()) # checks if the string value given is a digits
print(Name.startswith("T")) # checks if the beginning of the string starts with teh given Char

``` 

## Strings, concatenation and casting  

concatenation is the combination of different values, variables, and strings together 
```python
# Strings, concatenation and casting

    #to find the length of a string use the len() function

greetings = "Hello World!"

# can use any number started from 0,
# if you use negative numbers it will work backwards
print(len(greetings))

print(greetings[0:-10])
 #greetings[:-10] == greetings[:2]

white_spaces = "lot's of white spaces at the end                    "
print(len(white_spaces))
print(len(white_spaces.strip())) # the strip function gets rid of the empty white spaces in a string

example_text = "here's some text with lot's of text"
print(example_text.count("text")) #The Count methdod will count how mnay times a given text/char appears in a text
print(example_text.lower()) # This brings the entire text to lower case
print(example_text.upper()) # This brings the entire text to upper case
print(example_text.replace("with", ",")) # this methods replaces the first value with  the given second value

print(example_text.capitalize()) # This capitialises the first letter of the text

#Concatenation
#combining values, variables, strings together

First_name = "Tyree"
Second_name = "Blake-Bailey"
Age = "23"
#
# # casting an int -> a string
# print(First_name + " " + Second_name + " is " + str(Age))
# #str() converts any value it is given into a string

Age_int = int(Age)

print(Age_int)

print(str(Age_int) + ", is a " + str(type(Age_int)))
print("{}, is a {}".format(Age_int, type(Age_int)))
print(f"{Age_int}, is a {type(Age_int)}")

#above are three exactly the same way to print the statement

```

# Python Data Collections

- Lists
- Dictionary
- Tuples
- Sets

## List

- lists can hold any form data in the same list 

## Tuples

- Syntax Tuple_Example()
- tuples are the same as list except a tuples cannot be changed once they are created they are mutable

## Dictionaries

- are structured as key = value
- values can be any form (string, int, list)
- Syntax dictionary_example{}

## Sets

- sets are data collections, but the difference is that they are unordered
- Syntax name = {}
- the data is given back in a random ordered
```python
# Lists
# Syntax ["London" ]

shopping_list = [ "juice", "strawberries", "yogurt", "chicken", "raspberry", "butter" ]
#                   0           1              2        3           4           5

print(shopping_list)
print(type(shopping_list))

#use shopping_list[x] to print that item in the list
print(shopping_list[2])
print(shopping_list[4])
print(shopping_list[-1])

#can adjustingn the values in teh list
shopping_list[5] = "Oats" # replaces given slot with new value
shopping_list.append("mango") # adds new item at the end
shopping_list.remove("Oats") # removes the value that is given
shopping_list.pop() #pop() removes the last item in the list


#prints the list in reverse order
print(shopping_list[::-1])
print(shopping_list.reverse())

#prints the list one item at a time in a loop format
for x in shopping_list:
    print(x)

# Tuples

essential = ("egg", "milk", "break")

print(essential)
print(type(essential))

# replace bread with yogurt
#essential(2) = "yogurt" #returns an error cannot change the value of a tuple

## Dictionaries

# can hold any form of data within it

student_1 = {
    "name" : "Tyree ",
    "key"  : "Value",
    "stream" : "Cyber Security", #string
    "Completed_lessons" : "3", #int
    "Complete_lessons_names":["variables", "operators", "data_collections"] #list


}

print(student_1) # prints the entire dictionary
print(student_1["name"]) # prints the value from the given key
print(student_1["Complete_lessons_names"][1]) # prints one value from the list in the dictionary
print(student_1.keys()) #only prints the keys in the dictionary
print(student_1.values()) #Only prints the values in the dictionary


## Sets
# sets are data collections but the difference is that they are unordered
#Syntax name = {}
# the data is given back in a random ordered


car_parts = {"wheels", "doors", "engine"}
print(car_parts)

# used to add an item
car_parts.add("windows")
print(car_parts)
# both used to remove an item from the list
car_parts.discard("doors")
car_parts.remove("doors")


#Frozen sets
frozen_set = ([1,3,5,6])
print(frozen_set) # frozen sets are always printed in the same ordered

```