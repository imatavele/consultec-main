import os
from django.contrib.gis.utils import LayerMapping
from .models import Post, Province, District

# posts_mapping = {
#     'area': 'AREA',
#     'perimeter': 'PERIMETER',
#     'district': 'DISTRITO',
#     'province': 'PROVINCIA',
#     'post': 'POSTO',
#     'geom': 'MULTIPOLYGON',
# }

# posts_shp = os.path.abspath(
#     os.path.join(os.path.dirname(__file__), 'gislayers', 'moz-posts.shp'),
# )
# def run(verbose=True):
#     lm = LayerMapping(Post, posts_shp, posts_mapping, transform=True)
#     lm.save(strict=True, verbose=verbose)

# provinces_mapping = {
#     'zone': 'ZONA',
#     'province': 'PROVINCIA',
#     'geom': 'MULTIPOLYGON',
# }

# provinces_shp = os.path.abspath(
#     os.path.join(os.path.dirname(__file__), 'gislayers', 'moz-provs.shp'),
# )
# def run_provinces(verbose=True):
#     lm = LayerMapping(Province, provinces_shp, provinces_mapping, transform=True)
#     lm.save(strict=True, verbose=verbose)

# run_provinces()

districts_mapping = {
    'district': 'DISTRITO',
    'province': 'PROVINCIA',
    'geom': 'MULTIPOLYGON',
}

districts_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'gislayers', 'moz-districts.shp'),
)
def run_districts(verbose=True):
    lm = LayerMapping(District, districts_shp, districts_mapping, transform=True)
    lm.save(strict=True, verbose=verbose)

run_districts()