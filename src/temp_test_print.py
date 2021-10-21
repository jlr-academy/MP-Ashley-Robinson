from utilities import print_list
import file_mngment






file_path = r'data\test.csv'
list = [{'color': 'blue', 'fruit': 'apple', 'pet': 'dog'},{'color': 'red', 'fruit': 'banana', 'pet': 'cat'}]
file_mngment.list_of_dicts_to_csv(list,file_path) 
print(file_mngment.csv_to_list_of_dicts(list,file_path))


print_list(list)