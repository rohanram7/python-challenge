import csv
import os

# Define the path to the directory where the text file should be saved
output_directory = 'C:\\Users\\tarai\\OneDrive\\Documents\\python-challenge\\python-challenge\\PyPoll\\analysis'

# Ensure the output directory exists; if not, create it
os.makedirs(output_directory, exist_ok=True)

# Define the path to the CSV file
election_data = 'C:\\Users\\tarai\\OneDrive\\Documents\\python-challenge\\python-challenge\\PyPoll\\Resources\\election_data.csv'

# Initialize variables to store vote counts and candidate names
total_votes = 0
candidate_votes = {}

# Read the election data from the CSV file
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip the header row
    next(csvreader)
    
    # Iterate through each row in the CSV file
    for row in csvreader:
        # Update the total vote count
        total_votes += 1
        
        # Extract the candidate name from the row
        candidate_name = row[2]
        
        # Check if the candidate is already in the dictionary
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            # Initialize the candidate's vote count
            candidate_votes[candidate_name] = 1


# Initialize variables to track the winning candidate and vote count
winning_candidate = ""
winning_votes = 0

# Loop through the candidate votes to find the winner
for candidate, votes in candidate_votes.items():
    if votes > winning_votes:
        winning_candidate = candidate
        winning_votes = votes

# Define the path for the output text file
output_file = os.path.join(output_directory, "election_results.txt")

# Write the results to the text file
with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")

    # Loop through the candidate votes and write their results to the text file
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winning_candidate}\n")
    txtfile.write("-------------------------\n")

# Define the path for the output text file
output_file = os.path.join(output_directory, "election_results.txt")

try:
    # Open and write the results to the text file
    with open(output_file, 'w') as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Total Votes: {total_votes}\n")
        txtfile.write("-------------------------\n")

        # Loop through the candidate votes and write their results to the text file
        for candidate, votes in candidate_votes.items():
            percentage = (votes / total_votes) * 100
            txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        txtfile.write("-------------------------\n")
        txtfile.write(f"Winner: {winning_candidate}\n")
        txtfile.write("-------------------------\n")

    print("Election results have been saved to election_results.txt")
except Exception as e:
    print(f"An error occurred while writing the results: {e}")


