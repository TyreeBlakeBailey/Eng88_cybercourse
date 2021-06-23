import datetime


def Birth_Year(age):
    return int(datetime.datetime.now().strftime('%Y')) - int(age) - 1
def Birthday_Pass(BirthDay): # function to check if the persons birthday has passed
    BirthDay.strfttime('%d')


name = input('What is your name?  ').capitalize()
age = input("How old are you ?  ")
Birth_Day = input("What is your birthday DD/MM")

print("OMG {}, you are {} years old so you were born in {} ".format(name, age, Birth_Year(age)))
