# Generated by Django 3.1.4 on 2020-12-18 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20201217_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='avatar',
        ),
    ]
