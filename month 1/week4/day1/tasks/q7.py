class Product:
    def __init__(self, product_id, product_name, category,
                brand, price, stock, rating, warranty):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.brand = brand
        self.price = price
        self.stock = stock
        self.rating = rating
        self.warranty = warranty

    def buy(self):
        if self.stock > 0:
            self.stock -= 1
            return f"{self.product_name} purchased successfully."
        else:
            return "Product is out of stock."

    def add_to_cart(self):
        return f"{self.product_name} added to cart."

    def update_stock(self, quantity):
        self.stock += quantity
        return self.stock

    def show_details(self):
        return (
            f"Product ID   : {self.product_id}\n"
            f"Product Name : {self.product_name}\n"
            f"Category     : {self.category}\n"
            f"Brand        : {self.brand}\n"
            f"Price        : ₹{self.price}\n"
            f"Stock        : {self.stock}\n"
            f"Rating       : {self.rating}\n"
            f"Warranty     : {self.warranty}"
        )

    def apply_discount(self, discount):
        self.price -= discount
        return self.price


p1 = Product(101, "Laptop", "Electronics",
            "Dell", 65000, 10, 4.5, "2 Years")

p2 = Product(102, "Smartphone", "Electronics",
            "Samsung", 45000, 20, 4.6, "1 Year")

p3 = Product(103, "Headphones", "Accessories",
            "Sony", 5000, 15, 4.4, "6 Months")

p4 = Product(104, "Smart Watch", "Wearables",
            "Apple", 35000, 8, 4.8, "1 Year")

p5 = Product(105, "Keyboard", "Computer Accessories",
            "Logitech", 2500, 30, 4.3, "1 Year")


print(p1.buy())
print(p2.add_to_cart())
print("Updated Stock:", p3.update_stock(10))
print("Price after Discount:", p4.apply_discount(5000))
print()
print(p5.show_details())