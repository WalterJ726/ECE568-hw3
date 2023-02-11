from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50)

# class Driver(User):
#     carbrand = CharField
#     maxslot = IntField
#     platenumber = IntField(maxlength=6)

# class Order(models.model):
#     arrivalTime = DataTimeField()
    

