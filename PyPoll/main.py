import csv
import os

file = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidate_list = []
candidate_dict = {}


with open(file) as data:
    csvreader = csv.reader(data, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:


# 