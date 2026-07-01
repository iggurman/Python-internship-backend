class MovieTicket():
    def __init__(self,seat,price):
        if 100>seat>0:
            self.__seat_number=seat
        self.__price=price
    
    def set_price(self,price):
        self.__price=price
        return self.__price
            
    def book_ticket(self,seat,amount):
        print("price is ",self.__price)
        self.__seat_number=seat
        if amount<self.__price:
            print("insufficient funds!")
        else:
            print("tickets bought!")
            return "amount returned ",amount-self.__price

    def cancel_ticket(self):
        self.__seat_number = None
        print("Ticket Cancelled")
        
    def get_ticket_details(self):
        return self.__seat_number," ",self.__price
    
x=MovieTicket(55,1050)
print(x.set_price(1000))
print(x.book_ticket(56,1500))