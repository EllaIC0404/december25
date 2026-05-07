import csv

def read_csv(filename):
    with open(filename, 'r') as file:
        file_reader = csv.reader(file)
        return list(file_reader)
