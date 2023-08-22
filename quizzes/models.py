from django.db import models

from projects.models import Project


# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=200, blank=True, null=True)
    manager_name = models.CharField(max_length=200, blank=True, null=True)
    business = models.CharField(max_length=200, blank=True, null=True)
    duat = models.CharField(max_length=200, blank=True, null=True)
    bank_name = models.CharField(max_length=200, blank=True, null=True)
    work_start = models.TimeField(blank=True, null=True)
    work_close = models.TimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    id_company = models.AutoField(primary_key=True)
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='id_project', blank=True, null=True)
    company_phone = models.CharField(max_length=200, blank=True, null=True)
    manager_phone = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    account_number = models.CharField(max_length=200, blank=True, null=True)
    invoice = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        #managed = False
        verbose_name_plural = 'companies'
