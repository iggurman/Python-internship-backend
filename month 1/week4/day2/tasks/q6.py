class Mobile:
    def __init__(self, battery_percentage):
        if battery_percentage < 0 or battery_percentage > 100:
            raise ValueError("Battery should be between 0 and 100")

        self.__battery_percentage = battery_percentage

    def charge(self, amount):
        if amount + self.__battery_percentage > 100:
            raise ValueError("Battery cannot exceed 100")

        self.__battery_percentage += amount

    def use_phone(self, amount):
        if self.__battery_percentage - amount < 0:
            raise ValueError("Battery cannot go below 0")

        self.__battery_percentage -= amount

    def get_battery(self):
        return self.__battery_percentage


m = Mobile(80)

print(m.get_battery())

m.charge(10)
print(m.get_battery())

m.use_phone(30)
print(m.get_battery())