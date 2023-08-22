from django.shortcuts import render

from employees.models import Employee
from projects.models import Project
from quizzes.models import Company


# Create your views here.
def listQuiz(request, id):
    project = Project.objects.get(pk=id)
    company = Company.objects.all()
    employee = Employee.objects.all()
    return render(request, 'listQuiz.html', {'project': project,
                                             'companies': company,
                                             'employees': employee})

