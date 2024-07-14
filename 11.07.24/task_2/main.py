from order import Order,Dish,user_discount,total_with_discount



if __name__ == "__main__":
    try:
        dish1 = Dish("Borscht", 50)
        dish2 = Dish("Salad", 30)
        order = Order()
        order.add_item(dish1, 2)
        order.add_item(dish2)
        order.print_order()
    except Exception as e:
        print(e)
    else:
        print(order)

        discount = user_discount()
        print(f"Total with discount: {total_with_discount(order, discount)} UAH")

        print("\nOrder items:")
        for item in order:
            print(item)

        print("\nAccessing order items by index:")
        try:
            print(order[0])
            print(order[1])
        except IndexError as e:
            print(e)
