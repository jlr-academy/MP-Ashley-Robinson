from unittest.mock import Mock, call
import utilities
from unittest.mock import patch, Mock

@patch("builtins.input")
@patch("builtins.print")
def test_print_list(mock_print:Mock, mock_input: Mock):
    #assemble
    mock_input.return_value = "2"
    #expected_print =
    dummy_data = [{"product_name":"Coke","price":"£1.50"},{"product_name":"Pepsi","price":"£1.45"}]

    #act
    utilities.print_list(dummy_data)

    #assert
    assert mock_print.call_args_list == [call(' '),call(1, {"product_name":"Coke","price":"£1.50"}),call(2, {"product_name":"Pepsi","price":"£1.45"}),call(' ')]


@patch("builtins.input")
def test_add_to_list(mock_input: Mock):
    #assemble
    mock_input.side_effect = ["Fanta","£2.00"]
    expected = [{"product_name":"Coke","price":"£1.50"},{"product_name":"Pepsi","price":"£1.45"},{"product_name":"Fanta","price":"£2.00"}]
    #expected_print =
    dummy_data = [{"product_name":"Coke","price":"£1.50"},{"product_name":"Pepsi","price":"£1.45"}]

    #act
    utilities.add_to_list(dummy_data)

    #assert
    assert expected == dummy_data  ## tested against dummy data as function will update global variable




@patch("builtins.input")
def test_select_from_list(mock_input: Mock):
    #assemble
    mock_input.side_effect = ["0","2"]
    expected = 1
    #expected_print =
    dummy_data = [{"product_name":"Coke","price":"£1.50"},{"product_name":"Pepsi","price":"£1.45"}]

    #act
    result = utilities.select_from_list(dummy_data)

    #assert
    assert expected == result  


def test_get_available_product_names_list():
    #Assemble
    expected =["Coke", "Pepsi"]
    dummy_data = [{"product_name":"Coke","price":"£1.50"},{"product_name":"Pepsi","price":"£1.45"}]
    #act
    result = utilities.get_available_product_names_list(dummy_data)
    #assert
    assert result == expected