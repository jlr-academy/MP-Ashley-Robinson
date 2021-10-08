from utilities import file_to_list, list_to_file
from menus import start_menu_choice, products_menu_choice, couriers_menu_choice, orders_menu_choice
from file_mngment import json_to_list, list_to_json


# 1. Create a directory on your system
# 2. Follow instructions above to create the virtual environment
# 3. Activate the venv
# 4. Try installing some packages and list them
# 5.. Create a requirements.txt files from your venv
# 6. When you are done, deactivate'''

#       MENU STRUCTURE
#
#
#                           start menu
#                               /\
#                              /  \
#                             /    \
#                     products      Courier
#

## next dev
# add order to order list

#########################-----------------------------#########################

#initialise
products_list = []
courier_list = []
orders_list = []


#load data
file_to_list(products_list,'data\product_list.txt')
file_to_list(courier_list,'data\courier_list.txt')
json_to_list(orders_list,"data\orders.json")



#Welcome notes

print('Welcome to your very own app - CafeUK \n')
print('What would you like review? ')


# main menu direct
choice =1
while choice!=0: # keep asking what they want to do until they ask to quit
    choice = start_menu_choice()

    #run different functions based on choice
    if choice == 1:
        print('You have chosen to review your products')
        products_menu_choice(products_list)
    elif choice ==2:
        print('You have chosen to review couriers')
        couriers_menu_choice(courier_list)
    elif choice ==3:
        print('You have chosen to save all of your changes ')
        list_to_file(products_list,'./data/product_list.txt')
        list_to_file(courier_list,'./data/courier_list.txt')
        list_to_json(orders_list, "data\orders.json")
    elif choice ==4:
        print('You have chosen to review orders')
        orders_menu_choice(orders_list)
    elif choice == 0:
        print('Thanks for visiting')
        quit()
    else:
        print('Invalid choice, please try again.')  
          

    print('What would you like to do next?')
    
