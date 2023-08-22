from django.db import models
from django.contrib.gis.db import models as gis_models

from employees.models import Employee


class Project(models.Model):
    id_project = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=250, blank=True, null=True)
    project_description = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    date_added = models.DateField(blank=True, null=True)
    #province = models.CharField(max_length=255, blank=True, null=True)
    #district = models.CharField(max_length=255, blank=True, null=True)
    #town = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    project_manager = models.ForeignKey(Employee, models.DO_NOTHING, db_column='project_manager', blank=True, null=True)
    client_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.project_name

    class Meta:
        #managed = False
        #db_table = 'projects'

        def __init__(self):
            self.project_name = Project.project_name

# @property
#     def status_info(self):
#         res = {'class': None}
#
#         if self.status == "Paid":
#             res['class'] = 'text-success'
#         elif self.status == "Due":
#             res['class'] = 'text-warning'
#         elif self.status == "Canceled":
#             res['class'] = 'text-danger'
#
#         return res

# class Province(models.Model):
#     id_province = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200, blank=True, null=True)

#     def __str__(self):
#         return self.name
    
# class District(models.Model):
#     id_district = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     id_province = models.ForeignKey(Province, models.DO_NOTHING, db_column='id_province', blank=True,
#                                     null=True)
#     def __str__(self):
#         return self.name
    
class Province(gis_models.Model):
    zone = gis_models.CharField(max_length=254, blank=True, null=True)
    province = gis_models.CharField(max_length=254)
    geom = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.province
    
    def __unicode__(self):
    	return self.province
 
class District(gis_models.Model):
    district = gis_models.CharField(max_length=30)
    province = gis_models.CharField(max_length=30)
    geom = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.district
    
    def __unicode__(self):
    	return self.district

class Post(gis_models.Model):
    id_post = models.AutoField(primary_key=True)
    area = gis_models.FloatField()
    perimeter = gis_models.FloatField()
    district = gis_models.CharField(max_length=30)
    province = gis_models.CharField(max_length=30)
    post = gis_models.CharField(max_length=30)
    geom = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.post

    def __unicode__(self):
    	return self.post

class ProjectArea(gis_models.Model):
    NIVEL_TERRITORIAL = (
        ('Nacional', 'Nacional'),
        ('Provincial', 'Provincial'),
        ('Distrital', 'Distrital'),
        ('Posto Administrativo', 'Posto Admnistrativo'),
        ('Menor que Posto Administrativo', 'Menor que Posto Administrativo'),
    )
    id_project_area = gis_models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, default=None, null=True, on_delete=models.SET_NULL)
    date_added = gis_models.DateTimeField(auto_now_add=True, blank=True)
    name = gis_models.CharField(max_length=30)
    territory_level = gis_models.CharField(max_length=30, choices=NIVEL_TERRITORIAL)
    geom = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name

    def __unicode__(self):
    	return self.name
     
class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        #managed = False
        verbose_name_plural = 'statuses'
        
    def __str__(self):
        return self.name
