from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.appointmentList),
    path('create', views.createAppointment),
]