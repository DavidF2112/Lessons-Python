def my_function(text):
    print(len(text))
    return text

text = input("Enter some text>> ").lower().strip().split()
print(my_function(text))