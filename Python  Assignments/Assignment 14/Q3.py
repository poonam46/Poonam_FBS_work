strList = ["Python is easy","Learning Python is fun","Python is simple"]

words = []

for line in strList:
    words.extend(line.lower().split())

unique_words = set(words)

print("Unique words and their frequencies : \n")

for word in unique_words:
    count = 0
    for w in words:
        if w == word:
            count += 1

    print(f"{word} = {count}")