def user_name():
    pass


list_num = [ 9, 8, 7, 6, 5 ]
for nums in list_num:
    print(nums)

if True and True:
    pass
else:
    pass

# tuples are immutable cannot be changed where as lists can be changed
# Tuples processing is faster

num_id = {'0': 1, '5': 9}
print(type(num_id))  # prints dictionary


class ExampleClass:
    pass


ExampleObject = ExampleClass()

value_list = [ 9, 8, 7, 6, 5, 4 ]
value_list.append(9)
print(value_list)

def greetings(name):
    if name == "name":
        return True
    else:
        return False

class SecondClass(ExampleClass):
    #super().__init__()
    pass


def EvenNums(List):
    EvenList = []
    for items in List:
        if items % 2 == 0:
            EvenList.append(items)
    return EvenList

print(EvenNums(value_list))


