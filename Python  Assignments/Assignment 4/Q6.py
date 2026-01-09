num = int(input('Enter a Number: '))

i=1
count=0

while i <= num:
    if(num % i == 0):
        count += 1
    i += 1
    
if(count == 2):
    print(f'{num} is a Prime Number.')
else:
    print(f'{num} is not a Prime Number.')
    