import csv

# CSV WITHOUT HEADER
# with open('data/addresses.csv') as csvfile:
#     # print(csvfile)
#     reader = csv.reader(csvfile, skipinitialspace=True)
#     # print(list(reader)) # a list of lists
#     for row in reader:
#         print(f'{row[0]} {row[1]}')

# CSV WITH HEADER
with open('data/biostats.csv') as csvfile:
    # print(csvfile)
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    # print(list(reader)) # list of dicts
    for row in reader:
        print(f"{row['Name']} - {row['Age']}")