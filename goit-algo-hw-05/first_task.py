def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result
            return result

    return fibonacci

# Приклад використання
fib = caching_fibonacci()
print(fib(5))  
print(fib(10))  
