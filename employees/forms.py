from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['fullname', 'email', 'phone_number', 'department',
                  'job_title', 'gender', 'birthdate', 'date_added']
        