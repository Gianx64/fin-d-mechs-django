from django.contrib import admin
from .models import Appointment, Workshop

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Workshop)