

from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from leaflet.admin import LeafletGeoAdmin

from projects.models import *

# Register your models here.

admin.register(Project)
admin.site.register(Project)
@admin.register(Province)
class ProvinceAdmin(LeafletGeoAdmin):
    """Province admin."""

    list_display = ("province", "zone")

@admin.register(District)
class DistrictAdmin(LeafletGeoAdmin):
    """District admin."""

    list_display = ("district", "province")

@admin.register(Post)
class PostAdmin(LeafletGeoAdmin):
    """Post admin."""

    list_display = ("post", "province", "district")

@admin.register(ProjectArea)
class ProjectAreaAdmin(LeafletGeoAdmin):
    """ProjectArea admin."""

    list_display = ("project_id", "territory_level", "name")

admin.site.register(Status)


class TransactionResource():
    class Meta:
        model = Project
        fields = ['id_project', 'project_name', 'end_date', 'start_date', 'project_manager_email', 'status']
