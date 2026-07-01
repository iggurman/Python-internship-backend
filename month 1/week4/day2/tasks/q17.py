class Hotel:
    def __init__(self, room):
        self.__room_status = room

    def book_room(self):
        if self.__room_status == "Available":
            self.__room_status = "Booked"
            print("Room Booked")
        else:
            print("Room Already Booked")

    def checkout(self):
        self.__room_status = "Available"
        print("Checkout Successful")

    def get_status(self):
        return self.__room_status


h = Hotel("Available")

print(h.get_status())

h.book_room()
print(h.get_status())

h.checkout()
print(h.get_status())