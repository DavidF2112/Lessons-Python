import logging
import exception_module

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

    def __iadd__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            dish, quantity = other
            self.add_item(dish, quantity)
        elif isinstance(other, Dish):
            self.add_item(other)
        else:
            logger.error('Invalid item type for addition')
            raise TypeError("Invalid item type for addition")
        return self
