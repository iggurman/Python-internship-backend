class FoodOrder:
    def __init__(self, order_id, customer_name, restaurant_name,
                food_item, quantity, price,delivery_address, payment_status):
        self.order_id = order_id
        self.customer_name = customer_name
        self.restaurant_name = restaurant_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price
        self.delivery_address = delivery_address
        self.payment_status = payment_status

    def place_order(self):
        return f"Order for {self.food_item} has been placed successfully."

    def cancel_order(self):
        return f"Order {self.order_id} has been cancelled."

    def track_order(self):
        return f"Order {self.order_id} is out for delivery."

    def make_payment(self):
        self.payment_status = "Paid"
        return f"Payment successful. Status: {self.payment_status}"

    def show_order(self):
        return (
            f"Order ID          : {self.order_id}\n"
            f"Customer Name     : {self.customer_name}\n"
            f"Restaurant Name   : {self.restaurant_name}\n"
            f"Food Item         : {self.food_item}\n"
            f"Quantity          : {self.quantity}\n"
            f"Price             : ₹{self.price}\n"
            f"Delivery Address  : {self.delivery_address}\n"
            f"Payment Status    : {self.payment_status}"
        )


order1 = FoodOrder(101, "Gurman", "Domino's",
                "Veg Pizza", 2, 600,
                "Indore", "Pending")

order2 = FoodOrder(102, "Avantika", "McDonald's",
                "Burger", 3, 450,
                "Bhopal", "Pending")

order3 = FoodOrder(103, "Ritik", "KFC",
                "Chicken Bucket", 1, 800,
                "Mumbai", "Paid")
order4 = FoodOrder(104, "Soham", "Pizza Hut",
                "Cheese Pizza", 2, 700,
                "Surat", "Pending")

order5 = FoodOrder(105, "Jaado", "Subway",
                "Veg Sandwich", 2, 350,
                "Delhi", "Pending")


print(order1.place_order())
print(order2.make_payment())
print(order3.track_order())
print(order4.cancel_order())
print()
print(order5.show_order())