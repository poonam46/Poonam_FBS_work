def sumOfPrime(n):
    sum = 0

    for i in range(2, n+1):
        
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                break
        else:
            sum = sum + i

    return sum

n = int(input("Enter the value of n : "))

res = sumOfPrime(n)

print(f"Sum of Prime Numbers between 1 to {n} is {res}")