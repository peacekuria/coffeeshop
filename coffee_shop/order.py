# Enable forward references for type hints
from __future__ import annotations
from typing import TYPE_CHECKING

# Use TYPE_CHECKING to avoid circular imports at runtime
# Customer and Coffee are only imported for type hinting, not actual execution
if TYPE_CHECKING:
    from customer import Customer
    from coffee import Coffee

class Order:
    """
    Order class represents an order placed by a customer for a coffee, with a price.
    """

    def __init__(self, customer: Customer, coffee: Coffee, price: float):
        """
        Initialize an Order with a customer, coffee, and price.
        
        Args:
            customer (Customer): The customer who made the order.
            coffee (Coffee): The coffee that was ordered.
            price (float): Price of the coffee (between 1.0 and 10.0).
        
        Raises:
            TypeError: If customer or coffee are not instances of respective classes.
            ValueError: If price is not between 1.0 and 10.0.
        """
        # Set customer using the property setter to validate the input
        self.customer = customer
        # Set coffee using the property setter to validate the input
        self.coffee = coffee
        # Set price using the property setter to validate the input and convert to float
        self.price = price

    @property
    def customer(self) -> Customer:
        """Get the customer who made the order."""
        # Return the private _customer attribute
        return self._customer
    
    @customer.setter
    def customer(self, value: Customer):
        """Set and validate the customer for this order."""
        # Check if the value has a 'name' attribute to verify it's a Customer instance
        if not hasattr(value, 'name'):
            raise TypeError("customer must be an instance of Customer class")
        # If validation passes, assign to the private attribute
        self._customer = value

    @property
    def coffee(self) -> Coffee:
        """Get the coffee in this order."""
        # Return the private _coffee attribute
        return self._coffee
    
    @coffee.setter
    def coffee(self, value: Coffee):
        """Set and validate the coffee for this order."""
        # Check if the value has a 'name' attribute to verify it's a Coffee instance
        if not hasattr(value, 'name'):
            raise TypeError("coffee must be an instance of Coffee class")
        # If validation passes, assign to the private attribute
        self._coffee = value

    @property
    def price(self) -> float:
        """Get the price of this order."""
        # Return the private _price attribute
        return self._price
    
    @price.setter
    def price(self, value: float):
        """Set and validate the price for this order."""
        # Check if the value is a number (int or float)
        if not isinstance(value, (int, float)):
            raise TypeError("price must be a number")
        # Convert to float and check if it's in the valid range (1.0 to 10.0)
        if not (1.0 <= float(value) <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0")
        # If validation passes, convert to float and assign to the private attribute
        self._price = float(value)
