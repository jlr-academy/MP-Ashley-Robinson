from utilities import print_list, add_to_list, del_list_item, amend_list_item
from datetime import datetime

#####  MENUS  #####

#welcome note
def welcome_note():
    if datetime.now().time() < 12:
        return "Good Morning"
    elif datetime.now().time() > 16.30:
        return "Good Evening"
    else:
        return "Good afternoon"


#Start menu
def start_menu_choice():
    print('''
    1   Inventory
    2   Couriers
    3   Save Changes
    4   Orders
    0   Exit app''')

    choicemade = int(input())
    return choicemade


#product menu
def products_menu_choice(products_list):
    choicemade = 1
    while choicemade !=0:
        print('''
        What would you like to do with your products?

        1   See Products
        2   Amend Products
        3   Create New products
        0   Exit to Main Menu
        ''')

        choicemade = int(input())

        if choicemade == 1: # see list
            print_list(products_list)
        elif choicemade == 2: # amend list item
            print('This is how your product list currently looks')
            print_list(products_list)
            ans = input('Would you like to amend (A) or delete (D) a product? ')
            if ans.upper() == "D":
                #DelProduct()
                del_list_item(products_list)
            else:
                #amend_product()
                amend_list_item(products_list)
        elif choicemade == 3: # append list
            add_to_list(products_list) ## test for scope and global variables being updated
            
        elif choicemade == 0:
            return
        else:
            print('Invalid choice. Try again')
        

#Courier menu
def couriers_menu_choice(courier_list):
    choicemade = 1
    while choicemade !=0:
        print('''
        What would you like to do with Couriers?

        1   See Couriers
        2   Amend Couriers
        3   Create new Courier
        0   Exit to Main Menu
        ''')

        choicemade = int(input())
        if choicemade == 1:
            print_list(courier_list)
        elif choicemade == 2:
            print('This is how your courier list currently looks')
            print_list(courier_list)
            ans = input('Would you like to amend (A) or delete (D) a Courier? ')
            if ans.upper() == "D":
                del_list_item(courier_list)
            else:
                amend_list_item(courier_list)
        elif choicemade == 3:
            add_to_list(courier_list)
        elif choicemade == 0:
            return
        else:
            print('Invalid choice. Try again') 


#Orders Menu

def orders_menu_choice(orders_list):
    choicemade = 1
    while choicemade !=0:
        print('''
        What would you like to do with Orders?

        1   See Orders
        2   Amend Orders
        3   Create new Order
        4   Update customer fields
        0   Exit to Main Menu
        ''')

        choicemade = int(input())
        if choicemade == 1:
            print_list(orders_list)
        elif choicemade == 2:
            print('These are your current orders ')
            print_list(orders_list)
            ans = input('Would you like to amend (A) or delete (D) an Order? ')
            if ans.upper() == "D":
                del_list_item(orders_list)
            else:
                amend_list_item(orders_list)
        elif choicemade == 3:
            add_to_list(orders_list)
        elif choicemade == 4:
            pass ## add function to update json file of order fields
        elif choicemade == 0:
            return
        else:
            print('Invalid choice. Try again')