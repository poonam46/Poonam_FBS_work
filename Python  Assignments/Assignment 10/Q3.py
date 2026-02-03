li = [20,90,40,80,100,30,60,35]
max = li[0]
smax = 0

for i in range(1,len(li)):
    if(li[i] > max):
        smax = max
        max = li[i]
    elif(li[i] > smax):
        smax = li[i]

print("Second Largest element from list =  ",smax)