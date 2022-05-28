import random
import csv

values = []
with open("medium_data.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        values.append(row[7])

print(values)

sample_1 = [[values[0]]]

for i in range(100):
    sample_1.append([random.choice(values)])

with open("sample_data.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sample_1)
