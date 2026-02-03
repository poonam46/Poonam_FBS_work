numbers = [2,4,6,8,3,7,5,9,1]

target = int(input("Enter the value to check sum : "))

set1 = set()

for num in numbers:
    diff = target - num
    if diff in set1:
        print(f"{num} , {diff}")
    set1.add(num)