#k = 1


for i in range(1,6):
   
    k = 65
    for j in range(1,6-i):
        print(" " , end = " ")

    for j in range(1,i):
        print(chr(k) , end = " ")
        k += 1

    for j in range(1,i+1):
        print(chr(k) , end = " ")
        k +=1
   
    for j in range(1,6-i):
        print(" ", end = " ")
    
    
    
    print()