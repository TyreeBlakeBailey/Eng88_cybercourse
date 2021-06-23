from Resturant_Menu import Menu
from Customer_order import Customer_order


class Customer(Menu, Customer_order):

    def Customer_Order(self):
        print("On todays menu we have the following:")
        for items in Menu().Resturant_menu.values():
            print(items)
        new_item = input("What do you want from the menu?    ")
        Customer_order().AddToMenu(Menu().Resturant_menu[ int(new_item) ])
        # print(Menu().Resturant_menu[int(input("What do you want from the menu?    "))])
        print(Customer_order().Order)


while True:
    Customer().Customer_Order()
