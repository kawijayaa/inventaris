from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
