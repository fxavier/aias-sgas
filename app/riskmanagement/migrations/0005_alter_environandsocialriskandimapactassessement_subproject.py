# Generated by Django 5.0.13 on 2025-03-16 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riskmanagement', '0004_alter_environandsocialriskandimapactassessement_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environandsocialriskandimapactassessement',
            name='subproject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='riskmanagement.subproject'),
        ),
    ]
