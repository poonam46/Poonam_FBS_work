set1 = {10,20,30,40,50,60}
set2 = {40,50,60,70,80,90}

missing_set1 = set2.difference(set1)
missing_set2 = set1.difference(set2)

print("Set 1 : ", set1)
print("Set 2 : ", set2)

print("Missing elements in Set 1 : ",missing_set1)
print("Missing elements in Set 2 : ",missing_set2)