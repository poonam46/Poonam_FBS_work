dict = {1 : 10, 2 : 20, 3 : 30, 4 : 40 , 5 : 50}

mul = 1

for i in dict.values():
    mul *= i


print("Multiplication of all items : " ,mul)