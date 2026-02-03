li1 = [10,20,30,40,50,60]
li2 = [40,50,60,70,80,90,100]

inter_list = []

for ele in li1:
    if ele in li2 and ele not in inter_list:
        inter_list.append(ele)



print("Intersection of two lists : ",inter_list)