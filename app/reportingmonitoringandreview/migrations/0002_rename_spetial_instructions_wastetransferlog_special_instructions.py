# Generated by Django 3.2.25 on 2024-07-31 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportingmonitoringandreview', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wastetransferlog',
            old_name='spetial_instructions',
            new_name='special_instructions',
        ),
    ]
