li = [1,2,3,4,5,6,7,8,9,10]

li2 = []

for ele in li:
    if ele % 2 != 0 :
        li2.append(ele)

print("Original list : ",li)
li = li2

print("List after removing even numbers : ", li)