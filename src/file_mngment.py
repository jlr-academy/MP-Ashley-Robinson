import json

import csv


# use to create a file for test
''' order_list =[{"customer_name": "Steve","customer_address": "Unit 32, 1 Main Street, LONDON, WH1 2ER","customer_phone": "0789887554","courier": "Mike","status": "preparing"},{"customer_name": "John","customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER","customer_phone": "0789887334","courier": "steve","status": "preparing"}]
with open("data\orders.json", "w") as file:
    json.dump(order_list, file) '''


#takes a list and adds to specfied file
def list_to_json(list_to_load:list, file_path: str):
    with open(file_path, "w") as file:
        json.dump(list_to_load, file)

#takes a dictionary and adds to specfied file
def json_to_list(list_to_update: list, file_path: str):
    with open(file_path, "r") as file:
        json_object = json.load(file)
        if type(json_object) == list:
            for order in json_object:
                list_to_update.append(order)
        else:
            pass # add error handling


#reads a CSV and creates a list of dictionaries
def csv_to_list_of_dicts(list_to_load:list, file_path: str):
    with open(file_path, "r", encoding='utf-8') as file:
        list_temp = [{k: v for k, v in row.items()}
            for row in csv.DictReader(file, skipinitialspace=True)]
        for i in list_temp: # Dirty fix for global variables
            list_to_load.append(i)
    




def list_of_dicts_to_csv(list_to_save:list, file_path: str):
    with open(file_path, "w", newline="", encoding='utf-8') as file:
        
        #get dictionary field names from first list item
        field_names = []
        for key in list_to_save[0]:
            field_names.append(key)

        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()

        #loop through each list item and add to CSV file
        for item in list_to_save:
            writer.writerow(item)

#use to test CSV file functionality
''' file_path = r'data\test.csv'
list = [{'color': 'blue', 'fruit': 'apple', 'pet': 'dog'},{'color': 'red', 'fruit': 'banana', 'pet': 'cat'}]
list_of_dicts_to_csv(list,file_path) 
print(csv_to_list_of_dicts(list,file_path)) '''

def save_change(products_list,courier_list,orders_list):
    list_of_dicts_to_csv(products_list,'./data/products.csv')
    list_of_dicts_to_csv(courier_list,'./data/couriers.csv')
    list_to_json(orders_list, "data\orders.json")