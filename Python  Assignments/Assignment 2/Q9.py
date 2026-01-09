x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

print(f'Before Swapping x is {x} , y is {y}.')

#y = x + y
#x = y - x 
#x = y - x

x, y = y, x
print(f'After Swapping x is {x}, y is {y}.')