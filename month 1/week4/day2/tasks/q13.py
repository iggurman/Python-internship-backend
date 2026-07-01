class ShoppingCart:
    def __init__(self, total):
        self.__total_amount = total

    def add_item(self, amount):
        self.__total_amount += amount

    def remove_item(self, amount):
        if amount <= self.__total_amount:
            self.__total_amount -= amount
        else:
            print("Insufficient Amount")

    def get_total(self):
        return self.__total_amount


c = ShoppingCart(1000)

print(c.get_total())

c.add_item(500)
print(c.get_total())

c.remove_item(300)
print(c.get_total())