def countOfDigits(num):
    count = 0
    while(num > 0 ):
        digit = num % 10
        count +=1
        num = num // 10

    return count

def armstrongNumberSum(num):
    temp = num
    sum = 0

    cnt = countOfDigits(num)

    while(temp > 0):
        digit = temp % 10
        sum = sum + (digit ** cnt)
        temp = temp // 10

    return sum 

def checkArmstrong(num):
    sum = armstrongNumberSum(num)

    if num == sum :
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number" 
    

num = int(input("Enter the Number : "))

print(checkArmstrong(num))





    