# Generated by Django 4.2.6 on 2023-10-23 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_slip_current_boat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slip',
            name='current_boat',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
