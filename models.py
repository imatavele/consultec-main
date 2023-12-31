# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `#managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename #db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        #managed = False
        #db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        #managed = False
        #db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        #managed = False
        #db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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
    id_employee = models.OneToOneField('Employee', models.DO_NOTHING, db_column='id_employee')
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        #managed = False
        #db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        #managed = False
        #db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        #managed = False
        #db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    id_project = models.ForeignKey('Project', models.DO_NOTHING, db_column='id_project', blank=True, null=True)
    company_phone = models.CharField(max_length=200, blank=True, null=True)
    manager_phone = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    account_number = models.CharField(max_length=200, blank=True, null=True)
    invoice = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        #managed = False
        #db_table = 'company'


class Department(models.Model):
    id_department = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        #managed = False
        #db_table = 'department'


class District(models.Model):
    id_district = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    id_province = models.ForeignKey('Province', models.DO_NOTHING, db_column='id_province', blank=True, null=True)

    class Meta:
        #managed = False
        #db_table = 'district'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        #managed = False
        #db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        #managed = False
        #db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        #managed = False
        #db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        #managed = False
        #db_table = 'django_session'


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

    class Meta:
        #managed = False
        #db_table = 'employee'


class Enquirer(models.Model):
    id_employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='id_employee', blank=True, null=True)
    id_project = models.ForeignKey('Project', models.DO_NOTHING, db_column='id_project', blank=True, null=True)
    date_added = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        #managed = False
        #db_table = 'enquirer'


class Project(models.Model):
    id_project = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=250, blank=True, null=True)
    project_description = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    data_added = models.DateField(blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    project_manager = models.ForeignKey(Employee, models.DO_NOTHING, db_column='project_manager', blank=True, null=True)
    client_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        #managed = False
        #db_table = 'project'


class Province(models.Model):
    id_province = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        #managed = False
        #db_table = 'province'


class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        #managed = False
        #db_table = 'status'
