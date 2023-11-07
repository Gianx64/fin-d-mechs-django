from django.db import models

# Create your models here.
class Reservation(models.Model):
    user = models.EmailField()
    date = models.DateTimeField()
    car_brand = models.CharField(max_length=128)
    car_model = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    address = models.CharField(max_length=128)
    commune = models.CharField(max_length=128)
    mech = models.EmailField()
    confirmed = models.BooleanField()