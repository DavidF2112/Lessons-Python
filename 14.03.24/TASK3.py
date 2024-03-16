some_dict = {
}
while True:
    element = input("Enter some element>> ").strip().lower()
    key = input("Enter key for element>> ").strip().lower()

    if key in some_dict or element in some_dict:
        print("This element or key alredy in dict!")
    else:
        some_dict[key] = element
        print(some_dict)
        answer = input("countine  yes/no >> ").strip().lower()
        if answer == "no":
            break