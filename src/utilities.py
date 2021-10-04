import typing

############# Utilities #############

# Prints out defined list
def print_list(list:list):
    print(' ')
    for i in list:
        print(i)
    print(' ')
    input('Press any key to continue ')

# adds named item to defined list. Asks for item if not passed one
def add_to_list(list: list, new_item = 'not known'):
    if new_item == 'not known':
        new_item = input('What would you like to be added? ')
    else:  
        pass

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
        delete_item = input('''Which item would you like to delete? 
        Tip: Say all to clear all inventory ''')
    if delete_item in list:
        ans = input(f'Are you sure you would like to delete {delete_item} permanantly Y/N ') # check if they really want to delete
        if ans.lower() == 'n':
            return
        else:
            list.remove(delete_item)
                
    elif delete_item.lower() == "all":
        list.clear()
    else:
        print('''I\'m sorry, that item does not exist in your inventory. No need to remove.
        ''')

# Amend list item
def amend_list_item(list: list):
    item = input('Which item would you like to amend? ')
    if item in list:
        for i in range(len(list)):
            itemname = list[i]
            if item.lower() == itemname.lower():
                new_name = input(f'What would you like {itemname} to change to? ')
                list[i] = new_name.title()
                print(f'{itemname} has been updated to {new_name.title()}. This is how the inventory now looks: ')
                print_list(list)
                return
    else:
        ans = input('''I\'m sorry, that item does not exist in your inventory. Would you like to add it? Y/N 
        ''')
        if ans.upper() == 'Y':
            add_to_list(list,item)
            return
        elif ans.upper() == 'N':
            if input('Would you like to try again? Y/N ').upper() =='Y':
                amend_list_item(list) # remove this as can create a call stack loop
                return
            else:
                return




