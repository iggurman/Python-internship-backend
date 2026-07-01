class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @property
    def area(self):
        return self.__length * self.__width

    @property
    def perimeter(self):
        return 2 * (self.__length + self.__width)


x = Rectangle(2, 6)

print(x.area)
print(x.perimeter)