from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100)
    category_slug=models.CharField(unique=True)
    category_description=models.TextField()
    category_image=models.ImageField(upload_to='picture')

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.category_name
    
    def get_url(self):
        return reverse('category_sort',args=[self.category_slug])