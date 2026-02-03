str1 = input("Enter the first string : ")
str2 = input("Enter the second string : ")

cnt1 = 0
cnt2 = 0

for ele in str1:
    cnt1 += 1

for ele in str2:
    cnt2 += 1

if(cnt1 > cnt2):
    print(f"{str1} is larger string than {str2}")
else:
    print(f"{str2} is larger string than {str1}")