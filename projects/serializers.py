from rest_framework import serializers
#
#
from projects.models import Employee, Province, District
#
#
# # Serializers define the API representation.
class ProvinceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

#class ProjectSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Project
#           fields = ['project_name', 'project_description', 'start_date', 'end_date',
#                   'project_manager_email', 'province', 'district', 'town']
