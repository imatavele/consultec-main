from authuser.models import AuthUser
from django import forms


class AuthUserForm(forms.ModelForm):

    class Meta:
        model = AuthUser
        fields = ('username', 'email', 'password', 'is_superuser', 'first_name', 'last_name',
                  'is_staff', 'is_active', 'id_employee', 'category')
