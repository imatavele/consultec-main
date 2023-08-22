from django.urls import path

from . import views

urlpatterns = [
    path("listQuiz/<id>", views.listQuiz, name="listQuiz")
]
