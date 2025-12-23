n = int(input('Enter the value of n: '))

a=0
b=1
count = 1

print('Fibonacci series: ')
while(count <= n):
    print(a,end=" ")
    c = a + b
    a = b
    b = c
    
    count += 1
    