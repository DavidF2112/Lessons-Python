def log_arguments_results(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции log_arguments_resukt с аргументами: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} вернула: {result}")
        
        return result
    return wrapper

@log_arguments_results
def add_numbers(a, b):
    return a + b
add_numbers(3, 4)
