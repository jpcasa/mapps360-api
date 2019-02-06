# Generated by Django 2.1.5 on 2019-02-06 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20190205_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.Address'),
        ),
        migrations.AddField(
            model_name='property',
            name='ammenities',
            field=models.ManyToManyField(to='api.Ammenity'),
        ),
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]