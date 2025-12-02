# Coffee Shop Domain Model

A Python application that models a Coffee Shop domain using object-oriented programming principles. This project demonstrates proper domain modeling with classes, methods, relationships, and data validation.

## Project Structure

```
coffee_shop/
├── customer.py          # Customer class definition
├── coffee.py            # Coffee class definition
├── order.py             # Order class definition
├── debug.py             # Interactive debug and testing script
├── tests/               # Test suite directory
│   ├── __init__.py
│   ├── test_customer.py # Customer class tests
│   ├── test_coffee.py   # Coffee class tests
│   └── test_order.py    # Order class tests
├── Pipfile              # Pipenv configuration file
└── README.md            # This file
```

## Setup and Installation

### Prerequisites
- Python 3.8+
- pipenv

### Installation Steps

1. Navigate to the project directory:
```bash
cd coffee_shop
```

2. Create and activate a virtual environment with pipenv:
```bash
pipenv install
pipenv shell
```

3. Install pytest for running tests:
```bash
pipenv install pytest
```

## Domain Model Overview

### Relationships

- **A Customer** can place many **Orders**
- **A Coffee** can have many **Orders**
- **An Order** belongs to one **Customer** and one **Coffee**
- **Customer** and **Coffee** have a many-to-many relationship through **Order**

### Classes

#### Customer
- **Attributes:**
  - `name` (str): Customer's name (1-15 characters)
- **Methods:**
  - `orders()`: Returns list of all orders for this customer
  - `coffees()`: Returns unique list of coffees ordered by this customer
  - `create_order(coffee, price)`: Creates a new order for this customer
  - `most_aficionado(coffee)` (class method): Returns the customer who spent the most on a coffee

#### Coffee
- **Attributes:**
  - `name` (str): Coffee name (minimum 3 characters)
- **Methods:**
  - `orders()`: Returns list of all orders for this coffee
  - `customers()`: Returns unique list of customers who ordered this coffee
  - `num_orders()`: Returns total number of times this coffee was ordered
  - `average_price()`: Returns average price of this coffee across all orders

#### Order
- **Attributes:**
  - `customer` (Customer): The customer who placed the order
  - `coffee` (Coffee): The coffee that was ordered
  - `price` (float): Price of the order (1.0-10.0)
- **Properties:**
  - All attributes are read-only properties with validation

## Usage Examples

### Creating Instances

```python
from customer import Customer
from coffee import Coffee

# Create a customer
alice = Customer("Alice")

# Create a coffee
espresso = Coffee("Espresso")

# Create an order through the customer
order = alice.create_order(espresso, 2.50)
```

### Querying Relationships

```python
# Get all orders for a customer
alice_orders = alice.orders()

# Get unique coffees ordered by a customer
alice_coffees = alice.coffees()

# Get all orders for a coffee
espresso_orders = espresso.orders()

# Get unique customers who ordered a coffee
espresso_customers = espresso.customers()

# Get number of times a coffee was ordered
espresso_count = espresso.num_orders()

# Get average price of a coffee
espresso_avg = espresso.average_price()

# Find the biggest customer (most aficionado) of a coffee
top_customer = Customer.most_aficionado(espresso)
```

## Running Tests

Run all tests:
```bash
pytest
```

Run specific test file:
```bash
pytest tests/test_customer.py
```

Run specific test:
```bash
pytest tests/test_customer.py::TestCustomerInitialization::test_customer_creation_valid
```

Run with verbose output:
```bash
pytest -v
```

Run with coverage:
```bash
pytest --cov=.
```

## Debug and Interactive Testing

Run the interactive debug script to see all features in action:
```bash
python debug.py
```

This script demonstrates:
- Creating customers and coffees
- Creating orders
- Querying relationships
- Calculating aggregates
- Testing exception handling

## Data Validation

The model includes comprehensive input validation:

### Customer Validation
- Name must be a string
- Name must be between 1-15 characters long

### Coffee Validation
- Name must be a string
- Name must be at least 3 characters long

### Order Validation
- Customer must be a valid Customer instance
- Coffee must be a valid Coffee instance
- Price must be a number (int or float)
- Price must be between 1.0 and 10.0

### Exception Handling

All validation errors raise appropriate exceptions:
```python
from customer import Customer

try:
    invalid = Customer("InvalidNameThatIsTooLong")
except ValueError as e:
    print(f"Error: {e}")
```

## Code Quality

- Follows PEP 8 style guidelines
- Includes comprehensive docstrings
- Uses type hints for better code clarity
- Circular imports handled with TYPE_CHECKING
- Clean separation of concerns
- Single source of truth for data relationships

## Key Features

1. **Object-Oriented Design:** Classes model real-world entities with proper encapsulation
2. **Data Validation:** Input validation ensures data integrity
3. **Relationships:** Proper implementation of many-to-many relationships
4. **Aggregate Methods:** Helper methods for common queries
5. **Test Coverage:** Comprehensive test suite with pytest
6. **Documentation:** Well-documented code with docstrings

## Dependencies

- pytest (for testing)

## Authors

Created as a code challenge assignment for learning object-oriented programming in Python.

## License

This project is private and for educational purposes only.
