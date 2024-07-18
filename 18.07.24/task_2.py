import time

def memoize(fn):
    cache = {}
    def memoized_fn(x):
        if x not in cache:
            cache[x] = fn(x)
        return cache[x]
    return memoized_fn

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

@memoize
def fibonacci_memoized(n):
    if n <= 1:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)

n = 35

start_time = time.time()
result_recursive = fibonacci_recursive(n)
end_time = time.time()
time_recursive = end_time - start_time

print(f"Рекурсивный результат: {result_recursive}, время выполнения: {time_recursive:.5f} секунд")

start_time = time.time()
result_memoized = fibonacci_memoized(n)
end_time = time.time()
time_memoized = end_time - start_time

print(f"Мемоизированный результат: {result_memoized}, время выполнения: {time_memoized:.5f} секунд")
