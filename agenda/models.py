from django.db import models

# Create your models here.
class Appointment(models.Model):
    user = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    city = models.CharField(max_length=128)
    address = models.CharField(max_length=150)
    car_brand = models.CharField(max_length=128)
    car_model = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    service = models.BooleanField(default=None, blank=True, null=True)  #None = Workshop service, False = Home service, True = Pickup
    workshop = models.IntegerField(default=None, blank=True, null=True)
    mech = models.EmailField()
    confirmed = models.BooleanField(default=False)
    confirmtime = models.DateTimeField(default=None, blank=True, null=True)
    canceled = models.BooleanField(default=False)
    canceledby = models.EmailField(default=None, blank=True, null=True)
    canceltime = models.DateTimeField(default=None, blank=True, null=True)
    completed = models.BooleanField(default=False)
    completedtime = models.DateTimeField(default=None, blank=True, null=True)
    usercommenttime = models.DateTimeField(default=None, blank=True, null=True)
    usercomment = models.CharField(max_length=128, default=None, blank=True, null=True)   #reason for cancelling or comment of appointment
    mechcommenttime = models.DateTimeField(default=None, blank=True, null=True)
    mechcomment = models.CharField(max_length=128, default=None, blank=True, null=True)   #response for comment of appointment
    #status = models.PositiveSmallIntegerField(default=0) #0 = Submitted, 1 = Confirmed, 2 = Canceled, 3 = Completed

class Workshop(models.Model):
    mech = models.EmailField()
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    address = models.CharField(max_length=150)
    open = models.TimeField()   #opening time
    close = models.TimeField()  #closing time
    description = models.CharField(max_length=256)