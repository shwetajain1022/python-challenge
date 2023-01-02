import os
import csv
import statistics
#initialise variables for reading budget_data.csv file and writing results to financialanalysis.txt
budget_data_csv = os.path.join( 'Resources', 'budget_data.csv')
results_txt = os.path.join( 'analysis', 'financialanalysis.txt')

#initialising the lists and variables required for the computation
#reference - https://note.nkmk.me/en/python-multi-variables-values/
budget_data, changesToProfitLoss, noOfMonths, greatestIncreaseInProfitLosses, minimumIncreaseInProfitLosses =[],[],[],[],[]
i, totalAmt, totalNoOfMonths, avgOfProfitLoss = 0,0,0,0

#function to find the average of the change of profit and loss
#reference - https://www.geeksforgeeks.org/find-average-list-python/?ref=lbp
def AverageProfitLosses(changesToProfitLoss1):
    listOfProfitLoss = [float(x) for x in changesToProfitLoss1 ]
    return round(statistics.mean(listOfProfitLoss),2)

#function to find the greatest profit
def GreatestProfitLosses(changesToProfitLoss1):
    listOfProfitLoss = [float(x) for x in changesToProfitLoss1 ]
    return listOfProfitLoss.index(max(listOfProfitLoss))

#function to find the greatest loss
def MinimumProfitLosses(changesToProfitLoss):
    listOfProfitLoss = [float(x) for x in changesToProfitLoss ]
    return listOfProfitLoss.index(min(listOfProfitLoss))

#read values from the budget_data.csv file
with open(budget_data_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # Loop through the data to calculate to
    i=0
    for row in csvreader:                
        if i>=1 :
            noOfMonths.append(row[0])
            changesToProfitLoss.append(float(row[1])-(previousProfitLoss))
        totalAmt = totalAmt + float(row[1])
        totalNoOfMonths = totalNoOfMonths+1
        i+=1
        previousProfitLoss = float(row[1])

#Writing to the terminal and the file
with open(results_txt, 'w') as r:
    print("Financial Analysis")
    r.write("Financial Analysis\n")

    print("--------------------------------------------------------------------------------------------")
    r.write("--------------------------------------------------------------------------------------------\n")

    print(f"Total Months: {totalNoOfMonths}\n") 
    r.write("Total Months: "+str(totalNoOfMonths)+"\n") 

    print(f"Total: ${totalAmt}\n") 
    r.write("Total: $"+str(totalAmt)+"\n")

    #Call to calculate average of profit loss     
    avgOfProfitLoss = AverageProfitLosses(changesToProfitLoss)
    print(f"Average : ${avgOfProfitLoss}\n")
    r.write("Average : ${:,.2f}".format(avgOfProfitLoss)+"\n")

    #Call to calculate the greatest change in the profit and loss
    greatestProfitLossesKey =GreatestProfitLosses(changesToProfitLoss)
    greatestIncreaseInProfitLosses = changesToProfitLoss[greatestProfitLossesKey]
    greatestIncreaseMonthInProfitLosses = noOfMonths[greatestProfitLossesKey]

    #Printing the greatest change in the profit and loss
    print(f"Greatest Increase in Profits: {greatestIncreaseMonthInProfitLosses}  (${str(greatestIncreaseInProfitLosses)})\n")
    r.write("Greatest Increase in Profits: "+str(greatestIncreaseMonthInProfitLosses)+"  ($"+str(greatestIncreaseInProfitLosses)+")\n") 

    #Call to calculate the greatest decrease in the profit and loss
    minimumProfitLossesKey =MinimumProfitLosses(changesToProfitLoss)
    minimumIncreaseInProfitLosses = changesToProfitLoss[minimumProfitLossesKey]
    minimumIncreaseMonthInProfitLosses = noOfMonths[minimumProfitLossesKey]

    #Printing the greatest decrease change in the profit and loss 
    print(f"Greatest Decrease in Profits: {minimumIncreaseMonthInProfitLosses}  (${str(minimumIncreaseInProfitLosses)})")
    r.write("Greatest Decrease in Profits: "+ str(minimumIncreaseMonthInProfitLosses)+"  ($"+str(minimumIncreaseInProfitLosses)+")\n") 

