def sequence_generator(initial_value, n, user_function):
    current_value = initial_value
    count = 0
    while count < n:
        yield current_value
        current_value = user_function(current_value)
        count += 1


def user_function_arithmetic(x):
    return x + 2


gen = sequence_generator(1, 5, user_function_arithmetic)
for value in gen:
    print(value)
