In the PyBank challenge, the requirement was to find, the total number of months included in the dataset, the net total amount of "Profit/Losses" over the entire period, the changes in "Profit/Losses" during the whole period; and then the average of those changes, the greatest increase in profits (date and amount) over the entire period as well as the greatest decrease in profits (date and amount) over the entire period.

I started by finding the budget_data.cvs file location under the resources folder and also creating the budget_data.txt under the analysis folder where the result will be received.
I managed to open and read the file and also create different variables such as:
total_months for the total number of months 
Total_PL for the net total amount of Profit/Losses

In the for loop, I managed to count the date row and also created the different variable inside of the loop such as:
- current_amount for calculating the total amount
- change_amount for calculating the changing amount
- previous_PL for passing the new current amount
- change_amount for Appending the change amount to the list

I applied the conditions for calculating the greatest increase/decrease amounts _ please check the values for the greatest_increase and greatest_decrease.
I also applied the condition in case no row or the value is zero when I was calculating the average of those changes _ please find the average_change variable in the code.

After opening the output file (budget_data_final.txt), the system managed to display the results by writing the results in the budget_data_final.txt.

For more information, please check the comments in the code.





