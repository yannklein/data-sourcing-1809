import csv

# CSV WITHOUT HEADER
# with open('data/addresses.csv') as csvfile:
#     reader = csv.reader(csvfile, skipinitialspace=True)
    # print(list(reader))
    # for row in reader:
    #     print(row[0], row[1])
# CSV WITH HEADER
with open('data/biostats.csv') as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    # print(list(reader))
    for row in reader:
        print(f"{row['Name']} is {row['Age']}")