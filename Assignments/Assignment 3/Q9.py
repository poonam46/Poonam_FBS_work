m1 = int(input("Enter the first subject marks out of 100 : "))
m2 = int(input("Enter the second subject marks out of 100 : "))
m3 = int(input("Enter the third subject marks out of 100 : "))
m4 = int(input("Enter the fourth subject marks out of 100 : "))
m5 = int(input("Enter the fifth subject marks out of 100 : "))

total = m1 + m2 + m3 + m4 + m5
perc = (total / 500) * 100

if(perc >= 75):
    print("First Class")
elif(perc >= 60):
    print("Second Class")
elif(perc >= 50):
    print("Third Class")
elif(perc >= 35):
    print("Pass")
else:
    print("Fail")