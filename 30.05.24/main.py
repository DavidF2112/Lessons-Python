import discounts_module
import order_module

def total_with_discount(order: order_module.Order, discount: discounts_module.Discount):
    """
    Calculate total price with discount
    :param order: Order
    :param discount: Discount Type
    :return: Value with discount
    """
    if not isinstance(order, order_module.Order):
        raise TypeError("Order should be an Order object")
    if not isinstance(discount, discounts_module.Discount):
        raise TypeError("Discount should be a Discount object")
    order_module.logger.info('Price of order: %s; discount: %s; total prise: %s',
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
            return discounts_module.DiscountSilver()
        if answer == "gold":
            return discounts_module.DiscountGold()
        if answer == "platinum":
            return discounts_module.DiscountPlatinum()
    return discounts_module.Discount()


if __name__ == "__main__":
    try:
        dish1 = order_module.Dish("Borscht", 50)
        dish2 = order_module.Dish("Salad", 30)
        order = order_module.Order()
        order.add_item(dish1, '2')
        order.add_item(dish2)
        order.print_order()
    except Exception as e:
        print(e)
    else:
        print(order)

        discount = user_discount()
        print(f"Total with discount: {total_with_discount(order, discount)} UAH")
