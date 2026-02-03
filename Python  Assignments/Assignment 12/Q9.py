str = "Hello everyone How are you"

wcnt = 0
cnt = 0

str1 = str.split(" ")

for ele in str1:
    # if ele == " ":
    wcnt += 1
    
for ele in str: 
    if ele != " ": 
        cnt += 1

print(f"Total characters in string {str} : {cnt}")
print(f"Total words in string {str} : {wcnt}")

