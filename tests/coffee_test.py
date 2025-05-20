import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_name_valid():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_name_type_error():
    with pytest.raises(TypeError):
        Coffee(123)

def test_coffee_name_length_error():
    with pytest.raises(ValueError):
        Coffee("Ab")

def test_coffee_name_immutable():
    coffee = Coffee("Mocha")
    with pytest.raises(AttributeError):
        coffee.name = "Latte"

def test_coffee_orders():
    coffee = Coffee("Espresso")
    customer = Customer("Derrick")
    order1 = Order(customer, coffee, 4.0)
    order2 = Order(customer, coffee, 4.5)
    assert coffee.orders() == [order1, order2]

def test_coffee_customers():
    coffee = Coffee("Cappuccino")
    customer1 = Customer("Zain")
    customer2 = Customer("Charlie")
    Order(customer1, coffee, 5.0)
    Order(customer2, coffee, 6.0)
    Order(customer1, coffee, 5.5)
    assert set(coffee.customers()) == {customer1, customer2}

def test_num_orders():
    coffee = Coffee("Americano")
    customer = Customer("Dave")
    Order(customer, coffee, 3.0)
    Order(customer, coffee, 3.5)
    assert coffee.num_orders() == 2
    assert Coffee("NoOrders").num_orders() == 0

def test_average_price():
    coffee = Coffee("Mocha")
    customer = Customer("Eve")
    Order(customer, coffee, 4.0)
    Order(customer, coffee, 6.0)
    assert coffee.average_price() == 5.0
    assert Coffee("NoOrders").average_price() == 0