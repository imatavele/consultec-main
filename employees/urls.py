from django.urls import path
from . import views

urlpatterns = [
    path("", views.listEmployee, name="listEmployee"),
    path("addEmployee", views.addEmployee, name="addEmployee"),
    path('editEmployee/<id>', views.editEmployee, name='editEmployee'),
    path('deleteEmployee/<id>', views.deleteEmployee, name='deleteEmployee')
]


