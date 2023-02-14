from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

class Driver(models.Model):
    VEHICLE_TYPES = (
        ('b', 'BMW'),
        ('f', 'Ford'),
        ('k', 'Kia'),
        ('m', 'Maserati'),
        ('n', 'Nissan'),
    )
    ## TODO: userid and driverid
    # driver_Index = models.OneToOneField('User',on_delete=models.CASCADE)
    driver_info = models.SmallIntegerField()
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
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)
    arrival_time = models.DateTimeField()
    total_passanger = models.SmallIntegerField()
    vehicle_type = models.CharField(max_length=1, choices=VEHICLE_TYPES)
    # plate_numer = models.OneToOneField('Driver', )
    comfirmed_order_driver = models.SmallIntegerField(null=True, blank=True)
    plate_numer = models.IntegerField(null=True, blank=True)
    shareable = models.BooleanField()
    shared_people = models.CharField(max_length=100, null=True, blank=True)
    special_requests = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=True)
    completed_time = models.DateTimeField(null=True, blank=True)


    class Meta:
        ordering = ["completed_time"]

    def __str__(self):
        """
        String for representing the Model object, using for debugging
        """
        return '%s (%s)' % (self.id,self.destination)
    
    

