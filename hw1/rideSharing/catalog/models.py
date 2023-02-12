from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

class Driver(User):
    VEHICLE_TYPES = (
        ('b', 'BMW'),
        ('f', 'Ford'),
        ('k', 'Kia'),
        ('m', 'Maserati'),
        ('n', 'Nissan'),
    )
    vehicle_type = models.CharField(max_length=1, choices=VEHICLE_TYPES)
    maxslot = models.SmallIntegerField()
    plate_number = models.IntegerField()

class Order(models.Model):
    VEHICLE_TYPES = (
        ('b', 'BMW'),
        ('f', 'Ford'),
        ('k', 'Kia'),
        ('m', 'Maserati'),
        ('n', 'Nissan'),
    )
    user = models.ManyToManyField('User')
    destination = models.CharField(max_length=100)
    arrival_time = models.DateTimeField()
    total_passanger = models.SmallIntegerField()
    vehicle_type = models.CharField(max_length=1, choices=VEHICLE_TYPES)
    # plate_numer = models.OneToOneField('Driver', )
    plate_numer = models.IntegerField(null=True, blank=True)
    sharable = models.BooleanField()
    special_requests = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=True)
    completed_time = models.DateTimeField(null=True, blank=True)


    class Meta:
        ordering = ["completed_time"]
    
    

