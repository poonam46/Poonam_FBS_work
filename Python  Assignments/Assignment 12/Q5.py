str = input("Enter the string : ")

count = 0

for ele in str:
    if(ele == 'a' or ele == 'A' or ele == 'e' or ele == 'E' or ele == 'i' or ele == 'I' or ele == 'o' or ele == 'O' or ele == 'u' or ele == 'U'):
        count +=1

print("Total number of vowels : ", count)