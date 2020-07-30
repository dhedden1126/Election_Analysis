# Add dependencies.
import csv
import os
# Assign variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign variable to save the file to a path.
file_to_save = os.path.join("Analysis/election_results_challenge.txt") 

# Initialize counter
total_votes = 0

county_options=[]

county_votes = {}

# Candidate Options-Empty List []
candidate_options = []
#1. Candidate Votes-Empty Dictionary {}
candidate_votes = {}

# Final Solutions
winning_candidate = ""
winning_count = 0
winning_percentage = 0
county_turnout = ""
county_count = 0
county_percentage= 0

# Open csv and read 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read header row.
    headers = next(file_reader)

# Print each row in csv
    for row in file_reader:
        # +1 as it iterates through each row
        total_votes += 1

        # Print candidate name on each row (2) counting 0,1,2 Column A:C
        candidate_name = row[2]

        county_name =row[1]

        if county_name not in county_options:
            county_options.append(county_name)

            county_votes[county_name] = 0

        county_votes[county_name] +=1

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            # Count candidate's votes
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] +=1

#Save to txt file
with open(file_to_save, "w") as txt_file:

    election_results_challenge = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")
    print(election_results_challenge, end="")

    # Save final vote count to txt file
    txt_file.write(election_results_challenge)

    for county in county_votes:
        # Count and solve for percentage of votes
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(county_results)
        #  Save the candidate results to text file.
        txt_file.write(county_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > county_count) and (vote_percentage > county_percentage):
            county_count = votes
            winning_county = county
            county_percentage = vote_percentage
    # Print winning candidate's results to the terminal.
    winning_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    # Save winning candidate's results to a text file.
    txt_file.write(winning_county_summary)
    
    for candidate in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's vote count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate's results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print winning candidate's results to the terminal.(Format)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to text file.
    txt_file.write(winning_candidate_summary)