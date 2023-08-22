from django.contrib import messages
from django.shortcuts import render, redirect

from employees.models import Employee
from enquirers.forms import EnquirerForm
from enquirers.models import Enquirer
from projects.models import Project


# Create your views here.

def listEnquirer(request):
    employee = Employee.objects.all()
    project = Project.objects.all()
    enquirer = Enquirer.objects.all()

    if request.method == 'POST':
        form = EnquirerForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inqueridor adicionado com sucesso ...')
        else:
            messages.error(request, 'Erro ao adicionar funcionario ...')

    return render(request, 'listEnquirer.html', {'enquires': enquirer,
                                                 'employees': employee,
                                                 'projects': project})


def deleteEnquirer(request, id):
    eq = Enquirer.objects.get(pk=id)
    eq.delete()
    employee = Employee.objects.all()
    project = Project.objects.all()
    enquirer = Enquirer.objects.all()
    messages.success(request, 'Inqueridor retirado com successo')
    return render(request, 'listEnquirer.html', {'enquires': enquirer,
                                                 'employees': employee,
                                                 'projects': project})
