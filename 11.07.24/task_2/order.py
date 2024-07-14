from exception import PriceError,QuantityError,logger
from discount import DiscountSilver,Discount,DiscountGold,DiscountPlatinum


class Dish:

    def __init__(self, name: str, price: int | float):
        if not isinstance(price, (int, float)):
            raise TypeError("Price should be a number")

        if price <= 0:
            raise PriceError(price, "Price can't be negative")

        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} UAH"


class Order:

    def __init__(self):
        self.items = {}
        logger.info('Order created')

    def add_item(self, dish: Dish, quantity: int = 1):
        if not isinstance(dish, Dish):
            logger.error('Dish should be a Dish object')
            raise TypeError("Dish should be a Dish object")
        if not isinstance(quantity, int):
            logger.error('Quantity should be a number')
            raise TypeError("Quantity should be a number")
        if quantity <= 0:
            logger.error('Quantity can not be negative')
            raise QuantityError(quantity, "Quantity can't be negative")

        self.items[dish] = self.items.get(dish, 0) + quantity

    def print_order(self):
        try:
            with open('order.txt', 'w') as f:
                f.write(str(self))
        except Exception as e:
            logger.error('Problem with writing of your receipt. Please, try again later.')
            print('Problem with writing of your receipt. Please, try again later.')

    def total(self):
        return sum(dish.price * quantity for dish, quantity in self.items.items())

    def __str__(self):
        return "\n".join(f"{dish} x {quantity} = {dish.price * quantity} UAH" for dish, quantity in self.items.items())

    def __iter__(self):
        self._iter_items = iter(self.items.items())
        return self

    def __next__(self):
        return next(self._iter_items)

    def __getitem__(self, index):
        items_list = list(self.items.items())
        if index < 0 or index >= len(items_list):
            raise IndexError("Order index out of range")
        return items_list[index]



def total_with_discount(order: Order, discount: Discount):
    if not isinstance(order, Order):
        raise TypeError("Order should be an Order object")
    if not isinstance(discount, Discount):
        raise TypeError("Discount should be a Discount object")
    logger.info('Price of order: %s; discount: %s; total price: %s',
                order.total(),
                discount.discount(),
                order.total() * (1 - discount.discount()))
    return order.total() * (1 - discount.discount())


def user_discount():
    answer = input("Do you have a discount card? (yes/no): ").strip().lower()

    if answer == "yes":
        answer = input("What type of discount card do you have? (silver/gold/platinum): ").strip().lower()
        if answer == "silver":
            return DiscountSilver()
        if answer == "gold":
            return DiscountGold()
        if answer == "platinum":
            return DiscountPlatinum()
    return Discount()