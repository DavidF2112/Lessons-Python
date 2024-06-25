class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} UAH\nDescription: {self.description}"


class MenuCategory:
    def __init__(self, name):
        self.name = name
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def __str__(self):
        category_str = f"{self.name}:\n"
        for dish in self.dishes:
            category_str += str(dish) + "\n"
        return category_str


class RestaurantMenu:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def __str__(self):
        menu_str = ""
        for category in self.categories:
            menu_str += str(category) + "\n"
        return menu_str


def main():

    dish_1 = Dish("Caesar Salad", "Classic Caesar salad with chicken, romaine lettuce, croutons, and Caesar dressing", 120)
    dish_2 = Dish("Margherita Pizza", "Pizza with tomato sauce, mozzarella cheese, and fresh basil", 150)
    dish_3 = Dish("Tiramisu", "Classic Italian dessert made with coffee-soaked ladyfingers and mascarpone cream", 80)
    

    starters = MenuCategory("Starters")
    starters.add_dish(dish_1)

    main_courses = MenuCategory("Main Courses")
    main_courses.add_dish(dish_2)

    desserts = MenuCategory("Desserts")
    desserts.add_dish(dish_3)

    menu = RestaurantMenu()
    menu.add_category(starters)
    menu.add_category(main_courses)
    menu.add_category(desserts)

    print(menu)


if __name__ == "__main__":
    main()