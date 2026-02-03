li1 = [10,20,30,40,50,60]
li2 = [40,50,60,70,80,90,100]

union_list = []

for ele in li1:
    if ele not in union_list:
        union_list.append(ele)

for ele in li2:
    if ele not in union_list:
        union_list.append(ele)

print("Union of two lists : ",union_list)