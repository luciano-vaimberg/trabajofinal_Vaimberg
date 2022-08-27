# Generated by Django 4.1 on 2022-08-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('genero', models.CharField(max_length=25)),
                ('edad', models.IntegerField()),
                ('documento', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=50)),
                ('localidad', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('sueldo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SociosPlenos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('genero', models.CharField(max_length=25)),
                ('edad', models.IntegerField()),
                ('documento', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=50)),
                ('localidad', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('numero_socio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SociosSemiPlenos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('genero', models.CharField(max_length=25)),
                ('edad', models.IntegerField()),
                ('documento', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=50)),
                ('localidad', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('numero_socio', models.IntegerField()),
            ],
        ),
    ]