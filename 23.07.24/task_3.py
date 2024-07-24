def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            return None
    return wrapper

@handle_exceptions
def divide(a, b):
    return a / b

result = divide(5, 0)
print(f"Result: {result}")
