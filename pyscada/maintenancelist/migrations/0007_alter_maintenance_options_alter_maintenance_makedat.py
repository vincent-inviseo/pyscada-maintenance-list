# Generated by Django 4.2.3 on 2023-12-05 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenancelist', '0006_remove_maintenancedevice_isconform_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maintenance',
            options={'ordering': ['-makedAt']},
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='makedAt',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Make at'),
        ),
    ]
