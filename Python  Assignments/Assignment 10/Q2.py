li = [20,90,35,50,10,80,70]
max = li[0]
min = li[0]

for i in range(1,len(li)):
    if(li[i] > max):
        max = li[i]

    if(li[i] < min):
        min = li[i]

print("Maximum element from list = ",max)
print("Minimum element from list = ",min)

