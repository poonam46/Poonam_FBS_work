n = int(input('Enter the value of n: '))

print(f'Integers upto {n} that are divisible by 7 and multiple of 5: ')
for i in range(1, n+1):
    if((i % 7) == 0 and (i % 5) == 0):
        print(i)