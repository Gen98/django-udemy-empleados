# Generated by Django 4.0.3 on 2022-03-16 00:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0003_empleado_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='curriculum',
            field=ckeditor.fields.RichTextField(default='texto'),
            preserve_default=False,
        ),
    ]