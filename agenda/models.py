from django.db import models

# Create your models here.
class Appointment(models.Model):
    user = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    car_brand = models.CharField(max_length=128)
    car_model = models.CharField(max_length=128)
    description = models.TextField(max_length=256)
    mech = models.EmailField()
    confirmed = models.BooleanField(default=False)