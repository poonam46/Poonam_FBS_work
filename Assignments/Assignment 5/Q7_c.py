n = int(input("Enter the number of terms : "))

sum = 0
term = 1

for i in range(1,n+1):
    sum += term
    term *= 2

print(f"Sum of the geometric series  from 1 to {n}  = {sum}")
