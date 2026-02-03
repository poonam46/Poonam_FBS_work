def selectionSort(li):
    size = len(li)

    for i in range(0, size):
        min = i

        for j in range(i + 1, size):
            if(li[j][1] < li[min][1]):
                min = j

        li[i], li[min] = li[min], li[i]


li = [[10,4],[2,1],[13,20],[20,3],[25,30]]

print("List before sorting : ",li)

selectionSort(li)

print("List after sorting : ", li)

