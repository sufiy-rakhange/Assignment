# Generated by Django 3.1.4 on 2020-12-16 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20201216_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects/avatar'),
        ),
    ]