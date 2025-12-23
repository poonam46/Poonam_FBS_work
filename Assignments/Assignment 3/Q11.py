# Person 1
age1 = int(input("Enter the age of Person 1 : "))
ticket1 = float(input("Enter the amount of ticket : "))

if(age1 < 12):
    ticket1 = ticket1 * 0.70
elif(age1 > 59):
    ticket1 = ticket1 * 0.50
else:
    ticket1 = ticket1

# Person 2
age2 = int(input("Enter the age of Person 2 : "))
ticket2 = float(input("Enter the amount of ticket : "))

if(age2 < 12):
    ticket2 = ticket2 * 0.70
elif(age2 > 59):
    ticket2 = ticket2 * 0.50
else:
    ticket2 = ticket2

# Person 3
age3 = int(input("Enter the age of Person 3 : "))
ticket3 = float(input("Enter the amount of ticket : "))

if(age3 < 12):
    ticket3 = ticket3 * 0.70
elif(age3 > 59):
    ticket3 = ticket3 * 0.50
else:
    ticket3 = ticket3

# Person 4
age4 = int(input("Enter the age of Person 4 : "))
ticket4 = float(input("Enter the amount of ticket : "))

if(age4 < 12):
    ticket4 = ticket4 * 0.70
elif(age4 > 59):
    ticket4 = ticket4 * 0.50
else:
    ticket4 = ticket4

# Person 5
age5 = int(input("Enter the age of Person 5 : "))
ticket5 = float(input("Enter the amount of ticket : "))

if(age5 < 12):
    ticket5 = ticket5 * 0.70
elif(age5 > 59):
    ticket5 = ticket5 * 0.50
else:
    ticket5 = ticket5

total_amt = ticket1 + ticket2 + ticket3 + ticket4 + ticket5
print(f"Total ticket amount to travel all 5 people : {total_amt}")