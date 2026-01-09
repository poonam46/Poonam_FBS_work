num = int(input('Enter the Number: '))
fact = 1
for i in range(num,1,-1):
    fact = fact * i
print(f'Factorial of a number {num}! = {fact}')