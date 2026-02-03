li = [10,15,14,13,9,20,30]
m = int(input("Enter the first number to divide the elements of list : "))
n = int(input("Enter the second number to divide the elements of list : "))

print(f"Elements which are divided by {m} and {n} : ")

for ele in li:
    if ele % m == 0 and ele % n == 0:
        print(ele, end= " ") 