str = input("Enter he string : ")

res = "".join([ch for ch in str if ch.lower() not in "aeiou"])
print(res)