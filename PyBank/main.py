'''
PyBank Challenge

Analysis of budget_data as defined in the README.md
'''

# Import Dependancies. 
import os
import csv

# python lists to store the data 
count = 0
profit = []
monthly_changes = []
total_profit = 0
profit_change = 0
initial_profit = 0
date = [] 

# Open the CSV data: Resources/budget.csv
with open(os.path.join("Resources", "budget_data.csv"), newline="") as csv_data:
    csvreader = csv.reader(csv_data, delimiter=",")
    csv_header = next(csvreader)

    # loop through data
    for row in csvreader:    
      count += 1 # increase count for each iteration 
      date.append(row[0]) # append date data to the initialized var 
      profit.append(row[1]) #append profit
      total_profit +=  int(row[1]) #calculate profit

      #Calculate monthly and average profit shift.
      final_profit = int(row[1])
      monthly_profit_shift = final_profit - initial_profit

      #Commit monthly changes to list
      monthly_changes.append(monthly_profit_shift)

      profit_change = profit_change + monthly_profit_shift
      initial_profit = final_profit

      #Calculate the average change in profits
      average_change_profits = (profit_change/count)
      
      # max and min change and their observation dates
      max_increase_profit = max(monthly_changes)
      max_decrease_profit = min(monthly_changes)

      increase_date = date[monthly_changes.index(max_increase_profit)]
      decrease_date = date[monthly_changes.index(max_decrease_profit)]
      
   
    print(" \n\nFinancial Analysis")
    print("----------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(max_increase_profit) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(max_decrease_profit)+ ")")
    print("------------------------------------------------")

with open('analysis/financial_analysis.txt', 'w') as text:
    text.write("----------------------------\n")
    text.write("Financial Analysis"+ "\n")
    text.write("--------------------------------------------------\n")
    text.write("  Total Months: " + str(count) + "\n")
    text.write("  Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("  Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("  Greatest Increase in Profits: " + str(increase_date) + " ($" + str(max_increase_profit) + ")\n")
    text.write("  Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(max_decrease_profit) + ")\n")
    text.write("---------------------------------------------------\n")
