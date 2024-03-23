import string

def lines(l):  
    if len(l) == 5:
        _, first_name, second_name, money, category = map(str.strip, l)
        categories(category, money)
        users(first_name, money)  
    elif len(l) == 4:
        _, first_name, money, category = map(str.strip, l)
        categories(category, money)
        users(first_name, money)
    elif len(l) == 3:
        _, first_name, money = map(str.strip, l)
        users(first_name, money)

category_totals = {
    "decorations": 0,
    "food": 0,
    "toys": 0,
    "drinks": 0,
    "accessories": 0,
    "instruments": 0,
    "clothes": 0
}

result_of_bob = 0
result_of_mary = 0
result_of_aleksa = 0
result_of_maria = 0
result_of_jack = 0

def categories(category, money):
    global category_totals
    for i in string.punctuation:
        money = money.replace(i, "")
        if i == "$":
            break
    money = float(money)
    category_totals[category] += money

def users(first_name, money):
    global result_of_bob, result_of_mary, result_of_aleksa, result_of_maria, result_of_jack
    for i in string.punctuation:
        money = money.replace(i, "")
        if i == "$":
            break
    money = float(money)
    if first_name == "Bob":
        result_of_bob += money
    elif first_name == "Mary":
        result_of_mary += money
    elif first_name == "Aleksa":
        result_of_aleksa += money
    elif first_name == "Maria":
        result_of_maria += money
    elif first_name == "Jack":
        result_of_jack += money

with open('hw_10_test.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.split()
        lines(line)

full_result = result_of_bob + result_of_aleksa + result_of_jack + result_of_maria + result_of_mary

print("Category Totals:")
for category, total in category_totals.items():
    print(f"{category.capitalize()}: ${total}")

print("\nIndividual Totals:")
print("Bob:", result_of_bob)
print("Mary:", result_of_mary)
print("Aleksa:", result_of_aleksa)
print("Maria:", result_of_maria)
print("Jack:", result_of_jack)
print("Full Result:", full_result)
