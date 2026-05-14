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

def merge_data(list1, list2):
    joined_ids = []
    for row in list1:
        combined_list = []
        for row2 in list2:
            if row[0] == row2[0] and row[0] not in joined_ids:
                combined_list.append(row + row2[1:])
                joined_ids.append(row[0])
        if row[0] not in joined_ids:
            combined_list.append(row)
            joined_ids.append(row[0])
    return combined_list

def update_stock(input_list):
    for row in input_list[1:]:
        if len(row) == 11:
            row[2] = int(row[2]) - int(row[-2])
            row[4] = row[-1]
    return input_list