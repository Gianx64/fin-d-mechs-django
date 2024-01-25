from django.db import models

# Create your models here.
class Workshop(models.Model):
    owner = models.EmailField()
    mechs = models.CharField(max_length=128)    #mechs ids separated by ", "
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    address = models.CharField(max_length=150)
    open = models.TimeField()   #opening time
    close = models.TimeField()  #closing time
    deleted = models.BooleanField(default=False)
    description = models.CharField(max_length=256)