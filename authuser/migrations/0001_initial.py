# Generated by Django 4.1.7 on 2023-07-18 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField(blank=True, null=True)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField(blank=True, null=True)),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('id_employee', models.OneToOneField(db_column='id_employee', on_delete=django.db.models.deletion.DO_NOTHING, to='employees.employee')),
            ],
            options={
                'verbose_name_plural': 'auth_users',
            },
        ),
    ]
