class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string.")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = value

    def _add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders.copy()

    def customers(self):
        customers_set = set()
        for order in self._orders:
            customers_set.add(order.customer)
        return list(customers_set)

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0.0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)
