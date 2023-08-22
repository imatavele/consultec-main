# Generated by Django 4.1.7 on 2023-08-17 18:12

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField()),
                ('perimeter', models.FloatField()),
                ('distrito', models.CharField(max_length=30)),
                ('provincia', models.CharField(max_length=30)),
                ('posto', models.CharField(max_length=30)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]