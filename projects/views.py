import time
from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from .serializers import EmployeeSerializer, ProvinceSerializer, DistrictSerializer
import json

from employees.models import Employee
from enquirers.models import Enquirer
from .forms import ProjectForm, ProjectAreaForm
from .models import Project, ProjectArea, Status, Province, District, Post


def addProject(request):

    '''
        context = {}
        employees = Employee.objects.filter()
        districts = District.objects.filter()
        provinces = Province.objects.filter()
        
        context['employees'] = employees
        context['provinces'] = provinces
        context['districts'] = districts
        return render(request, 'addProject.html', context)
    ''' 
    return render(request, 'addProject.html')

def editProject(request, id):
    project = Project.objects.get(pk=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
        messages.success(request, "Projecto actualizado com sucesso!")
        return render(request, 'listProject.html', {'projects': Project.objects.all()})

    messages.error(request, "Erro ao actualizar o projecto...")
    return render(request, 'editProject.html', {#'provinces': Province.objects.all(),
                                                #'districts': District.objects.all(),
                                                'project': project,
                                                'employees': Employee.objects.all(),
                                                'status': Status.objects.all()})

def addProjectArea(request, id):
    project = Project.objects.get(pk=id)
    provinces = Province.objects.all()
    districts = District.objects.all()
    posts = Post.objects.all()

    if request.method == 'POST':
        #print('Posting project area of', request.POST['territory_level'], 'level')
        
        match request.POST['territory_level']:
            case 'Nacional':
                all_provs = Province.objects.all()
                
                for prov in all_provs:
                    proj_area = ProjectArea()
                    proj_area.project_id = Project.objects.get(pk=request.POST['project_id'])
                    proj_area.territory_level = request.POST['territory_level']
                    proj_area.geom = prov.geom
                    overlapping_geoms = ProjectArea.objects.filter(geom__overlaps=proj_area.geom)
                    if len(overlapping_geoms) == 0:
                        proj_area.save()
            case 'Provincial':
                name = request.POST['prov_name']
                proj_area = ProjectArea()
                proj_area.project_id = Project.objects.get(pk=request.POST['project_id'])
                proj_area.territory_level = request.POST['territory_level']
                proj_area.name = name
                prov_geom = Province.objects.filter(province=name).first().geom
                proj_area.geom = prov_geom
                overlapping_geoms = ProjectArea.objects.filter(geom__overlaps=proj_area.geom)
                if len(overlapping_geoms) == 0:
                    proj_area.save()
                    messages.success(request, "Área do Projecto adicionada com sucesso!")
                else:
                    messages.error(request,'Uma sobreposição encontrada. Área de projeto não inserida')
            case 'Distrital':
                name = request.POST['district_name']
                proj_area = ProjectArea()
                proj_area.project_id = Project.objects.get(pk=request.POST['project_id'])
                proj_area.territory_level = request.POST['territory_level']
                proj_area.name = name
                district_geom = District.objects.filter(district=name).first().geom
                proj_area.geom = district_geom
                overlapping_geoms = ProjectArea.objects.filter(geom__overlaps=proj_area.geom)
                if len(overlapping_geoms) == 0:
                    proj_area.save()
                    messages.success(request, "Área do Projecto adicionada com sucesso!")
                else:
                    messages.error(request,'Uma sobreposição encontrada. Área de projeto não inserida')
            case 'Posto Administrativo':
                name = request.POST['post_name']
                proj_area = ProjectArea()
                proj_area.name = name
                proj_area.project_id = Project.objects.get(pk=request.POST['project_id'])
                proj_area.territory_level = request.POST['territory_level']
                post_geom = Post.objects.filter(post=name).first().geom
                proj_area.geom = post_geom
                overlapping_geoms = ProjectArea.objects.filter(geom__overlaps=proj_area.geom)
                if len(overlapping_geoms) == 0:
                    proj_area.save()
                    messages.success(request, "Área do Projecto adicionada com sucesso!")
                else:
                    messages.error(request,'Uma sobreposição encontrada. Área de projeto não inserida')
            case 'Menor que Posto Administrativo':
                name = request.POST['small_area_name']
                proj_area = ProjectArea()
                proj_area.name = name
                proj_area.project_id = Project.objects.get(pk=request.POST['project_id'])
                proj_area.territory_level = request.POST['territory_level']
                proj_area.geom = request.POST['geom']
                overlapping_geoms = ProjectArea.objects.filter(geom__overlaps=proj_area.geom)
                if len(overlapping_geoms) == 0:
                    proj_area.save()
                    messages.success(request, "Área do Projecto adicionada com sucesso!")
                else:
                    messages.error(request,'Uma sobreposição encontrada. Área de projeto não inserida')
            case _:
                print('Nada por fazer')
        return redirect('listProject')
    else:
        form = ProjectAreaForm()
        context = {'form': form, 
                   'project': project,
                   'provinces': provinces,
                   'districts': districts,
                   'posts': posts}

    return render(request, 'addProjectArea.html', context)

def listProject(request):
    projects = Project.objects.all()

    if request.method == 'POST':
        form = ProjectForm(request.POST or None)
        # form.initial.__setattr__('status', 'activo')
        if form.is_valid():
            form.save()
            messages.success(request, "Projecto criado com sucesso")
            time.sleep(2)
        else:
            messages.error(request, 'Error ao criar projecto ...')
            for error in form.errors:
                print(error)
    
    return render(request, 'listProject.html', {'projects': projects})


def deleteProject(request, id):
    item = Project.objects.get(pk=id)
    item.delete()
    messages.success(request, 'Projecto removido com sucesso!')
    return redirect('listProject')

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    permission_classes = [permissions.IsAuthenticated]

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]