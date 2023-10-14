from django.db import models
from django.urls import reverse
from home.models import Category
# Create your models here.

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_slug = models.SlugField(unique=True)
    product_dec = models.TextField()
    product_price = models.IntegerField(default=0)
    product_img = models.ImageField(upload_to='picture')
    product_stock = models.IntegerField(default=0)
    product_is_available = models.BooleanField(default=False)
    product_created_date = models.DateTimeField(auto_now_add=True)
    product_modified_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.product_name
    
    