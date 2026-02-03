li = [20,90,40,80,20,100,30,80,60,35,80]
num = int(input("Enter the number to be serach : "))
count = 0

for i in range(0,len(li)):
    if(num == li[i]):
        count += 1
    
if(count > 0):
    print(f"{num} is present in the list {count} times. ")
else:
    print(f"{num} is not present in the list. ")

