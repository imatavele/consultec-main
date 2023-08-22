from django.urls import path
from . import views

urlpatterns = [

    path('', views.listEnquirer, name='listEnquirer'),
    path('deleteEnquirer/<id>', views.deleteEnquirer, name='deleteEnquirer')
]
