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
