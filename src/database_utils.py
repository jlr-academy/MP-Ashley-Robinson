import pymysql 
import os
from dotenv import load_dotenv



'''# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")'''

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
def add_to_db(table_name:str,fields:list,vals:list):
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


# db_to_list_of_dics

def db_table_to_list_of_dics(list_to_update:list, db_table):
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






