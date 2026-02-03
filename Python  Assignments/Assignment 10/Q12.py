numbers = [1,2,3,4,5,6,7,8,9,10]

square = []
cube = []

for ele in numbers:
    square.append(ele ** 2)
    cube.append(ele ** 3)

print("Original List : ",numbers)
print("List of Squares : ", square)
print("List of Cubes : ",cube)