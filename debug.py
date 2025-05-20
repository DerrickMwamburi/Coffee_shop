from customer import Customer
from coffee import Coffee
from order import Order

def main():
    # Create four sample customers
    alice = Customer("Alice")
    bob = Customer("Bob")
    charlie = Customer("Charlie")
    dave = Customer("Dave")
    
    # Create some coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    cappuccino = Coffee("Cappuccino")
    
    # Create some orders
    alice.create_order(latte, 5.0)
    alice.create_order(espresso, 4.0)
    bob.create_order(latte, 5.5)
    charlie.create_order(cappuccino, 6.0)
    dave.create_order(latte, 5.0)
    dave.create_order(espresso, 4.5)
    
    # Test relationships and aggregates
    print(f"Alice's orders: {len(alice.orders())}")
    print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")
    print(f"Latte's customers: {[customer.name for customer in latte.customers()]}")
    print(f"Latte's order count: {latte.num_orders()}")
    print(f"Latte's average price: {latte.average_price()}")
    
    # Test most_aficionado
    most_aficionado = Customer.most_aficionado(latte)
    print(f"Most aficionado for Latte: {most_aficionado.name if most_aficionado else None}")

if __name__ == "__main__":
    main()