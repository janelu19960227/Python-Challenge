import csv
import os
from collections import Counter

# Define file paths
file_path = 'Resources/election_data.csv'
output_dir = 'analysis'
output_file = os.path.join(output_dir, 'election_results.txt')

# Create the 'analysis' folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Initialize variables
total_entries = 0
candidate_counts = Counter()

# Open and read the CSV file
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    
    # Skip the header row
    next(reader)
    
    # Iterate over the rows to count entries and candidate votes
    for row in reader:
        if row[0]:  
            total_entries += 1
            candidate_name = row[2]  
            candidate_counts[candidate_name] += 1

# Determine the winner
if candidate_counts:
    winner = max(candidate_counts, key=candidate_counts.get)
    winner_count = candidate_counts[winner]
    winner_percentage = (winner_count / total_entries) * 100
else:
    winner = "None"
    winner_count = 0
    winner_percentage = 0

# Write the results to the output file
with open(output_file, mode='w') as file:
    file.write(f'Total Entries in Column A: {total_entries}\n\n')
    file.write('Candidate Votes:\n')
    
    for candidate, count in candidate_counts.items():
        percentage = (count / total_entries) * 100
        file.write(f'{candidate}: {count} votes ({percentage:.2f}%)\n')
    
    file.write(f'\nWinner: {winner}\n')
    

# Display the results
print(f'Results saved to {output_file}')
print(f'Total Entries in Column A: {total_entries}')
print('Candidate Votes:')
for candidate, count in candidate_counts.items():
    percentage = (count / total_entries) * 100
    print(f'{candidate}: {count} votes ({percentage:.2f}%)')

print(f'\nWinner: {winner}')