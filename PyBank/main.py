import os
import csv
budget_data_csv = os.path.join( 'Resources', 'budget_data.csv')
results_txt = os.path.join( 'analysis', 'financialanalysis.txt')
budget_data = []
changesToProfitLoss = []
i = 0
totalAmt = 0
totalNoOfMonths = 0
avgOfProfitLoss = 0
noOfMonths= []
greatestIncreaseInProfitLosses = []
minimumIncreaseInProfitLosses =[]

def GreatestProfitLosses(changesToProfitLoss1):
    listOfProfitLoss = [float(x) for x in changesToProfitLoss1 ]
    return listOfProfitLoss.index(max(listOfProfitLoss))

def MinimumProfitLosses(changesToProfitLoss):
    listOfProfitLoss = [float(x) for x in changesToProfitLoss ]
    return listOfProfitLoss.index(min(listOfProfitLoss))

with open(budget_data_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # Loop through the data
    i=0
    for row in csvreader:                
        if i>=1 :
            noOfMonths.append(row[0])
            changesToProfitLoss.append(float(row[1])-(previousProfitLoss))
            #print(f"{row[0]} : {changesToProfitLoss[i-1]}")
        totalAmt = totalAmt + float(row[1])
        totalNoOfMonths = totalNoOfMonths+1
        i+=1
        previousProfitLoss = float(row[1])
with open(results_txt, 'w') as r:
    print("Financial Analysis")
    r.write("Financial Analysis")
    print("\n")
    r.write("\n")
    print("--------------------------------------------------------------------------------------------")
    r.write("--------------------------------------------------------------------------------------------")
    print("\n")
    r.write("\n")
    print(f"Total Months: {totalNoOfMonths}") 
    r.write("Total Months: {totalNoOfMonths}") 
    print("\n")
    r.write("\n")
    print(f"Total: {totalAmt}") 
    r.write("Total: {totalAmt}")     
    print("\n")
    r.write("\n")
    avgOfProfitLoss = totalAmt/totalNoOfMonths
    print(f"Average : ${avgOfProfitLoss}")
    r.write("Average : ${:,.2f}".format(avgOfProfitLoss)) 
    print("\n")
    r.write("\n")
    greatestProfitLossesKey =GreatestProfitLosses(changesToProfitLoss)
    greatestIncreaseInProfitLosses = changesToProfitLoss[greatestProfitLossesKey]
    greatestIncreaseMonthInProfitLosses = noOfMonths[greatestProfitLossesKey]
    print(f"Greatest Increase in Profits: {greatestIncreaseMonthInProfitLosses}  (${str(greatestIncreaseInProfitLosses)})")
    r.write("Greatest Increase in Profits: "+str(greatestIncreaseMonthInProfitLosses)+"  ($"+str(greatestIncreaseInProfitLosses)+")") 
    print("\n")
    r.write("\n")
    minimumProfitLossesKey =MinimumProfitLosses(changesToProfitLoss)
    minimumIncreaseInProfitLosses = changesToProfitLoss[minimumProfitLossesKey]
    minimumIncreaseMonthInProfitLosses = noOfMonths[minimumProfitLossesKey]
    print(f"Greatest Decrease in Profits: {minimumIncreaseMonthInProfitLosses}  (${str(minimumIncreaseInProfitLosses)})")
    r.write("Greatest Decrease in Profits: "+ str(minimumIncreaseMonthInProfitLosses)+"  ($"+str(minimumIncreaseInProfitLosses)+")") 

