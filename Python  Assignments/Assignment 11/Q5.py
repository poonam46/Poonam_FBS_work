def selectionSort(li):
    size = len(li)

    for i in range(0, size):
        min = i
        for j in range(i + 1, size):
            if(len(li[j]) < len(li[min])):
                min = j
        
        li[i] , li[min] = li[min] , li[i]


li = ["apple","fig","banana","grapes","kiwi"]

print("List before sorting : ", li)

selectionSort(li)

print("List after sorting : ", li)