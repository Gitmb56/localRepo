class Order:
    def __init__(self, order_id, items, price):
        self.order_id = order_id      # Data (State)
        self.items = items            # List of items
        self.price = price            # Total price
        self.status = "CREATED"       # Initial status

    # Action 1: Place Order
    def place_order(self):
        if self.status == "CREATED":
            self.status = "PLACED"
            print(f"Order {self.order_id} placed successfully.")
        else:
            print("Order cannot be placed again.")

    # Action 2: Cancel Order
    def cancel_order(self):
        if self.status in ["CREATED", "PLACED"]:
            self.status = "CANCELLED"
            print(f"Order {self.order_id} has been cancelled.")
        else:
            print("Order cannot be cancelled.")

    # Action 3: Track Order
    def track_order(self):
        print(f"Order {self.order_id} status: {self.status}")

order1 = Order(
    order_id=101,
    items=["Laptop", "Mouse"],
    price=55000
)

order1.place_order()
order1.track_order()
order1.cancel_order()
order1.track_order()
