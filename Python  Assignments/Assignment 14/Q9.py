numbers = [2,4,6,8,3,7,5,9,1]

target = int(input("Enter the value to check sum : "))

res = set()

for i in range(0,len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if(numbers[i] + numbers[j] + numbers[k] == target):
                triplet = tuple(sorted((numbers[i],numbers[j],numbers[k])))

                res.add(triplet)

print("Unique combinations of 3 numbers : ")
for t in res:
    print(t)