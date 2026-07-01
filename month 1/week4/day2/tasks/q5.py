class Mobile():
    def __init__(self,battery_percentage):
        if 100<battery_percentage or battery_percentage<0:
            raise ValueError
        else:
            self.__battery=battery_percentage
            
    def charge(self,charge):
        if charge+self.__battery>100:
            raise ValueError
        else:
            self.__battery+=charge
            return self.__battery
    def use_phone(self,discharge):
        if discharge+self.__battery>100:
            raise ValueError
        else:
            self.__battery-=discharge
            return self.__battery
    def get_battery(self):
        return self.__battery
x=Mobile(89)
print(x.get_battery())
print(x.charge(1))