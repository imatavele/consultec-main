from django import forms
from .models import Enquirer


class EnquirerForm(forms.ModelForm):
    class Meta:
        model = Enquirer
        fields = ['id_project', 'id_employee', 'position', 'date_added']
