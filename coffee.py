class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not 3 <= len(name) <= 15:  # Ensure name length is between 3 and 15
            raise ValueError("Name must be between 3 and 15 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot modify the name of a Coffee object")

    def orders(self):
        from order import Order  # Local import to avoid circular dependency
        return [order for order in Order._all_orders if order.coffee == self]

    def customers(self):
        from customer import Customer  # Local import to avoid circular dependency
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())  # Count the number of orders for this coffee

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0.0  # Return 0.0 if there are no orders
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)  # Calculate the average price