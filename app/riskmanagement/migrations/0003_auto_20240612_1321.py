# Generated by Django 3.2.25 on 2024-06-12 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('riskmanagement', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='environandsocialriskandimapactassessement',
            options={'verbose_name': 'Environmental and Social Risk and Impact Assessement', 'verbose_name_plural': 'Environmental and Social Risks and Impact Assessements'},
        ),
        migrations.AlterModelOptions(
            name='environmentalsocialscreening',
            options={'verbose_name': 'Environmental and Social Screening Form (FR.AS.023)', 'verbose_name_plural': 'Environmental and Social Screening Forms (FR.AS.023)'},
        ),
        migrations.AddField(
            model_name='environmentalsocialscreening',
            name='screening_results',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='screening_results', to='riskmanagement.screeningresult'),
            preserve_default=False,
        ),
    ]