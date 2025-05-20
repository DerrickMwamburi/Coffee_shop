import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_valid():
    customer = Customer("Derrick")
    assert customer.name == "Derrick"

def test_customer_name_type_error():
    with pytest.raises(TypeError):
        Customer(123)

def test_customer_name_length_error():
    with pytest.raises(ValueError):
        Customer("A" * 16)  # Name too long

def test_customer_orders():
    customer = Customer("Zain")
    coffee = Coffee("Latte")
    order1 = Order(customer, coffee, 5.0)
    order2 = Order(customer, coffee, 6.0)
    assert customer.orders() == [order1, order2]

def test_customer_coffees():
    customer = Customer("Charlie")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Mocha")
    Order(customer, coffee1, 4.0)
    Order(customer, coffee2, 5.0)
    Order(customer, coffee1, 4.5)
    assert set(customer.coffees()) == {coffee1, coffee2}

def test_create_order():
    customer = Customer("Dave")
    coffee = Coffee("Cappuccino")
    order = customer.create_order(coffee, 7.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 7.0

def test_most_aficionado():
    coffee = Coffee("Americano")
    customer1 = Customer("Eve")
    customer2 = Customer("Frank")
    Order(customer1, coffee, 5.0)
    Order(customer1, coffee, 5.0)
    Order(customer2, coffee, 3.0)
    assert Customer.most_aficionado(coffee) == customer1
    assert Customer.most_aficionado(Coffee("NoOrders")) is None