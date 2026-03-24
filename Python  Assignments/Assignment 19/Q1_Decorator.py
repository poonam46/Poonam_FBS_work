def memoize(fun):
    cache = {}

    def wrapper(n):
        if n in cache:
            print("Using cached result for " , n)
            return cache[n]
        
        result = fun(n)
        cache[n] = result
        return result

    return wrapper


@memoize
def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n*factorial(n-1)


print(factorial(5))
print(factorial(5))