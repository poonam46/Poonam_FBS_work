str = "Poonam"
str1 = ""

n = int(input("Enter the index to remove the character : "))


for i in range(0, len(str)):
    if(i != n):
        str1 = str1 + str[i]

str = str1
print(f"String After removing {n} th index : ", str)

