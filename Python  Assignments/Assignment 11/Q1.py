li = [1,2,3,4,5,6,7,8,9,10]

even = []
odd = []

for ele in li:
    if ele % 2 == 0:
        even.append(ele)
    else:
        odd.append(ele)

print("Original List : ",li)
print("Even numbers list : ", even)
print("Odd numbers list : ", odd)