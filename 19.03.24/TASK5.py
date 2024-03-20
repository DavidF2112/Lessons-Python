def next_number(sequence):
    numbers = [int(x) for x in sequence.split(',')]
    
    if len(numbers) == 2:  
        ratio = numbers[1] / numbers[0]
        return numbers[-1] * ratio

    diff = numbers[1] - numbers[0]
    if all(numbers[i] - numbers[i-1] == diff for i in range(2, len(numbers))):  
        return numbers[-1] + diff

    ratio = numbers[1] // numbers[0]
    if all(numbers[i] // numbers[i-1] == ratio for i in range(2, len(numbers))):  
        return numbers[-1] * ratio

 
    return None

sequence = input("Введіть послідовність чисел через кому: ")

next_num = next_number(sequence)
if next_num is not None:
    print("Наступний член послідовності:", next_num)
else:
    print("Неможливо продовжити послідовність зазначеним способом.")
