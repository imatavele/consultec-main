import django_filters
from django import forms

from employees.models import Employee
from project.models import Project


class ProjectFilter(django_filters.FilterSet):

    employee = django_filters.ModelChoiceFilter(
        queryset=Employee.objects.all(),
        empty_label="All Employees",
        label="Employees",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )

    class Meta:
        model = Project
        fields = ['id_project', 'project_name', 'project_description', 'start_date', 'end_date',
                  'project_manager', 'province', 'district', 'town', 'status']