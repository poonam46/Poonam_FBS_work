def fibonacci(a,b,limit):
    for i in range(limit):
        c = a + b
        yield c
        a , b = b, c


limit = int(input("Enter the limit : "))
res = fibonacci(-1,1,limit)

for i in range(1, 10):
    print(next(res), end = " ")
# for num in res:
#     print(num, end = " ")