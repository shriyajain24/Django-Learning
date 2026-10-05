from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    image = models.ImageField()
    file = models.FileField()

class Product(models.Model):
    pass