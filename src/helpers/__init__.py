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
    # Calculate quantity sold per product_id by summing sales
    # Rename 'sales' column to 'quantity_sold' for clarity
    sales_data_dedup = sales_df.groupby('product_id')['sales'].sum().reset_index()
    sales_data_dedup.rename(columns={'sales': 'quantity_sold'}, inplace=True)
    combined_df = stock_df.merge(sales_data_dedup, on='product_id', how='left', validate='1:1')
    return combined_df

def update_stock(input_df: DataFrame) -> DataFrame:
    # Subtract sales from stock
    input_df['stock'] = input_df['quantity_in_stock'] - input_df['quantity_sold'].fillna(0)
    # Update the 'last_stock_update' date where a sale occurred
    mask = input_df['quantity_sold'] > 0
    input_df.loc[mask, 'last_stock_update'] = input_df.loc[mask, 'date']
   
    return input_df

def write_data(data: DataFrame, filepath=None) -> None:
        if filepath is None:
            filepath = 'updated_stock_data.csv'
        data.to_csv(filepath, index=False)
