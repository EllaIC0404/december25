import csv
import os
import pytest

from helpers import read_csv, merge_data

@pytest.fixture(scope="module")
def stock_file():
    with open('stock_data.csv', 'w', newline='') as stock_file:
        fieldnames = ['product_id', 'manufacturer_name', 'quantity_in_stock', 'supplier_contact',
                      'last_stock_update', 'price_per_unit', 'category', 'location_in_warehouse', 'reorder_threshold']
        stock_writer = csv.DictWriter(stock_file, fieldnames=fieldnames)
        stock_writer.writeheader()
        stock_writer.writerow({'product_id' : '123', 'manufacturer_name' : 'TestCompany','quantity_in_stock' : "10",
                               'supplier_contact' : '123-456-7891', 'last_stock_update' : '01/01/2000',
                               'price_per_unit': '100.00', 'category' : 'Test', 'location_in_warehouse' : 'A1', 
                               'reorder_threshold': '1'})
    yield
    os.remove('stock_data.csv')

@pytest.fixture(scope="module")
def sales_file():
    with open('sales_data.csv', 'w', newline='') as sales_file:
        fieldnames = ['product_id', 'sales', 'date']
        sales_writer = csv.DictWriter(sales_file, fieldnames=fieldnames)
        sales_writer.writeheader()
        sales_writer.writerow({'product_id': '123', 'sales': '5', 'date': '01/01/2000'})
    yield
    os.remove('sales_data.csv')

# As a user I want the application to be able to read in 
# (at least) two csv files to be processed (stock and sales data). 
def test_read_csv(stock_file):
    # Arrange - set up input and expected output
    filepath = 'stock_data.csv'
    expected_length = 2
    expected_id = 123
    expected_quantity = 10

    # Act
    stock_data = read_csv(filepath)

    # Assert
    assert len(stock_data) == expected_length
    assert stock_data[1][0] == expected_id
    assert stock_data[1][2] == expected_quantity


def test_read_sales_csv(sales_file):
    # Arrange - set up input and expected output
    filepath = 'sales_data.csv'
    expected_length = 2
    expected_id = 123
    expected_quantity = 5

    # Act
    sales_data = read_csv(filepath)

    # Assert
    assert len(sales_data) == expected_length
    assert sales_data[1][0] == expected_id
    assert sales_data[1][1] == expected_quantity


def test_datasets_merged(stock_file, sales_file):
    # Arrange - set up input and expected output
    stock_data = read_csv('stock_data.csv')
    sales_data = read_csv('sales_data.csv')
    expected_columns = 11
    expected_quantity = 5

    # Act
    merged_data = merge_data(stock_data, sales_data)

    # Assert
    assert len(merged_data[0]) == expected_columns
    assert merged_data[1][9] == expected_quantity