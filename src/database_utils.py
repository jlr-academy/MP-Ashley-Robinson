import pymysql 
import os
from dotenv import load_dotenv
from utilities import select_from_list


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
    #initialise - gets env vars and creates a connection & cursor
    connection, cursor = initialise_db()

    #create fields string & values string
    converted_list = [str(element) for element in fields]
    fields_str = ",".join(converted_list)

    converted_list = ["'" + str(element) + "'" for element in vals]
    vals_str = ",".join(converted_list)
    
    #Create SQL commands from strings
    sql = f"INSERT INTO {table_name}({fields_str}) VALUES({vals_str});"
    
    #Execute changes
    cursor.execute(sql)

    #commit chnages and close 
    connection.commit()
    cursor.close()
    connection.close()
    
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

def get_field_names(db_table):
    #initialise - gets env vars and creates a connection & cursor
    connection, cursor = initialise_db()    
    #Create SQL commands from strings
    sql = str(f"SELECT * FROM {db_table}")
    #Execute query
    cursor.execute(sql)
    #get all field names from db table
    field_names = [i[0] for i in cursor.description]

    connection.commit()
    cursor.close()
    connection.close()

    return field_names


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

def print_db_table(table_name):
    #get all field names from db table
    field_names = get_field_names(table_name)

    #initialise - gets env vars and creates a connection & cursor
    connection, cursor = initialise_db()    
    
    #Create SQL commands from strings
    sql = str(f"SELECT * FROM {table_name}")
    
    #Execute query
    cursor.execute(sql)
    #iterate through table and print each row
    rows = cursor.fetchall()
    for row in rows:
        j=0
        print_str = ""
        for i in row:
            ### calculate white space requirement for print -to do
            print_str = print_str + f"{field_names[j]}: {i},  "
            j=j+1
        print(print_str)

    #commit changes and close 
    connection.commit()
    cursor.close()
    connection.close()


#deletes a record from named table
def delete_db_record(table_name):
   
    #Ask which item requires deleting
    delete_id = int(input("Enter id number of the item you would like to delete: "))

    #initialise - gets env vars and creates a connection & cursor
    connection, cursor = initialise_db()    
    
    #Create SQL commands from strings
    sql = str(f"DELETE FROM {table_name} WHERE {table_name}_id={delete_id};")
    
    #Execute query
    cursor.execute(sql)

    #commit changes and close 
    connection.commit()
    cursor.close()
    connection.close()

def amend_db_record(table_name):
    #get the item that requires updating
    amend_id = input("\n Enter id number of the item you would like to amend: ")
    
    #get the field that requires updating
    field_names = get_field_names(table_name)
    field_selected = select_from_list(field_names)
    amend_field_str = field_names[field_selected] # to do - stop from trying to change the id number


    #get the new required value
    new_value = input(f"\n What would you like the new value for {amend_field_str} to be? ")
    #Create SQL syntax
    SQL_syntax = f"UPDATE {table_name} SET {amend_field_str} = '{new_value}' WHERE {table_name}_id = {amend_id};"

    #update the database
    db_update_SQL_syntax(SQL_syntax)





### below used to create dummy data
''' create_new_table("couriers")
create_new_table("products")
courier_fields_list =["couriers_name", "contact"]
product_field_list =["products_name","price"]

add_to_db("couriers",courier_fields_list,["DHL","07563355888"])
add_to_db("couriers",courier_fields_list,["Parcelforce","07563355999"])
add_to_db("products",product_field_list,["Pepsi","£0.75"])
add_to_db("products",product_field_list,["Sandwich","£2.50"])
add_to_db("products",product_field_list,["Crisps","£0.90"]) '''