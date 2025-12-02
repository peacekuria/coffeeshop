import sys
sys.path.insert(0, '..')

import pytest
from order import Order
from customer import Customer
from coffee import Coffee


class TestOrderInitialization:
    """Test Order class initialization and properties."""
    
    def test_order_creation_valid(self):
        """Test creating an order with valid inputs."""
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 2.5)
        
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 2.5
    
    def test_order_customer_validation(self):
        """Test that order requires a valid customer."""
        coffee = Coffee("Latte")  # Create a coffee instance

        with pytest.raises(TypeError):  # Expect TypeError for invalid customer
            Order("not a customer", coffee, 3.0)  # Pass string instead of Customer

    def test_order_coffee_validation(self):
        """Test that order requires a valid coffee."""
        customer = Customer("Bob")  # Create a customer instance

        with pytest.raises(TypeError):  # Expect TypeError for invalid coffee
            Order(customer, "not a coffee", 3.0)  # Pass string instead of Coffee

    def test_order_price_validation_type(self):
        """Test that order price must be a number."""
        customer = Customer("Charlie")  # Create a customer instance
        coffee = Coffee("Cappuccino")  # Create a coffee instance

        with pytest.raises(TypeError):  # Expect TypeError for non-numeric price
            Order(customer, coffee, "not a number")  # Pass string instead of number

    def test_order_price_validation_min(self):
        """Test that order price must be at least 1.0."""
        customer = Customer("Diana")  # Create a customer instance
        coffee = Coffee("Mocha")  # Create a coffee instance

        with pytest.raises(ValueError):  # Expect ValueError for price too low
            Order(customer, coffee, 0.5)  # Pass price below minimum

    def test_order_price_validation_max(self):
        """Test that order price cannot exceed 10.0."""
        customer = Customer("Eve")  # Create a customer instance
        coffee = Coffee("Americano")  # Create a coffee instance

        with pytest.raises(ValueError):  # Expect ValueError for price too high
            Order(customer, coffee, 15.0)  # Pass price above maximum


class TestOrderProperties:
    """Test Order property getters."""
    
    def test_order_customer_property(self):
        """Test that customer property returns the customer."""
        customer = Customer("Frank")
        coffee = Coffee("Cortado")
        order = Order(customer, coffee, 2.0)
        
        assert order.customer == customer
    
    def test_order_coffee_property(self):
        """Test that coffee property returns the coffee."""
        customer = Customer("Grace")
        coffee = Coffee("Macchiato")
        order = Order(customer, coffee, 3.0)
        
        assert order.coffee == coffee
    
    def test_order_price_property(self):
        """Test that price property returns the price as float."""
        customer = Customer("Henry")
        coffee = Coffee("Flat White")
        order = Order(customer, coffee, 3.5)
        
        assert order.price == 3.5
        assert isinstance(order.price, float)


class TestOrderIntegerPrice:
    """Test that integer prices are converted to float."""
    
    def test_order_integer_price_conversion(self):
        """Test that integer prices are converted to float."""
        customer = Customer("Iris")  # Create a customer instance
        coffee = Coffee("Irish Coffee")  # Create a coffee instance
        order = Order(customer, coffee, 5)  # Create an order with integer price

        assert order.price == 5.0  # Verify price is converted to float
        assert isinstance(order.price, float)  # Verify it's a float


class TestOrderValidPriceRange:
    """Test valid price ranges."""
    
    def test_order_minimum_price(self):
        """Test order with minimum valid price."""
        customer = Customer("Jack")
        coffee = Coffee("Lungo")
        order = Order(customer, coffee, 1.0)
        
        assert order.price == 1.0
    
    def test_order_maximum_price(self):
        """Test order with maximum valid price."""
        customer = Customer("Kate")
        coffee = Coffee("Ristretto")
        order = Order(customer, coffee, 10.0)
        
        assert order.price == 10.0
    
    def test_order_mid_range_price(self):
        """Test order with mid-range price."""
        customer = Customer("Liam")
        coffee = Coffee("Affogato")
        order = Order(customer, coffee, 5.5)
        
        assert order.price == 5.5
