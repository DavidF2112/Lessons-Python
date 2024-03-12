translations = {
    'hello':'привет',
    'goodbye':'пока',
    'cat':'кот',
    'dog':'собака',
}
word = input("Enter some word::   hello|goodbye|cat|dog  >> ").lower()
print("Перевод: ", translations[word])