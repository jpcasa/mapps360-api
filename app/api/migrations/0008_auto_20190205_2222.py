# Generated by Django 2.1.5 on 2019-02-05 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_floorplan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floorplan',
            name='plan',
            field=models.ImageField(upload_to='properties/floor_plans/'),
        ),
    ]
