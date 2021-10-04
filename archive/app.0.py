
#3) The first letter of a product should be auto-capitalised when a product is created, regardless of how the name is entered
#4) STRETCH: The first letter of each word in a product should be auto-capitalised when a product is created


productsList = []

#Welcome notes
print('Welcome to your very own app - CookUK')
print('What would you like to do today?')

#Start menu
def StartMenuChoice():
    print('''
    1   See inventory
    2   Create new product
    3   Amend the inventory
    4   Exit app''')

    choicemade = int(input())
    return choicemade


def create_product(NewProd = 'not known'):
    if NewProd != 'not known':
        NewItem = NewProd
    else:  
        NewItem = input('What is your new product called? ')
    #check if item in list (ignoring casing)
    newitemlower = NewItem.lower()
    if newitemlower in (string.lower() for string in productsList):
        productsList.append(NewItem)
        print(f'{NewItem} has been added to your inventory')

def see_inv():
    print(' ')
    for i in productsList:
        print(i)
    print(' ')

def AmendorDel():
    print('This is how your inventory currently looks')
    see_inv()
    ans = input('Would you like to amend (A) or delete (D) a product?')
    if ans.upper() == "D":
        DelProduct()
    else:
        amend_product()


def DelProduct():
    item = input('''Which item would you like to delete? 
        Tip: Say all to clear all inventory''')
    if item in productsList:
        ans = input(f'Are you sure you would like to delete {item} permanantly Y/N ') # check if they really want to delete
        if ans.lower() == 'n':
            return
        else:
            productsList.remove(item)
                
    elif item.lower() == "all":
        productsList.clear()
    else:
        print('''I\'m sorry, that item does not exist in your inventory. No need to remove.
        ''')

def amend_product():
    item = input('Which item would you like to amend? ')
    if item in productsList:
        for i in range(len(productsList)):
            product = productsList[i]
            if item.lower() == product.lower():
                new_name = input(f'What would you like {product} to change to? ')
                productsList[i] = new_name
                print(f'{product} has been updated to {new_name}. This is how the inventory now looks:')
                see_inv()
                return
    else:
        ans = input('''I\'m sorry, that item does not exist in your inventory. Would you like to add it? Y/N
        ''')
        if ans.upper() == 'Y':
            create_product(item)
            return
        elif ans.upper() == 'N':
            if input('Would you like to try again? Y/N').upper() =='Y':
                amend_product() # remove this as can create a call stack loop
            else:
                return


#Ask what they would like to do
choice =1
while choice!=4: # keep asking what they want to do until they ask to quit
    choice = StartMenuChoice()

    #run different functions based on choice
    if choice == 1:
        print('You have chosen to see your inventory')
        see_inv()
    elif choice ==2:
        print('You have chosen to create a new product')
        create_product()
        print('This is how your inventory now looks:')
        see_inv()
    elif choice ==3:
        print('You have chosen to amend the inventory')
        AmendorDel()
    else:
        print('Thanks for visiting today')  
        quit()  

    print('What would you like to do next?')
    
