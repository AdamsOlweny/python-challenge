'''
PyPoll Challenge
'''

# Import Dependancies. 
import os
import csv  

# initialize vars
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# open polling data: Resources/election_data.csv
with open(os.path.join("Resources","election_data.csv"), newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Conduct the ask
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # set candidate names
        candidatelist.append(row[2])
        # unique candidate names
    for candidate in set(candidatelist):
        unique_candidate.append(candidate) 
        votes_per_candidate = candidatelist.count(candidate)
        vote_count.append(votes_per_candidate) 
        percentage_vote = (votes_per_candidate/count)*100
        vote_percent.append(percentage_vote)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
#Print to terminal
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(round(vote_percent[i], 3)) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

 
with open('analysis/election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("-------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(round(vote_percent[i], 3)) +"% (" + str(vote_count[i]) + ")\n")
    text.write("-------------------------\n")
    text.write("Winner: " + winner + "\n")
    text.write("-------------------------\n")