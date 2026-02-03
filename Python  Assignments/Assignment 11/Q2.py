def bubbleSort(li1):
    size = len(li1)

    for i in range(1,size - 1):
        for j in range(0, size - i):
            if(li1[j] > li1[j + 1]):
                li1[j], li1[j + 1] = li1[j + 1] , li1[j]



li1 = [5,9,15,27,13]
li2 = [2,20,18,90,70,11]

for ele in li2:
    li1.append(ele)

print("After Merging two lists",li1)

print("\nBefore Sorting List : ", li1)

bubbleSort(li1)

print("\nAfter sorting list : ",li1)



