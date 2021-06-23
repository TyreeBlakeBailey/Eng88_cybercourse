#Lists
#Syntax ["London" ]

shopping_list = [ "juice", "strawberries", "yogurt", "chicken", "raspberry", "butter" ]
#                   0           1              2        3           4           5

print(shopping_list)
print(type(shopping_list))

#use shopping_list[x] to print that item in the list
print(shopping_list[2])
print(shopping_list[4])
print(shopping_list[-1])

#can adjustingn the values in the list
shopping_list[5] = "Oats" # replaces given slot with new value
shopping_list.append("mango") # adds new item at the end
shopping_list.remove("Oats") # removes the value that is given
shopping_list.pop() #pop() removes the last item in the list


#prints the list in reverse order
print(shopping_list[1:5])
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

