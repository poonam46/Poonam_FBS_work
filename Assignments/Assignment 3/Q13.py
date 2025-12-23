units = int(input("Enter the total units of electricity : "))
unit = units

if(units <= 50):
    bill = units * 0.50
elif(units <= 150):
    amt1 = 50 * 0.50
    units = units - 50
    amt2 = units * 0.75
    bill = amt1 + amt2
elif(units <= 250):
    amt1 = 50 * 0.50
    amt2 = 100 * 0.75
    units = units - 150
    amt3 = units * 1.20
    bill = amt1 + amt2 + amt3
else:
    amt1 = 50 * 0.50
    amt2 = 100 * 0.75
    amt3 = 100 * 1.20
    units = units - 250
    amt4 = units * 1.50
    bill = amt1 + amt2 + amt3 + amt4

subcharge = bill * 0.20
total_bill = subcharge + bill

print(f"Electricity Bill Amount for {unit} units is Rs.{total_bill} ")
