class Product:
    def __init__(self, price, discount):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if discount < 0 or discount > 70:
            raise ValueError("Discount must be between 0 and 70")

        self.__price = price
        self.__discount = discount

    def __calculate_final_price(self):
        return self.__price - (self.__price * self.__discount / 100)

    def get_final_price(self):
        return self.__calculate_final_price()


p = Product(1000, 20)

print("Final Price:", p.get_final_price())