def limit_calls(max_calls):
    def decorator(func):
        func._call_count = 0  

        def wrapper(*args, **kwargs):
            if func._call_count < max_calls:
                func._call_count += 1
                return func(*args, **kwargs)
            else:
                print(f"Превышено количество вызовов функции some_function ({max_calls} раз)")

        return wrapper
    return decorator

@limit_calls(3)
def some_function():
    pass

some_function()
some_function()
some_function()
some_function()
