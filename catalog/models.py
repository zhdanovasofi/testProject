from django.db import models
from django.core.validators import MinValueValidator

class Category(models.Model):
    categoty_id = models.AutoField(primary_key = True)
    category_name = models.CharField(max_length = 20)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_id  = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length = 40)
    product_price = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    categoty_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    balance = models.IntegerField(default=1)
    def __str__(self):
        return self.product_name
