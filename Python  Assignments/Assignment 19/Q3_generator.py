def my_range(start, stop, step = 1):
    if step > 0:
        while start < stop:
            yield start
            start += step

    else:
        while start > stop:
            yield start
            start += step

res = my_range(1,20)

for i in res:
    print(i)