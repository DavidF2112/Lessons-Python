text = input("Enter some text:: ").lower()

text = text.split()

text_set = set(text)

if len(text) != len(text_set):
    print("there are duplicates in this list")
else:
    print("there are no duplicates in this list")
