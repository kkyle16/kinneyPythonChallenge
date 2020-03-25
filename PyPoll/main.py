import csv
import os

file = os.path.join("Resources", "election_data.csv")

# Establishes a dictionary to keep track of candidates and their votes, and two iterative variables to track 
# the number of candidates and the total votes.
candidate_dict = {}
total_candidates = 0
rows = 0

#Opens the csv
with open(file) as data:
    csvreader = csv.reader(data, delimiter = ",")
    header = next(csvreader)

    # Populates the dictionary by checking to see if the key already exists. 
    # If it does, increases the vote by 1. If it doesn't, creates a new key with 1 vote. 
    for row in csvreader:
        if row[2] in candidate_dict:
            candidate_dict[row[2]] += 1
        else:
            candidate_dict[row[2]] = 1
            total_candidates += 1
        rows += 1    

# A function to return the election results in a specific format. Reads in the number of candidates and total votes cast
def analysis(num_candidates, num_votes):
    
    # Establishes variables inside this function. winner_votes helps calculate the winner and result is the return
    winner_votes = 0
    result = f"Election Results\n-------------------------\nTotal Votes: {num_votes}\n-------------------------"

    # Loop that cycles through the keys in the dictionary, returning the candidate and their total votes
    for i in range (1, num_candidates + 1):
        name = list(candidate_dict.keys())[i - 1]
        votes = candidate_dict[name]
        percent_votes = votes / num_votes * 100
        percent_votes = round(percent_votes, 3)

        if votes > winner_votes:
            winner = name
            winner_votes = votes
        
        # concatenates each candidates results to the total results
        result += f"\n{name}: {percent_votes}% ({votes})"
    
    
    result += f"\n-------------------------\nWinner: {winner}\n-------------------------"
    return result


print(analysis(total_candidates, rows))

# Outputs the election results to a text file. This is why I decided to return a string from the function
# rather than issue print statements inside the analysis function.
output_file = "output.txt"
with open(output_file, "w") as doc:
    doc.write(analysis(total_candidates, rows))