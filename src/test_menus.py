import menus
from unittest.mock import patch, Mock




@patch("builtins.input")
@patch("builtins.print")
def test_start_menu_choice(mock_print:Mock, mock_input: Mock):
    #assemble
    mock_input.return_value = "2"
    expected_print = "\n    1   Inventory\n    2   Couriers\n    3   Save Changes\n    4   Orders\n    0   Exit app"
    expected_return = 2
    #act
    actual = menus.start_menu_choice()
    #assert
    mock_print.assert_called_with(expected_print)
    assert expected_return == actual
    
    
@patch("menus.print_list")
@patch("builtins.input")
@patch("builtins.print")
def test_products_menu_choice(mock_print:Mock, mock_input: Mock, mock_print_list:Mock):
    #assemble
    expected_print= '''
        What would you like to do with your products?

        1   See Products
        2   Amend Products
        3   Create New products
        0   Exit to Main Menu
        '''
    mock_input.side_effect = ["1", "0", "0"]
    dummy_product_list =[{"Coke":"£1.50"},{"Fanta": "£1.45"}, {"Pepsi":"£2.00"}]
    #act
    menus.products_menu_choice(dummy_product_list)
    #assert
    mock_print.assert_called_with(expected_print)
    mock_print_list.assert_called()
    mock_print_list.assert_called_with(dummy_product_list)
    assert mock_print_list.called



@patch("menus.print_list")
@patch("builtins.input")
@patch("builtins.print")
def test_couriers_menu_choice(mock_print:Mock, mock_input: Mock, mock_print_list:Mock):
     #assemble
    expected_print= '''
        What would you like to do with Couriers?

        1   See Couriers
        2   Amend Couriers
        3   Create new Courier
        0   Exit to Main Menu
        '''
    mock_input.side_effect = ["1", "0", "0"]
    dummy_couriers_list =[{"name":"Michael","contact":"07563366778"},{"name":"Kevin","contact":"07563366778"}]
    #act
    menus.couriers_menu_choice(dummy_couriers_list)
    #assert
    mock_print.assert_called_with(expected_print)
    mock_print_list.assert_called()
    mock_print_list.assert_called_with(dummy_couriers_list)
    assert mock_print_list.called



@patch("menus.print_list")
@patch("builtins.input")
@patch("builtins.print")
def test_orders_menu_choice(mock_print:Mock, mock_input: Mock, mock_print_list:Mock):
     #assemble
    expected_print= '''
        What would you like to do with Orders?

        1   See Orders
        2   Amend Orders
        3   Create New Order
        4   Update Customer Fields
        5   Update Order Status
        0   Exit to Main Menu
        '''
    mock_input.side_effect = ["1", "0", "0"]
    dummy_orders_list =[{
        "customer_name": "Steve",
        "customer_address": "Unit 32, 1 Main Street, LONDON, WH1 2ER",
        "customer_phone": "0789887554",
        "courier": "DHL",
        "status": "preparing"
        },{
        "customer_name": "John",
        "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
        "customer_phone": "0789887334",
        "courier": "Parcel Force",
        "status": "preparing"
        },{
        "customer_name": "Mike",
        "customer_address": "2 South Street, Birmingham, BD1 2ER",
        "customer_phone": "0789667334",
        "courier": "Parcel Force",
        "status": "Delivered"
        }]
    #act
    menus.orders_menu_choice(dummy_orders_list)
    #assert
    mock_print.assert_called_with(expected_print)
    mock_print_list.assert_called()
    mock_print_list.assert_called_with(dummy_orders_list)
    assert mock_print_list.called