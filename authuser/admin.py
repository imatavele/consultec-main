from django.contrib import admin

from authuser.models import AuthUser

# Register your models here.

admin.register(AuthUser)
admin.site.register(AuthUser)

