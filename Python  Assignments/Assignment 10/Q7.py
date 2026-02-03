li = [1,2,3,4,5,6,7,8,9,10]
cube = []

for ele in li:
    cube.append(ele ** 3)

print("Original List : ",li)
print("List of cubes : ", cube)



# for i in range(0,len(li)):
#         ele = li[i]
#         cube = cube + [ele ** 3]

# cube = list(map(lambda x : x ** 3 , li))