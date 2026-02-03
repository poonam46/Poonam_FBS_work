str = input("Enter the String : ")

cnt = 0

for ele in str:
    if(ele.islower()):
        cnt += 1

print(f"Total Lowercase character in {str} = {cnt}")