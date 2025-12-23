n = int(input('Enter the value of range: '))
num = int(input('Enter a number: '))

print(f'All numbers in a range {n} divisible by a {num}.')
for i in range(1,n+1):
    if(i % num == 0):
        print(i)