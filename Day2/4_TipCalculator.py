print("Welcome to tip calculator")
bill = float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give?"))
people = int(input("How many people will you split the bill with?"))


tipAsPercent = tip / 100
TotalTipAmount = bill * tipAsPercent
TotalBill = bill + TotalTipAmount
billPerPerson = TotalBill / people
final_amount = round(billPerPerson, 2)
print(f"Each person should pay {final_amount}")


