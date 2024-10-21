import os
import csv

# File paths
input_file = r"C:\Users\Mimy\OneDrive\Desktop\python-challenge\PyPoll\Resources\election_data.csv"
output_file = os.path.join("analysis", "election_data.txt")

# initializing the variable
candidate_votes = {}
total_vote = 0
winner = ""
winning_count = 0

# Opening the CSV file and process it
with open(input_file) as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Skipping the header row
# looping to be able to find the total votes
    for row in reader:
        candidate_name = row[2]  # Candidate name is in the third column
        total_vote += 1  # Counting the total number of votes
        #checking if there is a name which is not on the list 
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
           # Incrementing the vote count for the candidate
        candidate_votes[candidate_name] += 1

# Openning the output file for writing the results
with open(output_file, "w") as datafile:
    # Writting the results to the file
    datafile.write("Election Results\n")
    datafile.write("----------------------\n")
    datafile.write(f"Total Votes: {total_vote}\n")
    datafile.write("----------------------\n")
    
    for candidate, votes in candidate_votes.items():
        # in case no data in the file
        if total_vote != 0:
     #calculating the percentage 
            percent_vote = (votes / total_vote) * 100
        #writing the names and percentages for each candidate
            datafile.write(f"{candidate}: {percent_vote:.3f}% ({votes})\n")
        else:
            datafile.write("N/A")
        # Determining the winning candidate
        if votes > winning_count:
            winning_count = votes
            winner = candidate
    # Writing the results again to the file
    datafile.write("----------------------\n")
    datafile.write(f"Winner: {winner}\n")
    datafile.write("----------------------\n")