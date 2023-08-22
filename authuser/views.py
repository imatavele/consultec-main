from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.datetime_safe import datetime

from authuser.forms import AuthUserForm
from authuser.models import AuthUser
from employees.models import Employee


# Create your views here.
def addUser(request):
    if request.method == "POST":
        id_employee = request.POST['id_employee']
        password = request.POST['password']
        username = request.POST['username']
        role = request.POST['category']
        email = 'staff@gmail.com'
        is_superuser = 'False'
        first_name = ''
        last_name = ''
        is_staff = 'True'
        is_active = 'True'
        employee = Employee.objects.get(pk=id_employee)
        authuser = AuthUser.objects.create(username=username, email=email,
                                           password=password, is_superuser=is_superuser,
                                           first_name=first_name, last_name=last_name,
                                           is_staff=is_staff, is_active=is_active,
                                           id_employee=employee,
                                           category=role
                                           )
        authuser.save()
        messages.success(request, 'Utilizador criado com sucesso ...')
    return render(request, 'addUser.html', {'employees': Employee.objects.all()})


def listUser(request):
    return render(request, 'listUser.html', {'users': AuthUser.objects.all()})


def editUser(request, id):
    user = AuthUser.objects.get(pk=id)

    if request.method == 'POST':
        form = AuthUserForm(request.POST, instance=user)
        form.id_employee = user.id_employee.id_employee
        if form.is_valid():
            form.save()
            messages.success(request, 'Utilizador actualizado com sucesso.')
            return redirect('listUser', {'employees': Employee.objects.all()})
        else:
            messages.error(request, 'Dados de formulario incorrectos:')
            return render(request, 'editUser.html', {'form': form})

    return render(request, 'editUser.html', {'user': user, 'employees': Employee.objects.all()})


def deleteUser(request, id):
    item = AuthUser.objects.get(pk=id)
    item.delete()
    messages.success(request, 'Utilizador removido com sucesso!')
    return render(request, 'listUser.html', {'users': AuthUser.objects.all()})
