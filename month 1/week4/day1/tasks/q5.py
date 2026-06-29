class Mobile:
    def __init__(self, brand, model, ram, storage, battery,
                camera, processor, price):
        self.brand = brand
        self.model = model
        self.ram = ram
        self.storage = storage
        self.battery = battery
        self.camera = camera
        self.processor = processor
        self.price = price

    def call(self, number):
        return f"Calling {number} from {self.brand} {self.model}."

    def send_message(self, number, message):
        return f"Message sent to {number}: {message}"

    def take_photo(self):
        return f"Photo captured using {self.camera} camera."

    def charge(self):
        return f"{self.brand} {self.model} is charging."

    def show_specification(self):
        return (
            f"Brand      : {self.brand}\n"
            f"Model      : {self.model}\n"
            f"RAM        : {self.ram}\n"
            f"Storage    : {self.storage}\n"
            f"Battery    : {self.battery}\n"
            f"Camera     : {self.camera}\n"
            f"Processor  : {self.processor}\n"
            f"Price      : ₹{self.price}"
        )


mob1 = Mobile("Samsung", "Galaxy S24", "8GB", "256GB",
            "5000mAh", "50MP", "Snapdragon 8 Gen 3", 75000)

mob2 = Mobile("Apple", "iPhone 15", "6GB", "128GB",
            "3349mAh", "48MP", "A16 Bionic", 80000)

mob3 = Mobile("OnePlus", "12R", "8GB", "256GB",
            "5500mAh", "50MP", "Snapdragon 8 Gen 2", 42000)

mob4 = Mobile("Xiaomi", "Redmi Note 13", "8GB", "128GB",
            "5000mAh", "108MP", "Dimensity 7200", 23000)

mob5 = Mobile("Realme", "GT Neo 5", "12GB", "256GB",
            "5000mAh", "64MP", "Snapdragon 8+ Gen 1", 35000)


print(mob1.call("9876543210"))
print(mob2.send_message("9876501234", "Hello!"))
print(mob3.take_photo())
print(mob4.charge())
print()
print(mob5.show_specification())