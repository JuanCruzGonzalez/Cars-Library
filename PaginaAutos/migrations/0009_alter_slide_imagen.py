# Generated by Django 4.1.2 on 2023-02-07 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaAutos', '0008_slide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='imagen',
            field=models.ImageField(upload_to='slides'),
        ),
    ]
