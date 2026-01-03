a = int(input("Enter value of a : "))
sum = 0


for i in range(1,11):
    sum += a ** i / i

print(f"Sum of Series = {sum:.2f}")

