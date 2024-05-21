class Discount:
    def discount(self, amount):
        return amount  


class RegularDiscount(Discount):
    def discount(self, amount):
        return amount  


class SilverDiscount(Discount):
    def discount(self, amount):
        return amount * 0.9  


class GoldDiscount(Discount):
    def discount(self, amount):
        return amount * 0.8  


class Client:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def get_total_price(self, order):
        total_amount = sum(order.values())
        return self.discount.discount(total_amount)


def main():
    order1 = {"burger": 50, "fries": 30, "drink": 20}
    order2 = {"pizza": 80, "salad": 40}
    order3 = {"pasta": 70, "soup": 30}

    client1 = Client("Alice", RegularDiscount())
    client2 = Client("Bob", SilverDiscount())
    client3 = Client("Charlie", GoldDiscount())

    print(f"{client1.name}'s total price: {client1.get_total_price(order1):.2f}")
    print(f"{client2.name}'s total price: {client2.get_total_price(order2):.2f}")
    print(f"{client3.name}'s total price: {client3.get_total_price(order3):.2f}")


if __name__ == "__main__":
    main()
