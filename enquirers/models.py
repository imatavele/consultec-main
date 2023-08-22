from django.db import models

from employees.models import Employee
from projects.models import Project


# Create your models here.

class Enquirer(models.Model):
    id_employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='id_employee', blank=True, null=True)
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='id_project', blank=True, null=True)
    date_added = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)