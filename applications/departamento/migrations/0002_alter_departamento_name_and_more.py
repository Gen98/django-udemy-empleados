# Generated by Django 4.0.3 on 2022-03-10 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(editable=False, max_length=50, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='short_name',
            field=models.CharField(blank=True, max_length=20, verbose_name='Nombre Corto'),
        ),
    ]
