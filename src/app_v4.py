from menus import start_menu_choice, products_menu_choice, couriers_menu_choice, orders_menu_choice, customers_menu_choice
from file_mngment import json_to_list, list_to_json, csv_to_list_of_dicts, list_of_dicts_to_csv, save_change
from menus import clear_screen
from cafe_ASCII_art import squidward, hogs, pig
from random import randint
import utilities


#       MENU STRUCTURE
#
#
#                           start menu
#                               /\
#                              /  \
#                             /    \
#                     products      Courier
#


#########################-----------------------------#########################


''' products_list = csv_to_list_of_dicts('data\products.csv')
courier_list = csv_to_list_of_dicts('data\couriers.csv')
orders_list = json_to_list("data\orders.json") '''



#initialise
products_list = []
courier_list = []
orders_list = []

#load data
products_list = utilities.db_table_to_list_of_dics("products")
courier_list = utilities.db_table_to_list_of_dics("couriers")


#csv_to_list_of_dicts(products_list,'data\products.csv')
#csv_to_list_of_dicts(courier_list,'data\couriers.csv')
json_to_list(orders_list,"data\orders.json")



#Welcome notes
clear_screen()



# main menu direct
choice =1
while choice!=0: # keep asking what they want to do until they ask to quit
    choice = start_menu_choice()

    #run different functions based on choice
    if choice == 1:
        print('You have chosen to review your products')
        products_menu_choice()
    elif choice ==2:
        print('You have chosen to review couriers')
        couriers_menu_choice()
    elif choice ==3:
        print('You have chosen to review customers')
        customers_menu_choice()
    elif choice ==4:
        print('You have chosen to review orders')
        orders_menu_choice(orders_list)
    elif choice == 0:
        print('Thanks for visiting')
        choice = input("Would you like to save changes? Y/N ") 
        if choice.lower() == "y":
            save_change(products_list, courier_list, orders_list)
        else:
            pass
        quit()
    else:
        print('Invalid choice, please try again.')  
          
    #Loading screen images
    print('Loading menu...')
    image_rand = randint(1,3)
    if image_rand == 1:
        print(squidward)
    elif image_rand == 2:
        print(hogs)
    else:
        print(pig)


