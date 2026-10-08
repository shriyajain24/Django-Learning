from django.db import models

# Create your models here.

# CRUD - Create, Read, Update, Delete

class Student(models.Model):
    # id = models.AutoField() Automatically added by django
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(blank=True,null=True)
    address = models.TextField(null=True , blank=True)
    image = models.ImageField()
    file = models.FileField()
   

    
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)
    
    def __str__(self):
        return self.car_name
