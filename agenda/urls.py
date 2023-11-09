from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.appointmentList),
    path('create', views.createAppointment),
    path('<id>', views.showAppointment),
    path('update/<id>/<action>', views.updateAppointment),
]