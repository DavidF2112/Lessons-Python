import random
import string

def generate_password(length, use_special_chars=False):
    if use_special_chars == "True":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password



password_length = int(input("Enter len>> "))
include_special_chars =input("Enter True or False>> ")
generated_password = generate_password(password_length, include_special_chars)
print("Згенерований пароль:", generated_password)
