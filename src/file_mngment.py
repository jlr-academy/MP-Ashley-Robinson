import json
import typing


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