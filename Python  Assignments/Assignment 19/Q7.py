li = [ num for num in range(1,1001) for d in range(2,10) if num % d == 0]
li = set(li)
print(li)