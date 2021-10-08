import json

order_list =[{"customer_name": "Steve","customer_address": "Unit 32, 1 Main Street, LONDON, WH1 2ER","customer_phone": "0789887554","courier": "Mike","status": "preparing"},{"customer_name": "John","customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER","customer_phone": "0789887334","courier": "steve","status": "preparing"}]





with open("data\orders.json", "w") as file:
    json.dump(order_list, file)




with open("data\orders.json", "r") as file:
    json_object = json.load(file)
    print(type(json_object)) 