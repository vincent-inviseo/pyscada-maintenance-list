# Generated by Django 4.2.3 on 2023-11-02 10:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceDeviceType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50, verbose_name='Type of device')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceDevice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reference', models.CharField(blank=True, max_length=50, null=True, verbose_name='Reference')),
                ('name', models.CharField(max_length=100, verbose_name='Title')),
                ('createdAt', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created at')),
                ('updatedAt', models.TextField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Updated at')),
                ('period', models.CharField(choices=[('every month', 'every month'), ('each 3 months', 'each 3 months'), ('each 4 months', 'each 4 months'), ('each year', 'each year'), ('every 2 years', 'every 2 years')], max_length=50, verbose_name='Select maintenance period')),
                ('lastMaintenance', models.DateTimeField(blank=True, null=True, verbose_name='Date last maintenance')),
                ('isConform', models.BooleanField(verbose_name='Device is conform after control')),
                ('report', models.CharField(blank=True, max_length=150, null=True, verbose_name='report url join')),
                ('maintainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='maintenancelist.maintenancedevicetype')),
            ],
            options={
                'ordering': ['-createdAt'],
            },
        ),
    ]
