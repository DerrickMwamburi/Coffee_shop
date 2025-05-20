import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_valid():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_invalid_customer():
    coffee = Coffee("Mocha")
    with pytest.raises(TypeError):
        Order("NotACustomer", coffee, 5.0)

def test_order_invalid_coffee():
    customer = Customer("Bob")
    with pytest.raises(TypeError):
        Order(customer, "NotACoffee", 5.0)

def test_order_invalid_price_type():
    customer = Customer("Charlie")
    coffee = Coffee("Espresso")
    with pytest.raises(TypeError):
        Order(customer, coffee, "5.0")

def test_order_invalid_price_range():
    customer = Customer("Dave")
    coffee = Coffee("Cappuccino")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)

def test_price_immutable():
    customer = Customer("Eve")
    coffee = Coffee("Americano")
    order = Order(customer, coffee, 4.0)
    with pytest.raises(AttributeError):
        order.price = 5.0