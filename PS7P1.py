#input phase
principal = float(input("Enter principle amount: "))
rate = float(input("Enter interest rate :"))

print ("Year Beginning Balance Ending Balance")

#process phase
total_interest = 0
for year in range(1,6):

  beginning_balance = principal 
interest = beginning_balance  * rate 
ending_balance = beginning_balance + interest
total_interest = total_interest + interest 

#output phase 
print(year, " $",
      format(beginning_balance, ",.2f"), 
       "$", format(ending_balance, ",.2f"))

principal = ending_balance

print("Total interest earned: $", format(total_interest, ",.2f"))
