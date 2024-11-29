from django.test import TestCase
from .models import Customer, Order
from django.utils import timezone

class CustomerModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", email="john@example.com")

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.email, "john@example.com")

class OrderModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="Jane Doe", email="jane@example.com")
        self.order = Order.objects.create(customer=self.customer, order_date=timezone.now(), total_amount=100.50)

    def test_order_creation(self):
        self.assertEqual(self.order.customer.name, "Jane Doe")
        self.assertTrue(isinstance(self.order.order_date, timezone.datetime))
        self.assertEqual(self.order.total_amount, 100.50)

    def test_order_customer_relationship(self):
        self.assertEqual(self.order.customer.email, "jane@example.com")
        self.assertEqual(self.customer.orders.count(), 1)
        self.assertEqual(self.customer.orders.first().total_amount, 100.50)

    def test_order_string_representation(self):
        self.assertEqual(str(self.order), f'Order {self.order.id} by {self.customer.name}')

class CustomerOrderRelationshipTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="Alice", email="alice@example.com")
        self.order1 = Order.objects.create(customer=self.customer, order_date=timezone.now(), total_amount=50.00)
        self.order2 = Order.objects.create(customer=self.customer, order_date=timezone.now(), total_amount=75.00)

    def test_multiple_orders(self):
        self.assertEqual(self.customer.orders.count(), 2)
        self.assertEqual(self.customer.orders.first().total_amount, 50.00)
        self.assertEqual(self.customer.orders.last().total_amount, 75.00)

