def fabonacciSeries(n,a = -1 ,b = 1):
    if n == 0:
        return 0
    else:
        c = a + b
        print(c, end = " ")
    
        fabonacciSeries(n-1, b,c)

n = int(input("enter the number : "))
fabonacciSeries(n)
