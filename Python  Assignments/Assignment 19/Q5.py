str = input("Enter the string : ")

res = [word for word in str.split() if len(word) < 5]
print(res)