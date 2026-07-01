class FlightBooking:
    def __init__(self, seats):
        self.__available_seats = seats

    def book_seat(self):
        if self.__available_seats > 0:
            self.__available_seats -= 1
        else:
            print("No seats available")

    def cancel_booking(self):
        self.__available_seats += 1

    def get_available_seats(self):
        return self.__available_seats


f = FlightBooking(10)

print(f.get_available_seats())

f.book_seat()
print(f.get_available_seats())

f.cancel_booking()
print(f.get_available_seats())