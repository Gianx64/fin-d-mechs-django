from django.db import models

# Create your models here.
class Reservation(models.Model):
    user = models.EmailField()
    date = models.DateTimeField()
    location = models.CharField(max_length=128)
    car = models.CharField(max_length=128)
    mech = models.EmailField()
    confirmed = models.BooleanField()