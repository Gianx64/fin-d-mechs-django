from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.home),
    path('profile', views.profile),
    path('signup', views.signup),
    path('signin', views.signin),
    path('signout', views.signout),
]