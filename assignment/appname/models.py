# sales/models.py

from django.db import models

class Customer(models.Model):
    """Model representing a customer."""
    first_name = models.CharField(max_length=50,  help_text="The customer's first name")
    last_name = models.CharField(max_length=50,  help_text="The customer's last name") 
    email = models.EmailField(unique=True, help_text="The customer's email address")
    phone_number = models.CharField(max_length=15, blank=True, null=True, help_text="The customer's phone number")
    address = models.TextField(blank=True, null=True, help_text="The customer's shipping address")

    def __str__(self):
        return self.name


class Order(models.Model):
    """Model representing an order placed by a customer."""
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE, 
        related_name="orders",
        help_text="The customer who placed this order"
    )
    order_date = models.DateTimeField(auto_now_add=True, help_text="The date and time the order was placed")
    total_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="The total amount for the order"
    )
    payment_method = models.CharField(
        max_length=50, 
        choices=[
            ('credit_card', 'Credit Card'),
            ('paypal', 'PayPal'),
            ('bank_transfer', 'Bank Transfer'),
            ('cash_on_delivery', 'Cash on Delivery')
        ],
        default='credit_card',
        help_text="The payment method used for the order"
    )
    payment_status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('paid', 'Paid'),
            ('failed', 'Failed'),
            ('refunded', 'Refunded')
        ],
        default='pending',
        help_text="The status of the payment"
    )
    shipping_address = models.TextField(help_text="The shipping address for the order")
    shipping_city = models.CharField(max_length=100, help_text="The city for shipping")
    shipping_state = models.CharField(max_length=100, blank=True, null=True, help_text="The state for shipping")
    shipping_postal_code = models.CharField(max_length=20, help_text="The postal code for shipping")
    shipping_country = models.CharField(max_length=100, help_text="The country for shipping")
    order_status = models.CharField(
        max_length=20,
        choices=[
            ('processing', 'Processing'),
            ('shipped', 'Shipped'),
            ('delivered', 'Delivered'),
            ('cancelled', 'Cancelled')
        ],
        default='processing',
        help_text="The current status of the order"
    )

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"

