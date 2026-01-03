start= int(input("Enter the starting range of to print Armstrong Number : "))
stop = int(input("Enter the ending range of to print Armstrong Number : "))

print(f"The Armstrong numbers between {start} to {stop} are : ")

for i in range(start,stop+1):
    temp = i
    temp1 = i
    cnt = 0
    sum = 0 

    while(temp > 0):
        digit = temp % 10
        cnt += 1
        temp = temp // 10

    while(temp1 > 0 ):
        d = temp1 % 10
        sum += d ** cnt
        temp1 = temp1 // 10

    if sum == i:
        print(i)
     


