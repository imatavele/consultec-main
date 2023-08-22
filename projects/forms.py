from django import forms
from .models import Project, ProjectArea
from leaflet.forms.widgets import LeafletWidget


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['id_project', 'project_name', 'project_description', 'start_date', 'end_date',
                  'project_manager', 'status', 'client_name'] #'province', 'district', 'town',

class ProjectAreaForm(forms.ModelForm):
    class Meta:
        LEAFLET_WIDGET_ATTRS = {
		    'map_height': '400px',
		    'map_width': '100%',
		    'display_raw': 'true',
		    'map_srid': 4326,
		    'settings_overrides': {
		    	'DEFAULT_ZOOM': 5
		    }
		}
        model = ProjectArea
        fields = ('project_id', 'name', 'territory_level', 'geom')
        widgets = {'geom': LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS)}
