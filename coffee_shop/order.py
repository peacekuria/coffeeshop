from __future__ import annotations
from typing import TYPE_CHECKING

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
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def customer(self) -> Customer:
        """Get the customer who made the order."""
        return self._customer
    
    @customer.setter
    def customer(self, value: Customer):
        if not hasattr(value, 'name'):
            raise TypeError("customer must be an instance of Customer class")
        self._customer = value

    @property
    def coffee(self) -> Coffee:
        """Get the coffee in this order."""
        return self._coffee
    
    @coffee.setter
    def coffee(self, value: Coffee):
        if not hasattr(value, 'name'):
            raise TypeError("coffee must be an instance of Coffee class")
        self._coffee = value

    @property
    def price(self) -> float:
        """Get the price of this order."""
        return self._price
    
    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("price must be a number")
        if not (1.0 <= float(value) <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0")
        self._price = float(value)
