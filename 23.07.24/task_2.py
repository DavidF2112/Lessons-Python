def cache_result(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            key = f"{args}-{kwargs}"
            
            try:
                with open(filename, 'r') as file:
                    cache = file.readlines()
            except FileNotFoundError:
                cache = []
            
            for line in cache:
                saved_key, saved_result = line.split(':::')
                if saved_key == key:
                    print(f"Результат загружен из файла {filename}")
                    return eval(saved_result)
            
            result = func(*args, **kwargs)
            with open(filename, 'a') as file:
                file.write(f"{key}:::{result}\n")
            print(f"Результат сохранен в файл {filename}")
            return result
        return wrapper
    return decorator

@cache_result('result_cache.txt')
def expensive_computation(x, y):
    return x * y

result = expensive_computation(3, 4)
print(f"Результат: {result}")

result = expensive_computation(3, 4)
print(f"Результат: {result}")
