# Generated by Django 3.1.4 on 2020-12-17 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_remove_project_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.project')),
            ],
        ),
    ]