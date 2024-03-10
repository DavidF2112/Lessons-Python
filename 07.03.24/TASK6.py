word = input("Enter>>  ")

n = len(word)
found = False
for i in range(1, n//2 + 1):
    if n % i == 0:
        pattern = word[:i]
        if pattern * (n//i) == word:
            print("Repetitive word:", pattern)
            found = True
            break

if not found:
    print("Repetitive word not found!")
