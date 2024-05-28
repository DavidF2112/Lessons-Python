class Dish:
    def __init__(self, name, price):
        if price <= 0:
            raise Exception(f"Invalid price: {price}. Price must be greater than 0.")
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} UAH"


class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, dish: Dish, quantity: int = 1):
        self.items[dish] = self.items.get(dish, 0) + quantity

    def total(self):
        return sum(dish.price * quantity for dish, quantity in self.items.items())

    def __str__(self):
        return "\n".join(f"{dish} x {quantity} = {dish.price * quantity} UAH" for dish, quantity in self.items.items())


class Discount:
    def discount(self):
        return 0

    def validate_discount(self, value):
        if not (0 <= value <= 1):
            raise Exception(f"Invalid discount: {value}. Discount must be between 0 and 1.")
        return value


class DiscountSilver(Discount):
    def discount(self):
        return self.validate_discount(0.1)


class DiscountGold(Discount):
    def discount(self):
        return self.validate_discount(0.2)


class DiscountPlatinum(Discount):
    def discount(self):
        return self.validate_discount(0.3)


def total_with_discount(order, discount):
    return order.total() * (1 - discount.discount())


def user_discount():
    answer = input("Do you have a discount card? (yes/no): ")

    if answer == "yes":
        answer = input("What type of discount card do you have? (silver/gold/platinum): ")
        if answer == "silver":
            return DiscountSilver()
        if answer == "gold":
            return DiscountGold()
        if answer == "platinum":
            return DiscountPlatinum()
    return Discount()


if __name__ == "__main__":
    try:
        dish1 = Dish("Borscht", 50)
        dish2 = Dish("Salad", 30)
        order = Order()
        order.add_item(dish1, 2)
        order.add_item(dish2)
        print(order)
        discount = user_discount()
        print(f"Total with discount: {total_with_discount(order, discount)} UAH")
    except Exception as e:
        print(e)

