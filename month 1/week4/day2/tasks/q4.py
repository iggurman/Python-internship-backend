class Product:
    def __init__(self, name, price):
        self.__name = name

        if price <= 0:
            raise ValueError("Price should be greater than 0")

        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price <= 0:
            raise ValueError("Price should be greater than 0")

        self.__price = price


p1 = Product("Laptop", 50000)

print("Price:", p1.get_price())

p1.set_price(55000)
print("Updated Price:", p1.get_price())

p1.set_price(-100)   
p2 = Product("Phone", 0)   