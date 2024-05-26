import csv
import os

total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read in the CSV file
with open('election_data.csv', 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        # Count the total number of votes
        total_votes += 1

        # Count the number of votes for each candidate
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1

# Determine the winner of the election
for candidate, votes in candidates.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Generate Output Summary
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

# Append each candidate's result to the output
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

# Append the winner to the output
output += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# Print the output (to terminal)
print(output)

# Export the results to text file
output_file = os.path.join("election_results.txt")
with open(output_file, "w") as txt_file:
    txt_file.write(output)