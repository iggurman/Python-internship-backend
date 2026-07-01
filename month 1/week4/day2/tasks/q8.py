class Laptop:
    def __init__(self, volume):
        if volume < 0 or volume > 100:
            raise ValueError("Volume should be between 0 and 100")

        self.__volume = volume

    def increase_volume(self, amount):
        if self.__volume + amount > 100:
            raise ValueError("Volume cannot exceed 100")

        self.__volume += amount

    def decrease_volume(self, amount):
        if self.__volume - amount < 0:
            raise ValueError("Volume cannot go below 0")

        self.__volume -= amount

    def get_volume(self):
        return self.__volume


# Example
l = Laptop(50)

print(l.get_volume())

l.increase_volume(20)
print(l.get_volume())

l.decrease_volume(30)
print(l.get_volume())