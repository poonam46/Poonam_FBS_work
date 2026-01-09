num = int(input('Enter 3 Digit Number: '))

d1 = num % 10
#print('d1: ',d1)
num = num // 10
#print(num)

d2 = num % 10
#print('d2: ',d2)
num = num // 10
#print(num)

d3 = num % 10
#print('d3: ',d3)
num = num // 10
#print(num)

sum = d1 + d2 + d3
print(f"Sum of 3 Digit Number is {sum}.")