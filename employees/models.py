from django.db import models


class Employee(models.Model):
    id_employee = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    job_title = models.CharField(max_length=200, blank=True, null=True)
    date_added = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.fullname

class Department(models.Model):
    id_department = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)