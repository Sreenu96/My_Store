from django.db import models
from .category import Category
class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to='image')
    desc = models.TextField()
    price = models.IntegerField()