from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.workshopList),
    path('create', views.createWorkshop),
    path('<id>', views.showWorkshop),
    path('update/<id>', views.updateWorkshop),
    path('delete/<id>', views.deleteWorkshop),
]