import csv

# CSV WITHOUT HEADER
# with open("data/addresses.csv") as csvfile:
#     reader = csv.reader(csvfile, skipinitialspace=True)
#     # print(list(reader))
#     # print(list(enumerate(reader)))
#     for index, row in enumerate(reader):
#         print(f'{index + 1} - {row[0]}')

# CSV WITH HEADER
with open("data/biostats.csv") as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    # print(list(reader))
    for row in reader:
        print(row['Name'])

        