from exception import PriceError,logger
from cart import Product,Cart



if __name__ == "__main__":
    try:
        x1 = Product("Bread", 10)
        x2 = Product("Milk", 20)
        x3 = Product("Butter", 30)
        x4 = Product("Cheese", 40)
        cart = Cart()
        logger.info("Cart created")
        cart.add_product(x1, 2)
        cart.add_product(x2, 3)
        cart.add_product(x3, 4)
        cart.add_product(x4, 5)
        print(cart)
        
        print("\nCart items:")
        for item in cart:
            print(item)
    except ValueError as e:
        print(e)
