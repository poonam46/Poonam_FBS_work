x = int(input("Enter the value of x : "))
n = int(input("Enter the number of terms : "))

sum = 0
den = 1

for i in range(1,n+1):
    term = (x ** i) / den
    if i % 2 == 0:
        sum -= term
    else:
        sum += term

    den += 2
    
print(f"Sum of series = {sum}  ")