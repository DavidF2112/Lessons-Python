valut = {
"grivna":36,
"zloty":4
}
money = input("Which valut:: grivna/zloty >> ").lower()
how_many = int(input("Enter money:: "))

if money == "grivna":
    print("Dollars: " , how_many // valut["grivna"])
elif money == "zloty":
    print("Dollars: " ,how_many // valut["zloty"])
else:
    print("We don't have this valut!")