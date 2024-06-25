class Product:
    def __init__(self , name , price):
        self.name = name 
        self.price = price


    def __str__(self):
        return f"Name of product - {self.name}\nPrice of product - {self.price}"


class Cart:
    def __init__(self):
        self.items = {}


    def add_product(self , product:Product, quantity: int = 1):
         self.items[product] = self.items.get(product , 0) + quantity


    def total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())  
    

    def __str__(self):
        return "\n".join(f"{product} x {quantity} = {product.price * quantity} UAH" for product, quantity , in self.items.items())
    

if __name__ == '__main__':
    product_1 = Product("Beef" , 150)
    product_2 = Product("Tomato" , 10)
    product_3 = Product("Apple" , 6)

    cart = Cart()

    cart.add_product(product_1 , 1)
    cart.add_product(product_2 , 10)
    cart.add_product(product_3 , 5)

    print(cart)
    

