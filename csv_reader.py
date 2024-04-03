import csv

# CSV WITHOUT HEADER
# with open('data/addresses.csv') as csvfile:
#     reader = csv.reader(csvfile, skipinitialspace=True)
#     # print(list(reader))
#     # reader is a kind of list
#     for row in reader:
#         print(f"Name: {row[0]}, City: {row[3]}")

# CSV WITH HEADER
with open('data/biostats.csv') as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    # print(list(reader))
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}")
