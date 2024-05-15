class Product:
    def __init__(self, title, cost):
        self.title = title
        self.cost = cost

    def __str__(self):
        return f"{self.title}: {self.cost}"


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total_price(self):
        total_price = sum(product.cost for product in self.products)
        return total_price

    def __str__(self):
        products_str = '\n'.join(map(str, self.products))
        total_price = self.calculate_total_price()
        return f"Cart:\n{products_str}\nTotal Price: {total_price}"


def main():
    product_1 = Product('Tomat', 10)
    product_2 = Product('Cucumber', 23)
    product_3 = Product('Limon', 12)
    product_4 = Product('Apple', 5)

    cart_1 = Cart()
    cart_1.add_product(product_1)
    cart_1.add_product(product_2)
    cart_1.add_product(product_3)
    cart_1.add_product(product_4)
    print(cart_1)


main()
