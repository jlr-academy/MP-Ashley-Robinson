import typing
from file_mngment import json_to_list
############# Utilities #############

# Prints out defined list
def print_list(list:list):
    print(' ')
    i=1
    for item in list:
        print(i, item)
        i =i+1
    print(' ')
    input('Press any key to continue ')

# adds named item to defined list. Asks for item if not passed one
def add_to_list(list: list, new_item = 'not known'):
    if type(list[0]) == dict:
        order_details_list = []
        temp_dict = {}
        json_to_list(order_details_list,"data\order_fields.json")
        print("Please add the required order details. ")
        for i in order_details_list:
            temp_dict[i] = input(f"{i}: ")
        list.append(temp_dict)
   
    else:  
        new_item = input('What would you like to be added? ')

        #check if item in list (ignoring casing)
        newitemlower = new_item.lower()
        newitemtitle = newitemlower.title()
        #if newitemlower in (string.lower() for string in list):
        if newitemtitle in list:
            print('item already exists in list')
            return list
        else:
            list.append(newitemtitle)
            return list
            #print(f'{NewItem} has been added to your inventory')

# Write list to a file
def list_to_file(list: list,filename):
    try:
        with open(filename,'w') as file:
            for item in list:
                file.write(item + '\n')
    except:
        print(f'File not accessable: {filename}')


# Write file to list
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
    # if int(delete_item) <= len(list) and int(delete_item) >= 1:
    # if int(delete_item) in range(len(list))
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
        options_list =[]
        json_to_list(options_list, "data\order_fields.json")
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
    new_status = input("What would you like to change the status to? ")
    list[item][status_str] = new_status


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
        json_to_list(order_details_list,"data\order_fields.json")
        for i in order_details_list:
            print("Please add the required order details. ")
            temp_dict[i] = input(f"{i}: ")
        list.append(temp_dict)
    else:
        pass

