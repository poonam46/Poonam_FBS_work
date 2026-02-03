str = "poonam"

str1 = " "

for i in range(0,len(str)):
    if i % 2 == 0:
        str1 = str1 + str[i]

print(f"Before removing odd index character : {str}")

str = str1

print(f"After removing odd index character : {str}")
