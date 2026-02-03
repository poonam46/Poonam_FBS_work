def bubbleSort(li):
    size = len(li)

    for i in range(1,size):
        for j in range(0,size - i):
            if(li[j] > li[j + 1]):
                li[j] , li[j + 1] = li[j+1] , li[j]


li = [50,10,60,40,20,100,90]

print("List before sorting  : ",li)

bubbleSort(li)

print("List after sorting : ",li)

print("Second largest element is : ",li[-2])