words = ["eat","tea","tan","seat","ate","nat","bat","tent"]

anagrams = {}

for w in words:
    key = "".join(sorted(w))

    if key in anagrams:
        anagrams[key].append(w)
    else:
        anagrams[key] = [w]


print("Grouped Anagrams : ")
for ele in anagrams.values():
    print(ele)