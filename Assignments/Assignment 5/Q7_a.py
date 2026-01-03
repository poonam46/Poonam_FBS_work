n = int(input("Enter value of n : "))
sum = 0
fact = 1

for i in range(1,n + 1):
    fact = fact * i
    sum += fact

print(f"Sum of factorial series upto {n} = {sum}")

