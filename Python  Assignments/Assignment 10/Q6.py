li = [20,90,40,80,20,100,30,80,60,35,80]
li2 = []

for ele in li:
    if ele not in li2:
        li2.append(ele)

li = li2
          
print(li)