num = int('Enter a Number: ')
sum = 0
i = 1

while(i < num):
    if(i % num == 0):
        sum += i
    i += 1
    
if(sum == num):
    print(f'{num} is a Perfect Number.')
else:
    print(f'{num} is not a Perfect Number.')
    