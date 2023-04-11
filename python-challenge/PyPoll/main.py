import csv

#define file 
file_path = "/users/nikolm/Desktop/election_data.csv"

# define variables
total_votes = 0
vote_counts = {}   

# read the CSV file into a list
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    data = list(csvreader)

# calculate total votes and vote counts
for row in data:
    total_votes += 1
    candidate = row[2]
    if candidate not in vote_counts:
        vote_counts[candidate] = 0
    vote_counts[candidate] += 1

# calculate and print percentage of votes for each candidate
print("```text")
print("Election Results")
print("--------------------------")
print("Total Votes:", total_votes)
print("--------------------------")

winner = None
winning_votes = 0
for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) *100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > winning_votes:
        winner = candidate
        winning_votes = votes

print("---------------------------------")
print (f"Winner: {winner}")
print("---------------------------------")

# export text file with results
with open("Results.txt", "w") as file:
    file.write("```text\n") 
    file.write("Election Results\n")
    file.write("--------------------------\n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("--------------------------\n")
    for candidate, votes in vote_counts.items():
        percentage = (votes / total_votes) *100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("---------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("---------------------------------\n")
    file.write("```\n")

print("Results exported to Results.txt")
