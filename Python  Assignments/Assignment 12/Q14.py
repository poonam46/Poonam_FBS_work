str = input("Enter the string : ")

cnt = 0

dict = {}

str1 = str.split(" ")

for ele in str1:
    if ele in dict:
        dict[ele] = dict[ele] + 1
    else:
        dict[ele] = 1

print(dict)
