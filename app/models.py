from django.db import models

# Define any necessary models here
class Research(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sentiment = models.CharField(max_length=10, null=True, blank=True)
    result = models.CharField(max_length=10, null=True, blank=True)
    confidence = models.FloatField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.text

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('upi', 'UPI'),
        ('net_banking', 'Net Banking'),
        ('cash_on_delivery', 'Cash on Delivery'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name