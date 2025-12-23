#Strong Number 145 = 1! + 4! + 5!

num = int(input('Enter a Number: '))
temp = num

sum = 0

while(temp > 0):
    digit = temp % 10
    
    fact = 1
    i = 1
    while(i <= digit):
        fact = fact * i
        i = i + 1
        
    sum = sum + fact
    
    temp = temp // 10
    
if(sum == num):
    print(f'{num} is a Strong Number.')
else:
    print(f'{num} is not a Strong Number.')