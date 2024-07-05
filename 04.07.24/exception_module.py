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