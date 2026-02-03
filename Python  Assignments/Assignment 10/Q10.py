li = [20,90,40,80,20,100,30,80,60,35,80]
print("List : ",li)

n = int(input("Enter the number from list to delete all occurences : "))

li2 = []

for ele in li:
    if ele != n :
        li2.append(ele)


li = li2
print("After removing element : ",li)