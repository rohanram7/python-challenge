import csv
import os

# Define the path to the budget_data.csv file
budget_data = os.path.join('Resources', 'budget_data.csv')

# Initialize variables to store financial data
total_months = 0
total_profit_losses = 0
changes = []
previous_profit_loss = None
greatest_increase = {"date": None, "amount": 0}
greatest_decrease = {"date": None, "amount": 0}

# Read data from the CSV file
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)
    
    # Loop through each row in the dataset
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Calculate the total number of months and the net total amount of profit/losses
        total_months += 1
        total_profit_losses += profit_loss
        
        # Calculate the change in profit/losses
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            
            # Update greatest increase and decrease if applicable
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            elif change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change
        
        # Update the previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change in profit/losses
average_change = sum(changes) / len(changes)

# Specify the path for the output file
output_file_path = r"C:\Users\tarai\OneDrive\Documents\python-challenge\python-challenge\PyBank\analysis\financial_analysis.txt"

# Open the file in write mode and write the results to it
with open(output_file_path, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_profit_losses}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

# Print a message to confirm that the file has been written
print(f"Results have been saved to '{output_file_path}'")
