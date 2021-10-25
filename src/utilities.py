import os
from file_mngment import json_to_list
import pymysql 
import os
from dotenv import load_dotenv
from columnar import columnar



############# Utilities #############

# Prints out defined list
def print_list(list:list):
    print(' ')
    i=1
    for item in list:   
        print(i, item)
        i = i + 1
    print(' ')
    

# adds named item to defined list. Asks for item if not passed one
def add_to_list(list: list):
    if type(list[0]) == dict:
        required_fields_list = get_required_fields(list)
        #avail_couriers_list = []
        #avail_product_list = []
        try:
            prod_list = []
            #csv_to_list_of_dicts(prod_list,"data\products.csv") 
            #prod_list = get_available_product_names_list(prod_list)

            prod_list = db_table_to_list_of_dics("products")
            prod_list = get_available_product_names_list(prod_list)
        except: pass
        try: 
            cour_list = []
            #csv_to_list_of_dicts(cour_list,"data\couriers.csv")
            #cour_list = get_available_courier_names_list(cour_list)
            
            cour_list = db_table_to_list_of_dics("couriers")
            cour_list = get_available_courier_names_list(cour_list)
        except: pass

        temp_dict = {}
        print("Please add the required details. ")
        for i in required_fields_list:
            if i == "courier_id":
                print(f"{i}: ")
                selection = select_from_list(cour_list)
                temp_dict[i] = selection

            elif i == "product_id":
                print(f"{i}: ")
                selection = select_from_list(prod_list)
                temp_dict[i] = selection
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
        return_list.append(courier["couriers_name"])
    return return_list

def get_available_product_names_list(list_of_dics:list):
    return_list = []
    for product in list_of_dics:
        return_list.append(product["products_name"])
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



############# DATABASE Utilities #############

# Load environment variables from .env file with dotenv.load_dotenv()
# establishes connection to database outlined in .env file & creates connection and cursor objects
def initialise_db():
    # Load environment variables from .env file
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
    host,
    user,
    password,
    database
    )

    #create cursor object that manages db operations
    cursor = connection.cursor()
    return connection, cursor

# Creates a new table in the database named in .env file. 
# adds fields *table_name*_id as PK, 
# adds field *table_name*_name as varchar
def create_new_table(table_name:str):
    
    #initialise - gets env vars and creates a connection & cursor
    connection, cursor = initialise_db()

    #check if tables exist already and create if not
    cursor.execute("SHOW TABLES")
    
    table_exists = False
    for x in cursor:
        if table_name == str(x[0]):
            print("The table already exists")
            table_exists = True
            break

    #create required tables
    if table_exists == False:
        sql = f"CREATE TABLE {table_name}({table_name}_id INT AUTO_INCREMENT PRIMARY KEY, {table_name}_name VARCHAR(255));"
        cursor.execute(sql)

    #commit chnages and close 
    connection.commit()
    cursor.close()
    connection.close()

#Add specified db item to named table
#takes a list of fields and list of values
def add_to_db_table(table_name:str,fields:list,vals:list):

    #create fields string & values string
    converted_list = [str(element) for element in fields]
    fields_str = ",".join(converted_list)

    converted_list = ["'" + str(element) + "'" for element in vals]
    vals_str = ",".join(converted_list)
    
    #Create SQL commands from strings
    sql = f"INSERT INTO {table_name}({fields_str}) VALUES({vals_str});"
    
    #Execute sql 
    db_update_SQL_syntax(sql)

#updates the db named in .envs with given SQL syntax
def db_update_SQL_syntax(SQL_syntax:str):
    #initialise - gets env vars and creates a connection & cursor
    connection, cursor = initialise_db()    
    
    #Create SQL commands from strings
    sql = str(SQL_syntax)
    
    #Execute changes
    cursor.execute(sql)

    #commit chnages and close 
    connection.commit()
    cursor.close()
    connection.close()

#updates the db named in .envs with given SQL syntax
#leaves connection open and returns cursor
def db_update_SQL_syntax_open(SQL_syntax:str):
    #initialise - gets env vars and creates a connection & cursor
    connection, cursor = initialise_db()    
    #Create SQL commands from strings
    sql = str(SQL_syntax)
    #Execute changes
    cursor.execute(sql)
    
    return connection, cursor

# returns a list of dictionaries from a specified table
def db_table_to_list_of_dics(db_table:str):
     #initialise - gets env vars and creates a connection & cursor
    connection, cursor = initialise_db()    
    #Create SQL commands from strings
    sql = str(f"SELECT * FROM {db_table}")
    #Execute changes
    cursor.execute(sql)

    #get field names from db_table
    columns = cursor.description 
    list_of_dics = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    #commit chnages and close 
    connection.commit()
    cursor.close()
    connection.close()
    return list_of_dics

#Not currently used
def list_of_dics_to_db_table(db_table:str, list_to_upload): ### wip - may not be required
    #initialise - gets env vars and creates a connection & cursor
    connection, cursor = initialise_db()    
    #Create SQL commands from strings
    sql = str(f"SELECT * FROM {db_table}")
    #Execute query
    cursor.execute(sql)
    #get all field names from db table
    field_names = [i[0] for i in cursor.description]
    
    #iterate through list of dics and add to db if fields match
    for i in list_to_upload:
        for field in i:
            if field in field_names:
                sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

#returns a list of field names from named table
def get_field_names(table_name):
    #initialise - gets env vars and creates a connection & cursor
    connection, cursor = initialise_db()    
    #Create SQL commands from strings
    sql = str(f"SELECT * FROM {table_name}")
    #Execute query
    cursor.execute(sql)
    #get all field names from db table
    field_names = [i[0] for i in cursor.description]
    #close connection
    connection.commit()
    cursor.close()
    connection.close()

    return field_names

#Takes user input to add to new db item
def add_new_record_in_db(table_name):
    #get all field names from db table
    field_names = get_field_names(table_name)
    #remove auto inc primary key from list
    field_names_less_pk = []
    #ask for input of values for each field
    vals_list = []
    print("Please enter the value for each required field. ")
    for i in field_names:
        if i[-3:] != "_id":
            field_names_less_pk.append(i)
            vals_list.append(str(input(f"{i}: ")))
    #Add to db table
    add_to_db_table(table_name,field_names_less_pk,vals_list)

#prints the contents of a table from database
def print_db_table(table_name):
    #get all field names from db table
    field_names = get_field_names(table_name)

    #initialise - gets env vars and creates a connection & cursor
    connection, cursor = initialise_db()    
    #Create SQL commands from strings
    sql = str(f"SELECT * FROM {table_name}")
    #Execute query
    cursor.execute(sql)
    
    #iterate through each row of table and append to array to print
    rows = cursor.fetchall()
    print_arr = []

    for row in rows:
        print_row = []
        for i in row:
            print_row.append(str(i))
        print_arr.append(print_row)

    #print
    table = columnar(print_arr, field_names, no_borders=False)
    print(table)

    

    #commit changes and close 
    connection.commit()
    cursor.close()
    connection.close()

#deletes a record from named table
def delete_db_record(table_name):
   
    #Ask which item requires deleting
    delete_id = int(input("Enter id number of the item you would like to delete: "))   
    
    #Create SQL commands from strings
    sql = str(f"DELETE FROM {table_name} WHERE {table_name}_id={delete_id};")
    
    #Execute query
    db_update_SQL_syntax(sql)

def amend_db_record(table_name):
    #get the item that requires updating
    amend_id = input("\nEnter id number of the item you would like to amend: ")
    
    #get the field that requires updating from user input
    field_names = get_field_names(table_name)
    field_selected = select_from_list(field_names)
    amend_field_str = field_names[field_selected] # to do - stop from trying to change the id number

    #get the new required value
    new_value = input(f"\nWhat would you like the new value for {amend_field_str} to be? ")

    #Create SQL syntax
    SQL_syntax = f"UPDATE {table_name} SET {amend_field_str} = '{new_value}' WHERE {table_name}_id = {amend_id};"

    #update the database
    db_update_SQL_syntax(SQL_syntax)


