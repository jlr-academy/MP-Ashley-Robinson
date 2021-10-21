import os
from file_mngment import json_to_list, csv_to_list_of_dicts

############# Utilities #############

# Prints out defined list
def print_list(list:list):
    print(' ')
    i=1
    for item in list:
        print(i, item)
        i = i + 1
    print(' ')
    #input('Press any key to continue ')

# adds named item to defined list. Asks for item if not passed one
def add_to_list(list: list):
    if type(list[0]) == dict:
        required_fields_list = get_required_fields(list)
        #avail_couriers_list = []
        #avail_product_list = []
        try:
            prod_list = []
            csv_to_list_of_dicts(prod_list,"data\products.csv") 
            prod_list = get_available_product_names_list(prod_list)
        except: pass
        try: 
            cour_list = []
            csv_to_list_of_dicts(cour_list,"data\couriers.csv")
            cour_list = get_available_courier_names_list(cour_list)
        except: pass

        temp_dict = {}
        print("Please add the required details. ")
        for i in required_fields_list:
            if i == "courier":
                print(f"{i}: ")
                selection = select_from_list(cour_list)
                temp_dict[i] = cour_list[selection]

            elif i == "product":
                print(f"{i}: ")
                selection = select_from_list(prod_list)
                temp_dict[i] = prod_list[selection]
            elif i == "status":
                status_list = ["Processing","Accepted","Packing","Delivery","Delivered", "Cancelled"]

                print(f"{i}: ")
                selection = select_from_list(status_list)
                temp_dict[i] = status_list[selection]

            else:
                temp_dict[i] = input(f"{i}: ")
        list.append(temp_dict)
    else:  
        new_item = input('What would you like to be added? ')
        #check if item in list (ignoring casing)
        newitemlower = new_item.lower()
        newitemtitle = newitemlower.title()
        if newitemtitle in list:
            print('item already exists in list')
            return list
        else:
            list.append(newitemtitle)
            return list
            

def get_available_courier_names_list(list_of_dics:list):
    return_list = []
    for courier in list_of_dics:
        return_list.append(courier["name"])
    return return_list

def get_available_product_names_list(list_of_dics:list):
    return_list = []
    for product in list_of_dics:
        return_list.append(product["product_name"])
    return return_list




#returns a list of keys that exist in the first list item
def get_required_fields(list_of_dics:list):
    list_of_fields =[]
    for item in list_of_dics:
        for key in item:
            if str(key) in list_of_fields:
                pass
            else:
                list_of_fields.append(key)
    return list_of_fields


# Write list to a .txt file
def list_to_file(list: list,filename):
    try:
        with open(filename,'w') as file:
            for item in list:
                file.write(item + '\n')
    except:
        print(f'File not accessable: {filename}')


# Write txt file to list
def file_to_list(list: list,filename): 
    try:
        with open(filename, 'r') as file:
            lines=file.readlines()
            for line in lines:
                line = line.rstrip() # will remove white space from right
                list.append(line)
    except FileNotFoundError as fnfe:
        print('File not found '+ str(fnfe))
    

#delete item from list
def del_list_item(list: list, del_item = 'not known'):
    if del_item != 'not known':
            delete_item = del_item
    else:  
        delete_item = input('''Enter reference number of the item would you like to delete? 
        Tip: Say all to clear all inventory ''')
    if int(delete_item)-1 <= len(list):
        ans = input(f'Are you sure you would like to delete {list[int(delete_item)-1]} permanantly Y/N ') # check if they really want to delete
        if ans.lower() == 'n':
            return
        else:
            del list[int(delete_item)-1]
                
    elif delete_item.lower() == "all":
        list.clear()
    else:
        print('''I\'m sorry, that item does not exist in your inventory. No need to remove.
        ''')


# Amend list item
def amend_list_item(list: list):
    
    item = int(input('Enter reference number of the item you would you like to amend? ')) - 1
    if type(list[item]) == str or type(list[item]) == int:
        while True:
            if item <= len(list):
                itemname = list[item]
                new_name = input(f'What would you like {itemname} to change to? ')
                list[item] = new_name.title()
                print(f'{itemname} has been updated to {new_name.title()}. This is how the inventory now looks: ')
                print_list(list)
                return
            else:
                input("Please choose an item from the list using the reference number" )
    else:
        #print(list[item])
        options_list = get_required_fields(list)
        
        print_list(options_list)
        list_choice = int(input("Enter reference number of field requiring change "))
        key_change = options_list[list_choice - 1]
        while True:
            if key_change in list[item]:
                new_name = input(f"What would you like {key_change} to be for this order? ")
                list[item][key_change] = new_name
                return
            else:
                print("That is not an available option. Please try again")

# As amend list item but updates the order status only, with less user input
def amend_order_status(list: list):
    print_list(list)
    item = int(input('Enter reference number of the order to update? ')) - 1
    status_str = "status"
    print(f"The current status of this order is {list[item][status_str]}")
    options_list =[]
    json_to_list(options_list,r"data\order_status.json")
    print_list(options_list)
    new_status = int(input("What would you like to change the status to? "))
    while True:
        if new_status <= len(options_list):
            list[item][status_str] = options_list[new_status - 1]
            print("Status Updated" )
            return
        else:
            input("Please choose an item from the list using the reference number" )
   


#Displays a list and returns the index of choice made    
def select_from_list(list: list):
    print_list(list)
    while True:
        choice = int(input("Select an item from the list using the reference number "))
        if choice <= len(list) and choice > 0:
            return choice - 1
        else:
            print("That is not an item in the displayed list. Please use the reference number for required item ")


def add_to_order_list(list: list, courier_list: list, product_list: list): #######WIP
    if type(list[0]) == dict:
        order_details_list = []
        temp_dict = {}
        json_to_list(order_details_list,r"data\order_fields.json")
        for i in order_details_list:
            print("Please add the required order details. ")
            temp_dict[i] = input(f"{i}: ")
        list.append(temp_dict)
    else:
        pass



