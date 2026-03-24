def palindrome_numbers():
    num = 1
    
    while(True):
        rev = 0

        temp = num
        while(temp > 0):
            digit = temp % 10
            rev = rev * 10 + digit
            temp = temp // 10

        if num == rev:
            yield num

        num += 1

res = palindrome_numbers()
for num in res:
    print(num , end = " ")

