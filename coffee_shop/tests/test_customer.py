import sys
sys.path.insert(0, '..')

import pytest
from customer import Customer
from coffee import Coffee
from order import Order


class TestCustomerInitialization:
    """Test Customer class initialization and properties."""
    
    def test_customer_creation_valid(self):
        """Test creating a customer with valid name."""
        customer = Customer("Alice")
        assert customer.name == "Alice"
    
    def test_customer_name_validation_type(self):
        """Test that customer name must be a string."""
        with pytest.raises(TypeError):
            Customer(123)
    
    def test_customer_name_validation_min_length(self):
        """Test that customer name must be at least 1 character."""
        with pytest.raises(ValueError):
            Customer("")
    
    def test_customer_name_validation_max_length(self):
        """Test that customer name cannot exceed 15 characters."""
        with pytest.raises(ValueError):
            Customer("Alice VeryLongName")


class TestCustomerOrders:
    """Test Customer order management."""

    def test_customer_orders_empty(self):
        """Test that new customer has no orders."""
        customer = Customer("Bob")  # Create a new customer instance
        assert customer.orders() == []  # Verify it starts with no orders

    def test_customer_create_order(self):
        """Test creating an order through customer."""
        customer = Customer("Charlie")  # Create a customer instance
        coffee = Coffee("Espresso")  # Create a coffee instance
        order = customer.create_order(coffee, 2.5)  # Customer creates an order

        assert isinstance(order, Order)  # Verify order is an Order instance
        assert order.customer == customer  # Verify order belongs to customer
        assert order.coffee == coffee  # Verify order is for the coffee
        assert order.price == 2.5  # Verify price is set correctly

    def test_customer_orders_list(self):
        """Test that customer orders are tracked."""
        customer = Customer("Diana")  # Create a customer instance
        coffee1 = Coffee("Latte")  # Create first coffee instance
        coffee2 = Coffee("Cappuccino")  # Create second coffee instance

        order1 = customer.create_order(coffee1, 3.0)  # First order
        order2 = customer.create_order(coffee2, 3.5)  # Second order

        assert len(customer.orders()) == 2  # Verify customer has two orders
        assert order1 in customer.orders()  # Verify first order is tracked
        assert order2 in customer.orders()  # Verify second order is tracked


class TestCustomerCoffees:
    """Test Customer coffees relationship."""
    
    def test_customer_coffees_empty(self):
        """Test that new customer has no coffees."""
        customer = Customer("Eve")  # create customer
        assert customer.coffees() == []  # no coffees

    def test_customer_unique_coffees(self):
        """Test that customer coffees returns unique list."""
        customer = Customer("Frank")  # create customer
        coffee = Coffee("Mocha")  # create coffee

        # Create multiple orders for same coffee
        customer.create_order(coffee, 3.0)  # first order
        customer.create_order(coffee, 3.0)  # second order

        coffees = customer.coffees()  # get coffees
        assert len(coffees) == 1  # one unique coffee
        assert coffee in coffees  # coffee in list

    def test_customer_multiple_coffees(self):
        """Test that customer can order multiple different coffees."""
        customer = Customer("Grace")  # create customer
        coffee1 = Coffee("Americano")  # create coffee 1
        coffee2 = Coffee("Macchiato")  # create coffee 2

        customer.create_order(coffee1, 2.0)  # order coffee 1
        customer.create_order(coffee2, 2.5)  # order coffee 2

        coffees = customer.coffees()  # get coffees
        assert len(coffees) == 2  # two coffees


class TestMostAficionado:
    """Test the most_aficionado class method."""
    
    def test_most_aficionado_no_orders(self):
        """Test most_aficionado with no orders for a coffee."""
        coffee = Coffee("Flat White")
        result = Customer.most_aficionado(coffee)
        assert result is None
    
    def test_most_aficionado_single_customer(self):
        """Test most_aficionado with one customer."""
        customer = Customer("Henry")
        coffee = Coffee("Cortado")
        
        customer.create_order(coffee, 2.5)
        
        result = Customer.most_aficionado(coffee)
        assert result == customer
    
    def test_most_aficionado_multiple_customers(self):
        """Test most_aficionado with multiple customers."""
        coffee = Coffee("Irish Coffee")
        
        customer1 = Customer("Iris")
        customer2 = Customer("Jack")
        
        # Jack spends more on this coffee
        customer1.create_order(coffee, 2.0)
        customer2.create_order(coffee, 3.0)
        customer2.create_order(coffee, 4.0)
        
        result = Customer.most_aficionado(coffee)
        assert result == customer2
    
    def test_most_aficionado_equal_spending(self):
        """Test most_aficionado when customers spend equally."""
        coffee = Coffee("Macchiato")
        
        customer1 = Customer("Kate")
        customer2 = Customer("Liam")
        
        customer1.create_order(coffee, 3.0)
        customer2.create_order(coffee, 3.0)
        
        result = Customer.most_aficionado(coffee)
        assert result in [customer1, customer2]
