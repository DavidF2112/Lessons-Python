while True:
    new_contact = input("Enter name of contact>> ")
    new_number = int(input("Enter number of contact>> "))
    contacs = {}
    contacs[new_number] = new_contact
    print(contacs)

    answer = input("Continue?  yes/no >> ").lower()
    
    if answer == "yes":
        delete = input("Do you want delet some contact:  yes/no  >> ")
        if delete == "yes":
            which = int(input("Enter number contact which you want delete>> "))
            del contacs[which]
            print(contacs)
    else:
        break

print(contacs)