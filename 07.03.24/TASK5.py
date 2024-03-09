text = input("Enter text>>  ")

words = text.split() 

longest_word = max(words, key=len) 

print("LONGEST WORD:", longest_word)
