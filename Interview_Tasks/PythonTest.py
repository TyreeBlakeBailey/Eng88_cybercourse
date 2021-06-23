#Get users name,
# age
# Date of birth

while True:
    first_name = input("Please enter you first name  ")
    last_name = input("Please enter your last name  ")
    Date_Birth = input("Please enter date of birth  ")

    print(first_name + " " + last_name + " " + Date_Birth)

    if input("Enter another user? y/n ").lower() == 'n':
        break

print("Exiting")