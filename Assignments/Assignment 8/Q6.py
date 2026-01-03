def  fabonacci(n,a,b):
  
    
    for i in range(1,n+1):
        c = a + b
        print(c , end=" ")

        a = b
        b = c

    


n = int(input("Enter the value of n : "))

fabonacci(n,1,0)