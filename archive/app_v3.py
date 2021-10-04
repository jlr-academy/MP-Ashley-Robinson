# 1. Create a directory on your system
# 2. Follow instructions above to create the virtual environment
# 3. Activate the venv
# 4. Try installing some packages and list them
# 5.. Create a requirements.txt files from your venv
# 6. When you are done, deactivate'''


#                           start menu
#                               /\
#                              /  \
#                             /    \
#                     products      Courier
#
#
#
#


#Welcome notes

print('Welcome to your very own app - CafeUK')
print('What would you like review?')


#####  Menus  #####
#Start menu
def StartMenuChoice():
    print('''
    1   Inventory
    2   Couriers
    3   Save Changes
    0   Exit app''')

    choicemade = int(input())
    return choicemade





#product menu
def ProductsMenuChoice(productsList):
    choicemade = 1
    while choicemade !=0:
        print('''
        What would you like to do with your products?

        1   See Products
        2   Amend Products
        3   Create New products
        0   Exit to Main Menu''')

        choicemade = int(input())

        if choicemade == 1: # see list
            Print_list(productsList)
        elif choicemade == 2: # amend list item
            print('This is how your product list currently looks')
            Print_list(productsList)
            ans = input('Would you like to amend (A) or delete (D) a product?')
            if ans.upper() == "D":
                #DelProduct()
                del_list_item(productsList)
            else:
                #amend_product()
                amend_list_item(productsList)
        elif choicemade == 3: # append list
            add_to_list(productsList) ## test for scope and global variables being updated
            
        elif choicemade == 0:
            return
        else:
            print('Invalid choice. Try again')
        

#Courier menu
def CouriersMenuChoice(Courierlist):
    while choicemade !=0:
        print('''
        What would you like to do with Couriers?

        1   See Couriers
        2   Amend Couriers
        3   Create new Courier
        0   Exit to Main Menu''')

        choicemade = int(input())
        if choicemade == 1:
            Print_list(Courierlist)
        elif choicemade == 2:
            print('This is how your courier list currently looks')
            Print_list(Courierlist)
            ans = input('Would you like to amend (A) or delete (D) a Courier?')
            if ans.upper() == "D":
                del_list_item(Courierlist)
            else:
                amend_list_item(Courierlist)
        elif choicemade == 3:
            add_to_list(Courierlist)
        elif choicemade == 0:
            return
        else:
            print('Invalid choice. Try again') 



############# Utilities #############

def Print_list(list):
    print(' ')
    for i in list:
        print(i)
    print(' ')

def add_to_list(list, new_item = 'not known'):
    if new_item != 'not known':
        NewItem = new_item
    else:  
        NewItem = input('What would you like to be added? ')

    #check if item in list (ignoring casing)
    newitemlower = NewItem.lower()
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
def list_to_file(list,filename):
    file = open(filename,'w')
    for item in list:
        file.write(item + '\n')
    file.close()

# Write file to list
def file_to_list(list,filename): ########xxxxx
    try:
        file = open(filename,'r')
        lines=file.readlines()
        for line in lines:
            line = line.rstrip() # will remove white space from right
            list.append(line)
    except FileNotFoundError as fnfe:
        print('File not found '+ str(fnfe))
    #0file.close()




#delete item from list
def del_list_item(list, del_item = 'not known'):
    if del_item != 'not known':
            DelItem = del_item
    else:  
        DelItem = input('''Which item would you like to delete? 
        Tip: Say all to clear all inventory ''')
    if DelItem in list:
        ans = input(f'Are you sure you would like to delete {DelItem} permanantly Y/N ') # check if they really want to delete
        if ans.lower() == 'n':
            return
        else:
            productsList.remove(DelItem)
                
    elif DelItem.lower() == "all":
        list.clear()
    else:
        print('''I\'m sorry, that item does not exist in your inventory. No need to remove.
        ''')

# Amend list item
def amend_list_item(list):
    item = input('Which item would you like to amend? ')
    if item in list:
        for i in range(len(list)):
            itemname = list[i]
            if item.lower() == itemname.lower():
                new_name = input(f'What would you like {itemname} to change to? ')
                list[i] = new_name
                print(f'{itemname} has been updated to {new_name}. This is how the inventory now looks:')
                Print_list(list)
                return
    else:
        ans = input('''I\'m sorry, that item does not exist in your inventory. Would you like to add it? Y/N
        ''')
        if ans.upper() == 'Y':
            add_to_list(list,item)
            return
        elif ans.upper() == 'N':
            if input('Would you like to try again? Y/N').upper() =='Y':
                amend_list_item(list) # remove this as can create a call stack loop
                return
            else:
                return







#########################


#initialise

productsList = []
Courierlist = []

#load data

file_to_list(productsList,'./data/product_list.txt')
file_to_list(Courierlist,'./data/courier_list.txt')


# main menu direct
choice =1
while choice!=0: # keep asking what they want to do until they ask to quit
    choice = StartMenuChoice()

    #run different functions based on choice
    if choice == 1:
        print('You have chosen to review your products')
        ProductsMenuChoice(productsList)
    elif choice ==2:
        print('You have chosen to review couriers')
        CouriersMenuChoice(Courierlist)
    elif choice ==3:
        print('You have chosen to save all of your changes ')
        list_to_file(productsList,'./data/product_list.txt')
        list_to_file(Courierlist,'./data/courier_list.txt')
    elif choice == 0:
        print('Thanks for visiting')
        quit()
    else:
        print('Invalid choice, please try again.')  
          

    print('What would you like to do next?')
    
