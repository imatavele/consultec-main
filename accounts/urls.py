from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.loginUser, name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
]
