class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)
        print(item, "added to cart")

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
            print(item, "removed from cart")
        else:
            print("Item not found")

    def get_items(self):
        return self.__items.copy()


cart = ShoppingCart()

cart.add_item("Laptop")
cart.add_item("Mobile")
cart.add_item("Headphones")

print("Cart Items:", cart.get_items())

cart.remove_item("Mobile")

print("Updated Cart:", cart.get_items())