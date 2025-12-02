import sys
sys.path.insert(0, '..')

import pytest
from coffee import Coffee
from customer import Customer


class TestCoffeeInitialization:
    """Test Coffee class initialization and properties."""

    def test_coffee_creation_valid(self):
        """Test creating a coffee with valid name."""
        coffee = Coffee("Espresso")  # Create a coffee instance with a valid name
        assert coffee.name == "Espresso"  # Verify the name is set correctly

    def test_coffee_name_validation_type(self):
        """Test that coffee name must be a string."""
        with pytest.raises(TypeError):  # Expect TypeError for non-string input
            Coffee(123)  # Pass an integer instead of string

    def test_coffee_name_validation_min_length(self):
        """Test that coffee name must be at least 3 characters."""
        with pytest.raises(ValueError):  # Expect ValueError for short name
            Coffee("Ab")  # Pass a name shorter than 3 characters


class TestCoffeeOrders:
    """Test Coffee order management."""

    def test_coffee_orders_empty(self):
        """Test that new coffee has no orders."""
        coffee = Coffee("Latte")
        assert coffee.orders() == []

    def test_coffee_orders_tracking(self):
        """Test that coffee tracks orders."""
        coffee = Coffee("Cappuccino")
        customer = Customer("Alice")

        order = customer.create_order(coffee, 3.0)

        assert len(coffee.orders()) == 1
        assert order in coffee.orders()


class TestCoffeeCustomers:
    """Test Coffee customers relationship."""
    
    def test_coffee_customers_empty(self):
        """Test that new coffee has no customers."""
        coffee = Coffee("Mocha")  # create coffee
        assert coffee.customers() == []  # no customers

    def test_coffee_unique_customers(self):
        """Test that coffee customers returns unique list."""
        coffee = Coffee("Americano")  # create coffee
        customer = Customer("Bob")  # create customer

        # Create multiple orders from same customer
        customer.create_order(coffee, 2.0)  # first order
        customer.create_order(coffee, 2.0)  # second order

        customers = coffee.customers()  # get customers
        assert len(customers) == 1  # one unique customer
        assert customer in customers  # customer in list

    def test_coffee_multiple_customers(self):
        """Test that coffee can be ordered by multiple customers."""
        coffee = Coffee("Cortado")  # create coffee
        customer1 = Customer("Charlie")  # create customer 1
        customer2 = Customer("Diana")  # create customer 2

        customer1.create_order(coffee, 2.5)  # order from customer 1
        customer2.create_order(coffee, 2.5)  # order from customer 2

        customers = coffee.customers()  # get customers
        assert len(customers) == 2  # two customers


class TestCoffeeNumOrders:
    """Test Coffee num_orders method."""

    def test_num_orders_empty(self):
        """Test num_orders for coffee with no orders."""
        coffee = Coffee("Macchiato")  # Create a coffee instance
        assert coffee.num_orders() == 0  # Should return 0 for no orders

    def test_num_orders_single(self):
        """Test num_orders for coffee with one order."""
        coffee = Coffee("Flat White")  # Create a coffee instance
        customer = Customer("Eve")  # Create a customer instance

        customer.create_order(coffee, 3.0)  # Customer creates an order

        assert coffee.num_orders() == 1  # Should return 1

    def test_num_orders_multiple(self):
        """Test num_orders for coffee with multiple orders."""
        coffee = Coffee("Irish Coffee")  # Create a coffee instance
        customer = Customer("Frank")  # Create a customer instance

        customer.create_order(coffee, 4.0)  # First order
        customer.create_order(coffee, 4.0)  # Second order
        customer.create_order(coffee, 4.0)  # Third order

        assert coffee.num_orders() == 3  # Should return 3


class TestCoffeeAveragePrice:
    """Test Coffee average_price method."""
    
    def test_average_price_empty(self):
        """Test average_price for coffee with no orders."""
        coffee = Coffee("Lungo")
        assert coffee.average_price() == 0.0
    
    def test_average_price_single(self):
        """Test average_price for coffee with one order."""
        coffee = Coffee("Ristretto")
        customer = Customer("Grace")
        
        customer.create_order(coffee, 2.5)
        
        assert coffee.average_price() == 2.5
    
    def test_average_price_multiple(self):
        """Test average_price for coffee with multiple orders."""
        coffee = Coffee("Affogato")
        customer1 = Customer("Henry")
        customer2 = Customer("Iris")
        
        customer1.create_order(coffee, 3.0)
        customer2.create_order(coffee, 5.0)
        
        assert coffee.average_price() == 4.0
    
    def test_average_price_precision(self):
        """Test average_price calculation with precision."""
        coffee = Coffee("Piccolo")
        customer = Customer("Jack")
        
        customer.create_order(coffee, 2.0)
        customer.create_order(coffee, 3.0)
        
        average = coffee.average_price()
        assert abs(average - 2.5) < 0.01
