# Generated by Django 4.1.7 on 2023-07-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id_department', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id_employee', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('job_title', models.CharField(blank=True, max_length=200, null=True)),
                ('date_added', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
