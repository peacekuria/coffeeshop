from __future__ import annotations
from typing import TYPE_CHECKING

# Import Order for creating orders
from order import Order

if TYPE_CHECKING:
    # Import Coffee only for type hinting to avoid circular import issues
    from coffee import Coffee

class Customer:
    """
    Customer class represents a customer in the coffee shop.
    
    Attributes:
        name (str): The name of the customer.
        _orders (list): A list to store orders made by this customer.
    
    Class Attributes:
        _all_orders (list): List of all orders made by all customers.
    """

    _all_orders = []

    def __init__(self, name: str):
        """
        Initialize a Customer with a name.
        Name should be a string between 1 and 15 characters.
        """
        self.name = name  # This will trigger the name setter validation
        self._orders = []  # Initialize empty list of orders for this customer
    
    @property
    def name(self) -> str:
        """Get the customer's name."""
        return self._name
    
    @name.setter
    def name(self, value: str):
        """Set the customer's name with validation."""
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value

    def orders(self) -> list[Order]:
        """
        Return a copy of the list of orders belonging to this customer.
        """
        return self._orders.copy()
    
    def coffees(self) -> list[Coffee]:
        """
        Return a list of unique Coffee instances that this customer has ordered.
        """
        coffees_set = set()
        for order in self._orders:
            coffees_set.add(order.coffee)
        return list(coffees_set)

    def create_order(self, coffee: Coffee, price: float) -> Order:
        """
        Create a new Order instance for this customer with the given coffee and price.
        
        Args:
            coffee (Coffee): The Coffee instance to order.
            price (float): The price of the coffee (should be between 1.0 and 10.0).
        
        Returns:
            Order: The newly created Order instance.
        
        Raises:
            TypeError: If coffee is not an instance of Coffee.
        """
        if not hasattr(coffee, 'name'):
            raise TypeError("coffee must be an instance of Coffee class")
        
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)  # Add order to this customer's list
        Customer._all_orders.append(new_order)  # Add to class-wide orders list
        coffee._add_order(new_order)  # Add order to the coffee's orders list
        return new_order

    @classmethod
    def most_aficionado(cls, coffee: Coffee) -> Customer | None:
        """
        Find the customer who has spent the most money on a given coffee.
        
        Args:
            coffee (Coffee): The coffee to check against.
        
        Returns:
            Customer: The customer who spent the most money on this coffee.
            None: If no customers found for this coffee.
        """
        if not coffee.orders():
            return None
        
        spending = {}
        for order in coffee.orders():
            cust = order.customer
            spending[cust] = spending.get(cust, 0) + order.price
        
        if not spending:
            return None
        
        # Find customer with max total spending on the coffee
        max_spender = max(spending, key=spending.get)
        return max_spender
