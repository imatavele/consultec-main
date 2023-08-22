from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'provinces', views.ProvinceViewSet)
router.register(r'districts', views.DistrictViewSet)
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.listProject, name="listProject"),
    path('addProject', views.addProject, name="addProject"),
    path('deleteProject/<id>', views.deleteProject, name='deleteProject'),
    path('editProject/<id>', views.editProject, name='editProject'),
    path('addProjectArea/<id>', views.addProjectArea, name='addProjectArea'),

    ]


