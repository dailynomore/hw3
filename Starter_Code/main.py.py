
import csv
import os

total_months = 0
total_profit_loss = 0
previous_profit_loss = None
profit_loss_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", float("inf")]

# Open and read the csv file


with open(r"C:\Users\wayne\Downloads\Starter_Code (2)\Starter_Code\PyBank\Resources\budget_data.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        # Count the total number of months
        total_months += 1

        # Calculate the net total amount of "Profit/Losses"
        total_profit_loss += int(row["Profit/Losses"])

        # Calculate the changes in "Profit/Losses", if previous month is available
        if previous_profit_loss is not None:
            change = int(row["Profit/Losses"]) - previous_profit_loss
            profit_loss_change.append(change)

            # Check for the greatest increase in profits
            if change > greatest_increase[1]:
                greatest_increase[0] = row["Date"]
                greatest_increase[1] = change

            # Check for the greatest decrease in profits
            if change < greatest_decrease[1]:
                greatest_decrease[0] = row["Date"]
                greatest_decrease[1] = change

        previous_profit_loss = int(row["Profit/Losses"])

# Calculate the average change in "Profit/Losses"
average_change = sum(profit_loss_change) / len(profit_loss_change)

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write the analysis to a text file
with open('financial_analysis.txt', mode='w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")


total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read in the CSV file
with open(r"C:\Users\wayne\Downloads\Starter_Code (2)\Starter_Code\PyPoll\Resources\election_data.csv", 'r') as csvfile:

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