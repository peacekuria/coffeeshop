"""
Debug file to test the coffee shop domain model interactively.
This file demonstrates how to use the Customer, Coffee, and Order classes.
"""

# Import the Customer class to create customer instances
from customer import Customer
# Import the Coffee class to create coffee instances
from coffee import Coffee


def main():
    """Run debug tests to verify the domain model works correctly."""
    
    print("=== Coffee Shop Domain Model - Debug Testing ===\n")
    
    # SECTION 1: Create some customers
    print("1. Creating Customers:")
    alice = Customer("Alice")
    bob = Customer("Bob")
    charlie = Customer("Charlie")
    print(f"   - Created: {alice.name}, {bob.name}, {charlie.name}\n")
    
    # SECTION 2: Create some coffees
    print("2. Creating Coffees:")
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")
    print(f"   - Created: {espresso.name}, {latte.name}, {cappuccino.name}\n")
    
    # SECTION 3: Test create_order method
    # This demonstrates the many-to-many relationship through Order
    print("3. Creating Orders:")
    # Alice creates two orders
    alice.create_order(espresso, 2.5)
    alice.create_order(latte, 3.5)
    # Bob creates two orders
    bob.create_order(espresso, 2.5)
    bob.create_order(cappuccino, 3.0)
    # Charlie creates one order
    charlie.create_order(latte, 3.5)
    print("   - Alice ordered Espresso (2.5) and Latte (3.5)")
    print("   - Bob ordered Espresso (2.5) and Cappuccino (3.0)")
    print("   - Charlie ordered Latte (3.5)\n")
    
    # SECTION 4: Test customer.orders() method
    # Each customer can retrieve all their orders
    print("4. Testing Customer Orders:")
    print(f"   - Alice has {len(alice.orders())} orders")
    print(f"   - Bob has {len(bob.orders())} orders")
    print(f"   - Charlie has {len(charlie.orders())} orders\n")
    
    # SECTION 5: Test customer.coffees() method
    # Each customer can get a unique list of coffees they've ordered
    print("5. Testing Customer Coffees (unique):")
    alice_coffees = alice.coffees()
    bob_coffees = bob.coffees()
    charlie_coffees = charlie.coffees()
    print(f"   - Alice ordered: {[c.name for c in alice_coffees]}")
    print(f"   - Bob ordered: {[c.name for c in bob_coffees]}")
    print(f"   - Charlie ordered: {[c.name for c in charlie_coffees]}\n")
    
    # SECTION 6: Test coffee.orders() method
    # Each coffee can retrieve all orders for that coffee
    print("6. Testing Coffee Orders:")
    print(f"   - Espresso has {len(espresso.orders())} orders")
    print(f"   - Latte has {len(latte.orders())} orders")
    print(f"   - Cappuccino has {len(cappuccino.orders())} orders\n")
    
    # SECTION 7: Test coffee.customers() method
    # Each coffee can get a unique list of customers who ordered it
    print("7. Testing Coffee Customers (unique):")
    espresso_customers = espresso.customers()
    latte_customers = latte.customers()
    cappuccino_customers = cappuccino.customers()
    print(f"   - Espresso ordered by: {[c.name for c in espresso_customers]}")
    print(f"   - Latte ordered by: {[c.name for c in latte_customers]}")
    print(f"   - Cappuccino ordered by: {[c.name for c in cappuccino_customers]}\n")
    
    # SECTION 8: Test coffee.num_orders() method
    # Each coffee can report how many times it has been ordered
    print("8. Testing Coffee num_orders():")
    print(f"   - Espresso: {espresso.num_orders()} orders")
    print(f"   - Latte: {latte.num_orders()} orders")
    print(f"   - Cappuccino: {cappuccino.num_orders()} orders\n")
    
    # SECTION 9: Test coffee.average_price() method
    # Calculate and display the average price for each coffee
    print("9. Testing Coffee average_price():")
    print(f"   - Espresso average price: ${espresso.average_price():.2f}")
    print(f"   - Latte average price: ${latte.average_price():.2f}")
    print(f"   - Cappuccino average price: ${cappuccino.average_price():.2f}\n")
    
    # SECTION 10: Test most_aficionado() class method
    # Find the customer who spent the most money on each coffee
    print("10. Testing Customer.most_aficionado():")
    espresso_aficionado = Customer.most_aficionado(espresso)
    latte_aficionado = Customer.most_aficionado(latte)
    cappuccino_aficionado = Customer.most_aficionado(cappuccino)
    
    # Check if results are not None before printing
    if espresso_aficionado:
        print(f"   - Espresso most aficionado: {espresso_aficionado.name}")
    if latte_aficionado:
        print(f"   - Latte most aficionado: {latte_aficionado.name}")
    if cappuccino_aficionado:
        print(f"   - Cappuccino most aficionado: {cappuccino_aficionado.name}\n")
    
    # SECTION 11: Test exception handling
    # Demonstrate that invalid inputs raise appropriate exceptions
    print("11. Testing Exception Handling:")
    # Try to create a customer with a name that's too long
    try:
        Customer("Alice123456789Invalid")
    except ValueError as e:
        print(f"   - Caught ValueError: {e}")
    
    # Try to create a coffee with a name that's too short
    try:
        Coffee("Jo")
    except ValueError as e:
        print(f"   - Caught ValueError: {e}")
    
    # Try to create an order with a price that's too high
    try:
        bob.create_order(latte, 15.0)
    except ValueError as e:
        print(f"   - Caught ValueError for price: {e}\n")
    
    print("=== Debug Testing Complete ===")


# Python convention: execute main only if this file is run directly
if __name__ == "__main__":
    main()
