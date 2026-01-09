num = int(input('Enter a Number: '))

temp = num
sum = 0
cnt = 0

temp1 = num
while(temp1 > 0):
    digit = temp1 % 10
    cnt += 1
    temp1 = temp1 // 10
    
while(temp > 0):
    digit = temp % 10
    sum = sum + (digit ** cnt)
    temp = temp // 10
    
if(sum == num):
    print(f'{num} is a Armstrong Number.')
else:
    print(f'{num} is not a Armstrong Number.')