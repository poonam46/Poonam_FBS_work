s1 = int(input("Enter the first side of triangle : "))
s2 = int(input("Enter the second side of triangle : "))
s3 = int(input("Enter the third side of triangle : "))

if(s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1):
    print("Triangle is valid")

    if(s1 == s2 == s3):
        print("Triangle is equilateral triangle.")
    elif(s1 == s2 or s1 == s3 or s2 == s3):
        print("Triangle is isosceles triangle.")
    else:
        print("Triangle is scalene triangle.")
else:
    print("Triangle is not valid.")