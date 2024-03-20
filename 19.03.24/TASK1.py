import random

def my_func(seacrh=-1):
    y = [random.randint(1,100) for _ in range(20)]
    for i in y:
        if i == seacrh:
            print(f"Your number in list: {y.index(i)}")
            print(seacrh)
            break
        return seacrh
      
search = int(input("Enter number:: ")) 

print(my_func(search))
print(my_func())