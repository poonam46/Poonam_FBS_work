str = input("Enter the string : ")

dict = {w : len(w) for w in str.split() }
print(dict)