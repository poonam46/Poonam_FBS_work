
n = int(input("How Many elements want in the list : "))

li = []  
even = []
odd = []

for i in range(0,n):
    num = int(input("Enter the list elements : "))
    li.append(num)

print("Original List : ",li)

for ele in li:
    if ele % 2 == 0:
        even.append(ele)

    else:
        odd.append(ele)

print("List of Even numbers : ", even)

print("List of Odd Numbers : ",odd)


# n = int(input("How Many elements want in the list : "))

# li = [0] * n 
# for i in range(0,n):
#     num = int(input("Enter the list elements : "))
#     li[i] = num

# print("Original List : ",li)

# even = list(filter(lambda x : x % 2 == 0,li))
# print("List of Even list : ", even)

# odd = list(filter(lambda x : x % 2 != 0,li))
# print("List of Odd Numbers : ",odd)