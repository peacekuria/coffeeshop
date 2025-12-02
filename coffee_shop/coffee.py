class Coffee:
    """
    Coffee class represents a type of coffee available in the coffee shop.
    
    Attributes:
        name (str): The name of the coffee.
        _orders (list): A list to store orders for this coffee.
    """
    
    def __init__(self, name):
        """
        Initialize a Coffee with a name.
        Name should be a string at least 3 characters long.
        """
        # Set name using the property setter to validate the input
        self.name = name
        # Initialize an empty list to store all orders for this coffee
        self._orders = []
    
    @property
    def name(self):
        """Get the coffee's name."""
        # Return the private _name attribute
        return self._name
    
    @name.setter
    def name(self, value):
        """Set the coffee's name with validation."""
        # Check if the provided value is a string type
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string.")
        # Check if the name has at least 3 characters
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        # If validation passes, assign the value to the private attribute
        self._name = value

    def _add_order(self, order):
        """Add an order to this coffee's orders list. (Internal method)"""
        # Append the order to this coffee's list (called by customer.create_order)
        self._orders.append(order)

    def orders(self):
        """Return a copy of the list of orders for this coffee."""
        # Return a copy to prevent external modification of the internal list
        return self._orders.copy()

    def customers(self):
        """Return a list of unique Customer instances who have ordered this coffee."""
        # Create an empty set to store unique customer objects
        customers_set = set()
        # Iterate through all orders for this coffee
        for order in self._orders:
            # Add each customer from the order to the set (duplicates automatically ignored)
            customers_set.add(order.customer)
        # Convert the set back to a list and return
        return list(customers_set)

    def num_orders(self):
        """Return the total number of times this coffee has been ordered."""
        # Simply return the count of orders in the list
        return len(self._orders)

    def average_price(self):
        """Return the average price for this coffee based on its orders."""
        # Check if there are no orders for this coffee
        if not self._orders:
            # Return 0.0 if no orders exist (avoid division by zero)
            return 0.0
        # Calculate the total of all order prices using sum()
        total = sum(order.price for order in self._orders)
        # Divide total by the number of orders to get average and return
        return total / len(self._orders)
