# Generated by Django 5.0.4 on 2024-04-29 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('estudiante', models.ManyToManyField(to='Clase.estudiante')),
                ('profesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Clase.profesor')),
            ],
        ),
    ]
