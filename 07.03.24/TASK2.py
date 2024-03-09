name = input("Enter name>> ")

contains_digit = False
for char in name:
    if char.isdigit():
        contains_digit = True
        break

first_letter_upper = name[0].isupper()

all_lower = all(char.islower() for char in name[1:])

if contains_digit:
    print("Your name have number!")
elif not first_letter_upper:
    print("In your doesn't have capital char!")
elif not all_lower:
    print("After capital char you doesn't lower case!")
else:
    print(f"Your name is perfect>> {name}")
