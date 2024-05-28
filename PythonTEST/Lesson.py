class Discount:
    def discount(self, amount):
        return amount
    

class RegularRoom(Discount):
    def discount(self, amount):
        return amount
    

class BuissnesRoom(Discount):
    def discount(self , amount):
        return amount * 0.9
    

class PresidentRoom(Discount):
    def discount(self, amount):
        return amount * 0.8
    

class Client:
    def __init__(self ,name,discount):
        self.name = name
        self.discount = discount


    def get_total_price(self, order):
        total_amount = sum(order.values())
        return self.discount.discount(total_amount)
    

def main():
    order_1 = {"one_room": 2000 , "second_room": 3000}
    order_2 = {"one_room": 5000 , "second_room": 10000}
    order_3 = {"one_room": 3000 , "second_room": 6000}


    client_1 = Client("David" , RegularRoom)
    client_2 = Client("Denis" , BuissnesRoom)
    client_3 = Client("Anna" , PresidentRoom)


    print(f"{client_1}'s total price: {client_1.get_total_price(order_1): .2f}")        
    print(f"{client_2}'s total price: {client_2.get_total_price(order_2): .2f}")        
    print(f"{client_3}'s total price: {client_3.get_total_price(order_3): .2f}")        



if __name__ == '__main__':
    main()