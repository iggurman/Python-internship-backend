class ATM:
    def __init__(self, pin):
        if len(str(pin)) != 4:
            raise ValueError("PIN must be exactly 4 digits")

        self.__pin = pin

    def verify_pin(self, pin):
        if self.__pin == pin:
            print("PIN Verified")
        else:
            print("Incorrect PIN")

    def change_pin(self, new_pin):
        if len(str(new_pin)) != 4:
            raise ValueError("PIN must be exactly 4 digits")

        self.__pin = new_pin


a = ATM(1234)

a.verify_pin(1234)
a.verify_pin(1111)

a.change_pin(5678)
a.verify_pin(5678)