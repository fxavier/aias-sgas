# Generated by Django 5.0.13 on 2025-03-16 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizationalcapacityandcompetency', '0004_alter_ohsacting_options_and_more'),
        ('riskmanagement', '0005_alter_environandsocialriskandimapactassessement_subproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingneeds',
            name='subproject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='riskmanagement.subproject'),
        ),
    ]
