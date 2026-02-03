num = 100

for row in range(10):
    if row % 2 == 0 :
        start = num

        for i in range(10):
            print(f"{start:3}", end = " ")
            start -= 1
    else:
        start = num - 9

        for i in range(10):
            print(f"{start:3}", end = " ")
            start += 1

    print()

    num -= 10