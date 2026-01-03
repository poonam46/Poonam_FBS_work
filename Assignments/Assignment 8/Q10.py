def leapYear(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 :
        return "Leap Year"
    else:
        return "Not a Leap Year"
    

year = int(input("Enter the Year  to check Leap Year or not : "))

print(leapYear(year))