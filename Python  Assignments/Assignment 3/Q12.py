num = int(input("Enter the three digit number : "))
temp = num

d1 = temp % 10
temp = temp //10

d2 = temp % 10 
temp = temp // 10

d3 = temp % 10
temp = temp // 10

rev = d1 * 100 + d2 * 10 + d3

if(num == rev):
    print(f"The three digit number {num} is palindrome.")
else:
    print(f"The three digit number {num} is not palindrome.")