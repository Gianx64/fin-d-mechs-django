from django.db import models

# Create your models here.
class IsMech(models.Model):
    email = models.EmailField()
    mech = models.BooleanField() #True if mech, False if user