from django.db import models

# Create your models here.
class Appointment(models.Model):
    user = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    commune = models.CharField(max_length=128)
    address = models.CharField(max_length=150)
    car_brand = models.CharField(max_length=128)
    car_model = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    mech = models.EmailField()
    confirmed = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    #status = models.PositiveSmallIntegerField(default=0) #0 = Submitted, 1 = Confirmed, 2 = Canceled, 3 = Completed