# Generated by Django 4.1 on 2022-09-18 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppVelez', '0009_avatar_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='imagen',
            new_name='imagen_avatar',
        ),
    ]
