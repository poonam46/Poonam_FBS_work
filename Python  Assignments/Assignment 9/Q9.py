def power(n,m):
    if m == 0:
        return 1
    else:
        return n * power(n,m - 1)
    
n = int(input("Enter the value of base  n : "))
m = int(input("Enter the value of power m : "))

res = power(n,m)
print(f"{m} to the power of {n} = {res}")
    