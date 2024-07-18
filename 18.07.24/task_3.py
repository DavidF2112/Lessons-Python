def apply_and_sum(numbers, user_function):
    transformed_numbers = [user_function(number) for number in numbers]
    return sum(transformed_numbers)

numbers = [1, 2, 3, 4, 5]

def user_function_square(x):
    return x ** 2

result = apply_and_sum(numbers, user_function_square)
print(f"Результат: {result}")
