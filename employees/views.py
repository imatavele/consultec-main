import datetime

from django.template.loader import render_to_string

from employees.forms import EmployeeForm
from employees.models import Employee, Department

from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def addEmployee(request):
    return render(request, 'addEmployee.html', {'departments': Department.objects.all()})


def editEmployee(request, id):
    employee = Employee.objects.get(pk=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        messages.success(request, "Funcionário actualizado com sucesso...")
        return render(request, 'listEmployee.html', {'employees': Employee.objects.all()})

    messages.success(request, "Erro actualizado com sucesso..")
    return render(request, 'editEmployee.html', {'employee': employee, 'departments': Department.objects.all()})


def listEmployee(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionario criado com sucesso ...')
        else:
            messages.error(request, 'Erro ao criar novo funcionário ...')

    return render(request, 'listEmployee.html', {'employees': employees})


def deleteEmployee(request, id):
    item = Employee.objects.get(pk=id)
    item.delete()
    messages.success(request, 'Funcionário removido com sucesso!')
    return redirect('listEmployee')
