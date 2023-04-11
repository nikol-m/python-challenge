import csv
import urllib.request

#define file 
url_path = "https://raw.githubusercontent.com/nikol-m/python-challenge/main/python-challenge/PyPoll/Resources/election_data.csv"


# define variables
total_votes = 0
vote_counts = {}   

# read the CSV file into a list
with urllib.request.urlopen(url_path)as url: 
    csvreader = csv.reader(url.read().decode().splitlines())
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

# initialize the winner variable to None and winning_votes to 0
winner = None
winning_votes = 0

# iterate through the vote_counts dictionary to calculate the % of votes for each candidate; 
# print the results 
# update the winner variable if a candidate has received more votes than the current winner
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
