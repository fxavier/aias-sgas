# Generated by Django 3.2.25 on 2024-06-16 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riskmanagement', '0004_environmentalsocialscreening_consultation_and_engagement'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='environandsocialriskandimapactassessement',
            options={'verbose_name': 'Environmental and Social Risk and Impact Assessement (FR.AS.002)', 'verbose_name_plural': 'Environmental and Social Risks and Impact Assessements (FR.AS.002)'},
        ),
        migrations.AlterModelOptions(
            name='legalrequirementcontrol',
            options={'verbose_name': 'Legal Requirement Control (FR.AS.003)', 'verbose_name_plural': 'Legal Requirements Control (FR.AS.003)'},
        ),
        migrations.AlterModelOptions(
            name='preliminaryenvironmentalinformation',
            options={'verbose_name': 'Preliminary Environmental Information Form (MOD.AS.02)', 'verbose_name_plural': 'Preliminary Environmental Information Forms (MOD.AS.02)'},
        ),
    ]
