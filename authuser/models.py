from django.db import models

from employees.models import Employee


# Create your models here.


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    date_joined = models.DateTimeField(blank=True, null=True)
    id_employee = models.OneToOneField(Employee, models.DO_NOTHING, db_column='id_employee')
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        #managed = False
        verbose_name_plural = 'auth_users'
