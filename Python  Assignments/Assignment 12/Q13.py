str = input("Enter the string : ")

dcnt = 0
ccnt = 0

for ele in str:
    if(ele.isalpha()):
        ccnt += 1
    elif(ele.isdigit()):
        dcnt += 1

print(f"Total number of digits in {str} = {dcnt}")
print(f"Total number of letters in {str} = {ccnt}")