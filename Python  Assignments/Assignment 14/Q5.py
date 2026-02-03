strings = ["interview","internet","internal","interval"]

prefix = " "

for i in range(len(min(strings,key=len))):
    s = set()
    for word in strings:
        s.add(word[i])

    if len(s) == 1:
        prefix += s.pop()
    else:
        break

print("Longest Common Prefix : ",prefix)