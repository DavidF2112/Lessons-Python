import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs) 
        end_time = time.time()  
        elapsed_time = end_time - start_time  
        print(f"Функция mesuare_time заняла {elapsed_time:.4f} секунд")
        return result
    return wrapper

@measure_time
def some_function():
    time.sleep(2)

some_function()
