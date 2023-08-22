from django.urls import path
from . import views

urlpatterns = [

    path("", views.listUser, name="listUser"),
    path("addUser", views.addUser, name="addUser"),
    path('deleteUser/<id>', views.deleteUser, name='deleteUser'),
    path('editUser/<id>', views.editUser, name='editUser')

]