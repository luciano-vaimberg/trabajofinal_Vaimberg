# Generated by Django 4.1 on 2022-08-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppVelez', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleados',
            name='legajo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]