a1 = int(input("Enter the first angle of triangle : "))
a2 = int(input("Enter the second angle of triangle : "))
a3 = int(input("Enter the third angle of triangle : "))

sum = a1 + a2 + a3

if(sum == 180):
    print("Triangle is valid")
else:
    print("Triangle is not valid.")
