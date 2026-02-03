li = [10,20,30,40,50,60]

dup = []

for ele in li:
    dup.append(ele)

print("Original List : ",li)

print("Duplicate List : " ,dup)

print("ID of original list : " ,id(li))

print("ID of duplicate list : ",id(dup))




# for i in range(0,len(li)):
#     dup = dup + [li[i]]

# dup = list(map(lambda x : x , li))
