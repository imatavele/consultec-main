from django.contrib import admin

from employees.models import *

# Register your models here.
admin.register(Employee)
admin.site.register(Department)
admin.site.register(Employee)

