def checkPrime(num,i=2):
    if num <= 1:
        return False
    
    if num == i:
        return True
    
    if num % i == 0:
        return False
    
    return checkPrime(num,i+1)

num = int(input("Enter teh Number : "))

res = checkPrime(num)

if res:
    print(f"{num} is Prime")
else:
    print(f"{num} is not Prime")