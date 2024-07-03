import logging

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('log.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


class PriceError(Exception):
    def __init__(self, price, message):
        self.message = message
        self.price = price
        super().__init__(self.message)

    def __str__(self):
        return f'Price {self.price} is invalid. {self.message}'


class QuantityError(Exception):
    def __init__(self, quantity, message):
        self.message = message
        self.quantity = quantity
        super().__init__(self.message)

    def __str__(self):
        return f'Quantity {self.quantity} is invalid. {self.message}'


class Dish:

    def __init__(self, name: str, price: int | float):
        if not isinstance(price, int | float):
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


class Discount:
    def discount(self):
        return 0


class DiscountSilver(Discount):
    def discount(self):
        return 0.1


class DiscountGold(Discount):
    def discount(self):
        return 0.2


class DiscountPlatinum(Discount):

    def discount(self):
        return 0.3


def total_with_discount(order: Order, discount: Discount):
    """
    Calculate total price with discount
    :param order: Order
    :param discount: Discount Type
    :return: Value with discount
    """
    if not isinstance(order, Order):
        raise TypeError("Order should be an Order object")
    if not isinstance(discount, Discount):
        raise TypeError("Discount should be a Discount object")
    logger.info('Price of order: %s; discount: %s; total prise: %s',
                order.total(),
                discount.discount(),
                order.total() * (1 - discount.discount()))
    return order.total() * (1 - discount.discount())


def user_discount():
    """
    Get discount from user
    :return: Discount object
    """
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


if __name__ == "__main__":
    try:
        dish1 = Dish("Borscht", 50)
        dish2 = Dish("Salad", 30)
        order = Order()
        order.add_item(dish1, '2')
        order.add_item(dish2)
        order.print_order()
    except Exception as e:
        print(e)
    else:
        print(order)

        discount = user_discount()
        print(f"Total with discount: {total_with_discount(order, discount)} UAH")