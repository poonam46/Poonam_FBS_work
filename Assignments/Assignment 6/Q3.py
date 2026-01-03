for i in range(1,5):
    for j in range(1,5-i):
        print(" ", end = " ")

    for j in range(1,i+1):
        if j == 2 or j == 4 :
            print(" ", end = " ")
        elif(i == 3 and j == 3):
            print(2 , end = " ")
        else:
            print(j , end = " ")

    for j in range(i - 1 , 0 , -1):
        if j == 2 :
            print(" ", end = " ")
        else:
            print(j , end = " ")
    
    for j in range(1,5-i):
        print(" " , end = " ")
    
    print()