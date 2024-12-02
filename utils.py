import csv
def read_csv(csv_path, mode ='r'):
    with open(csv_path, mode = mode) as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines)
