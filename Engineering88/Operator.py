# value1 = 6
# value2 = 7
#
print(value2 > value1)
print(value1 > value2)
print(value1 + value2)
print(value2 - value1)
print(value1 >= value2)  # greater than or equal to
print(value1 != value2)  # not equal to
print(value2 * value1)
print(value2 / value1)
#
Name = "Tyree"
Num = 2
# .isalpha # chekcs if the value is alphabetical
print(Name.isalpha())  # returns booleans value
print(str(Num).isalpha())
print(Name.isdigit())  # checks if the string value given is a digits
print(Name.startswith("T"))  # checks if the beginning of the string starts with teh given Char

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

#above are three exactly the same way to print the statment
