def sumOfDigit(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sumOfDigit(num // 10)
    

num = int(input("Enter the Number : " ))
sum = sumOfDigit(num)
print(f"Sum of digits of {num} is = {sum}")

