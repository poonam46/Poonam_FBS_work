def sumOfSeries(n):
    sum = 0

    for i in range(1,n+1):
        sum = sum + i

    return sum

n = int(input("Enter the value of n : "))

res = sumOfSeries(n)

print(f"Sum of Series upto {n} is {res}")