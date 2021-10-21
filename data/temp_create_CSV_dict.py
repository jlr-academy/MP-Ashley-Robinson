import csv



with open('couriers.csv', "w", newline="") as file:
    field_names = ['name', 'contact']
    
    writer = csv.DictWriter(file, fieldnames=field_names)
    p1 = {'name': 'Michael',
                    'contact': "07563366778"
                    }

    p2 = {'name': 'Kevin',
                    'contact': "07563366778",
                    }
    writer.writeheader()
    writer.writerow(p1)
    writer.writerow(p2)



with open('products.csv', "w", newline="") as file:
    field_names = ['product_name', 'price']
    
    writer = csv.DictWriter(file, fieldnames=field_names)
    p1 = {'product_name': 'Coke',
                    'price': "£1.50"
                    }

    p2 = {'product_name': 'Fanta',
                    'price': "£1.45",
                    }
    writer.writeheader()
    writer.writerow(p1)
    writer.writerow(p2)