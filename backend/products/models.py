from django.db import models

# Create your models here.


class Product(models.Model):
    """A Django model to represent a product"""
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)

    @property
    def sale_price(self):
        return self.price * 0.85
