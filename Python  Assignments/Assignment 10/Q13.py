li = [2,5,7,8,10,14,11,15,19,20]
li2 = []
print("Original List : ", li)

for ele in li:
    if ele % 2 != 0 :
        li2.append(ele)

li = li2

print("List after removing even elements : ",li)