# Generated by Django 4.1.2 on 2022-12-07 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('motor', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='autos')),
            ],
        ),
    ]