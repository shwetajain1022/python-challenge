import os
import csv

#initialise variables for reading budget_data.csv file and writing results to financialanalysis.txt
election_data_csv = os.path.join( 'Resources', 'election_data.csv')
results_txt = os.path.join( 'analysis', 'electiondatasummary.txt')

#initialising the lists and variables required for the computation
#reference - https://note.nkmk.me/en/python-multi-variables-values/
list_candidates_details, list_electionsummary,list_election =[],[],[]
i, totalVotes, totalCandidateVotes, winnerCandidateVote = 0,0,0,0
candidatesName, previousCandidateName, winnerCandidateName= "","",""

# Read in the CSV file
#reference -https://stackoverflow.com/questions/16108526/how-to-obtain-the-total-numbers-of-rows-from-a-csv-file-in-python
#https://www.w3resource.com/python-exercises/modules/python-module-csv-exercise-2.php
#total number of votes
with open(election_data_csv, 'r') as csvfile:
    totalVotes= len(list(csvfile))-1

print(f"Total votes : {totalVotes}") 

# Read in the CSV file and convert it to list
# Reference - https://linuxhint.com/import-csv-to-list-python/
with open(election_data_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    list_election = list(csvreader)

#reference : https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
#sort the list based on the candidate name
list_election.sort(key=lambda x: x[2])

#iterate through the list to create a new list contiaining the candidate name, total votes and percent of the total votes
for row in list_election:
    i += 1  
    
    if (i==1) :
        #initialise candidate name and previous candidate name in the first iteration   
        candidatesName = row[2]
        previousCandidateName = row[2]
    else :
        #initialise candidate name for all the other iterations   
        candidatesName = row[2]
    #store the total votes and percent of votes of the candidates into the list 
    if(previousCandidateName!=candidatesName):
        #create a list with candidate details
        list_candidates_details = []           
        list_candidates_details.append(previousCandidateName)
        list_candidates_details.append(totalCandidateVotes)
        list_candidates_details.append(round((totalCandidateVotes/totalVotes)*100,3))
        #append list_candidates_details to list_electionsummary list
        list_electionsummary.append(list_candidates_details)
        #reset the counter of totalCandidateVotes and update the previous candidate name with current candidate name
        totalCandidateVotes =1
        previousCandidateName = candidatesName  
    #store the total votes and percent of votes of the last candidate into the list       
    elif (totalVotes == i) :
        #add the counter the total candidate votes
        totalCandidateVotes += 1
        #create a list with candidate details
        list_candidates_details = []           
        list_candidates_details.append(candidatesName)
        list_candidates_details.append(totalCandidateVotes)
        list_candidates_details.append(round((totalCandidateVotes/totalVotes)*100,3))
        #append list_candidates_details to list_electionsummary list
        list_electionsummary.append(list_candidates_details)
    else :
        #add the counter the total candidate votes
        totalCandidateVotes +=1

i=0
#printing the election summary in the terminal and file
with open(results_txt, 'w') as r:
    print("Election Summary")
    print(f"-----------------------------------------------------------------------------")
    print(f"Total Votes: {totalVotes}")
    print(f"-----------------------------------------------------------------------------")
    r.write("Election Summary\n")
    r.write("-----------------------------------------------------------------------------\n")
    r.write("Total Votes: "+str(totalVotes)+"\n")
    r.write("-----------------------------------------------------------------------------\n")

    #calculate the winner and print the candidate summary
    for row in list_electionsummary :
        if i==0 :
            winnerCandidateName = row[0]
            winnerCandidateVote = row[2]
        elif(float(winnerCandidateVote)<float(row[2])) :
            winnerCandidateName = row[0]
            winnerCandidateVote = row[2]
        print(f"{row[0]}: {row[2]}% ({row[1]}) ")
        r.write(str(row[0]) + ": " + str(row[2])+ "% (" + str(row[1]) + ") \n")
        i+=1

    #print the winner in terminal and file
    print(f"-----------------------------------------------------------------------------")
    print(f"Winner: {winnerCandidateName}")     
    print(f"-----------------------------------------------------------------------------")  
    r.write("-----------------------------------------------------------------------------\n")
    r.write("Winner: "+winnerCandidateName+"\n")     
    r.write("-----------------------------------------------------------------------------\n")  
