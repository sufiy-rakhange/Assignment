# Generated by Django 3.1.4 on 2020-12-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20201217_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='enddate',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='startdate',
            field=models.CharField(max_length=100),
        ),
    ]