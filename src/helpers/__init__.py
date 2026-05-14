import csv

from pandas import DataFrame

def read_csv(filename):
    with open(filename, 'r') as file:
        data_reader = csv.reader(file)
        data = [[int(item) if item.isnumeric() else item for item in row] for row in data_reader]
        # new_data = []
        # for row in data_reader:
        #    new_row = []
        #    for item in row:
        #        if item.isnumeric():
        #            new_row.append(int(item))
        #        else:
        #            new_row.append(item)
        #    new_data.append(new_row)
    return data


def merge_data(stock_df: DataFrame, sales_df: DataFrame) -> DataFrame:
    return combined_df

def update_stock(input_df: DataFrame) -> DataFrame:
    # Subtract sales from stock
    
    # Update the 'last_stock_update' date where a sale occurred
   
    return input_df

def write_data(data: DataFrame, filepath=None) -> None:
    pass