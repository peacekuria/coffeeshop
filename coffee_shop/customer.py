# Enable forward references for type hints
from __future__ import annotations
from typing import TYPE_CHECKING

# Import Order class to create new orders
from order import Order

# Use TYPE_CHECKING to avoid circular imports at runtime
# Coffee is only imported for type hinting, not actual execution
if TYPE_CHECKING:
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

    # Class variable to track all orders across all customers (for most_aficionado method)
    _all_orders = []

    def __init__(self, name: str):
        """
        Initialize a Customer with a name.
        Name should be a string between 1 and 15 characters.
        """
        # Set name using the property setter to validate the input
        self.name = name
        # Initialize empty list to store this customer's orders
        self._orders = []
    
    @property
    def name(self) -> str:
        """Get the customer's name."""
        # Return the private _name attribute
        return self._name
    
    @name.setter
    def name(self, value: str):
        """Set the customer's name with validation."""
        # Check if the provided value is a string type
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        # Check if the name length is between 1 and 15 characters (inclusive)
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters.")
        # If validation passes, assign the value to the private attribute
        self._name = value

    def orders(self) -> list[Order]:
        """
        Return a copy of the list of orders belonging to this customer.
        """
        # Return a copy to prevent external modification of the internal list
        return self._orders.copy()
    
    def coffees(self) -> list[Coffee]:
        """
        Return a list of unique Coffee instances that this customer has ordered.
        """
        # Create an empty set to store unique coffee objects
        coffees_set = set()
        # Iterate through all orders for this customer
        for order in self._orders:
            # Add each coffee from the order to the set (duplicates are automatically ignored)
            coffees_set.add(order.coffee)
        # Convert the set back to a list and return
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
        # Check if coffee has a 'name' attribute to verify it's a Coffee instance
        if not hasattr(coffee, 'name'):
            raise TypeError("coffee must be an instance of Coffee class")
        
        # Create a new Order with this customer, the coffee, and the price
        # The Order constructor will validate the price automatically
        new_order = Order(self, coffee, price)
        # Add the order to this customer's list
        self._orders.append(new_order)
        # Add the order to the class-wide list for tracking all orders
        Customer._all_orders.append(new_order)
        # Add the order to the coffee's order list to maintain bidirectional relationship
        coffee._add_order(new_order)
        # Return the created order
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
        # Check if the coffee has any orders at all
        if not coffee.orders():
            # No orders found, so return None
            return None
        
        # Create an empty dictionary to track total spending per customer
        spending = {}
        # Iterate through all orders for this particular coffee
        for order in coffee.orders():
            # Get the customer from the order
            cust = order.customer
            # Add the order price to that customer's total (or 0 if first time)
            spending[cust] = spending.get(cust, 0) + order.price
        
        # Check if spending dictionary has any entries
        if not spending:
            # No spending data, return None
            return None
        
        # Use the max() function with key parameter to find customer with highest spending
        # The key parameter specifies that we want to compare by the dictionary values (prices)
        max_spender = max(spending, key=spending.get)
        # Return the customer who spent the most
        return max_spender
