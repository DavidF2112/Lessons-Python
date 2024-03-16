text = input("Enter some list>> ").lower()

text = text.split()
text = set(text)

print(len(text))