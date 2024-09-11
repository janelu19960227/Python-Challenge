import csv
import os

# Define file paths
file_path = "Resources/budget_data.csv"
output_dir = "analysis"
output_file = os.path.join(output_dir, "financial_analysis.txt")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Initialize variables
total_count = 0
total_value = 0
previous_profit = None
changes = []

# Read the CSV file and process data
with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        date, profit = row
        profit = float(profit)
        
        total_value += profit
        total_count += 1
        
        if previous_profit is not None:
            change = profit - previous_profit
            changes.append((date, change))
        
        previous_profit = profit

# Calculate average change
if changes:
    total_change = sum(change for _, change in changes)
    average_change = total_change / len(changes)
else:
    average_change = 0

# Find the greatest increase and decrease in profits
if changes:
    greatest_increase = max(changes, key=lambda x: x[1])
    greatest_decrease = min(changes, key=lambda x: x[1])
else:
    greatest_increase = ("", 0)
    greatest_decrease = ("", 0)

# Format values with dollar signs
total_value_formatted = "${:.2f}".format(total_value)
greatest_increase_value = "${:.2f}".format(greatest_increase[1])
greatest_decrease_value = "${:.2f}".format(greatest_decrease[1])

# Write results to the output file
with open(output_file, 'w') as outfile:
    outfile.write(f"Total count: {total_count}\n")
    outfile.write(f"Average Change: {average_change:.2f}\n")
    outfile.write(f"Total: {total_value_formatted}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} {greatest_increase_value}\n")
    outfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} {greatest_decrease_value}\n")

# Display results in the terminal
print(f"Results saved to {output_file}")
print(f"Total count: {total_count}")
print(f"Average Change: {average_change:.2f}")
print(f"Total: {total_value_formatted}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} {greatest_increase_value}")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} {greatest_decrease_value}")
