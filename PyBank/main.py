import os
import csv

# Setting the file paths
#infile from Resources folder
input_file = r"C:\Users\Mimy\OneDrive\Desktop\python-challenge\PyBank\Resources\budget_data.csv"
#outfile from analisis file
output_file = os.path.join("analysis", "budget_data_final.txt")

# Initializing variables
total_months = 0
total_PL = 0
average = 0
months = []
change_amounts = []
cleaned_data = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": float('inf')}
# Open the CSV file and process it
with open(input_file) as infile:
    reader = csv.reader(infile)
    
    # Read the header 
    header = next(reader)
    # Reading the second row from header
    first_row = next(reader)
    total_months +=1
    total_PL += int(first_row[1])
    previous_PL = int(first_row[1])
    
   
    # Process each row of data
    for row in reader:
        #counting the date rows
        total_months += 1
        #profit_losses = float(row[profit_losses_index])
        current_amount = int(row[1])
        #calculating the total amount
        total_PL += current_amount
        #calculating the cnanging amount
        change_amount = current_amount - previous_PL
        # changing the value
        previous_PL = current_amount
        # adding to the rows
        months.append(row[0])
        change_amounts.append(change_amount)
           #Calculating the greatest increase amount       
        if change_amount > greatest_increase["amount"]:

            greatest_increase["date"] = row[0]
            greatest_increase["amount"] = change_amount 
        #Calculating the greatest descrease amount
        if change_amount < greatest_decrease["amount"]:

            greatest_decrease["date"] = row[0]
            greatest_decrease["amount"] = change_amount 
        previous_PL = current_amount
      
    #Conditioning so that the system can keep going in case no rows to count
    if len(change_amounts) > 0: 
     #calculateing the average change
     average_change = sum(change_amounts)/len (change_amounts)
    else:
        average_change = "N/A"

# Writing the result to a CSV file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    
    # Writting the results
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total Profit/Losses: ${total_PL}"])
    writer.writerow([f"Average Change: ${average_change:.2f}"])
    writer.writerow([f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']:.2f})"])
    writer.writerow([f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']:.2f})"])
   
   
  #guiding from the terminal 
print(f"Data analysis complete. Output written to {output_file}")