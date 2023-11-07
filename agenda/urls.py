from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('reservations/', views.reservationList),
]