for i in range(1,6):
    for j in range(1,6 - i):
        print(" ", end = " ")

    for j in range(1,i + 1):
        if j == 1:
            print("*", end = " ")
        else:
            print(" ", end = " ")

    for j in range(1,i):
        if j ==  i - 1:
            print("*" , end = " ")
        else:
            print(" ", end = " ")
    
    for j in range(1,6-i):
        print(" " , end = " ")

    print()
    #for lower part
for i in range(1,6):
    for j in range(1,i + 1):
        if j == i:
            print("*", end = " ")
        else:
            print(" ", end = " ")

    for j in range(i+1 , 6):
        print(" ", end = " ")

    for j in range(1,6-i):
        if j ==  5 - i:
            print("*" , end = " ")
        else:
            print(" ", end = " ")
    
    for j in range(1,i):
        print(" " , end = " ")

    print()