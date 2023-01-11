import csv

# CSV WITHOUT HEADER
# with open('data/addresses.csv') as csvfile:
#     # print(csvfile) #<_io.TextIOWrapper name='data/addresses.csv' mode='r' encoding='UTF-8'>
#     reader = csv.reader(csvfile, skipinitialspace=True)
#     print(list(reader))

# CSV WITH HEADER
with open('data/biostats.csv') as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    print(list(reader))
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years-old")