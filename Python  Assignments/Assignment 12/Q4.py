str1 = input("Enter the string : ")

str2 = ""

size = len(str1)

str2 = str1[-1] + str1[1 : size - 1 ] + str1[0]

print(f"String after swapping : {str2}")
