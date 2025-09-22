from django.db import models

# Create your models here.
class OrderStatus(models.Model):
    name=models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.code

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Order #{self.id} - {customer_name}"         