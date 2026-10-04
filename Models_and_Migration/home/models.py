from django.db import models

# Create your models here.


class Student(models.Model):
    # id = models.AutoField() Automatically added by django
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    address = models.TextField(null=True , blank=True)
    image = models.ImageField()
    file = models.FileField()
   

    
class Product(models.Model):
    pass