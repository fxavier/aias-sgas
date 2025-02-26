# Generated by Django 4.2.19 on 2025-02-23 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('riskmanagement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emergencyresponse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatorioacidenteincidente',
            name='criado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='relatorioacidenteincidente',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riskmanagement.department'),
        ),
        migrations.AddField(
            model_name='relatorioacidenteincidente',
            name='pessoa_envolvida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergencyresponse.pessoaenvolvida'),
        ),
        migrations.AddField(
            model_name='relatorioacidenteincidente',
            name='pessoas_envolvidas_na_investigacao',
            field=models.ManyToManyField(to='emergencyresponse.pessoasenvolvidasnainvestigacao'),
        ),
        migrations.AddField(
            model_name='pessoaenvolvida',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riskmanagement.department'),
        ),
        migrations.AddField(
            model_name='listaverificacaokitprimeirossocorros',
            name='inspecao_realizada_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='incidentflashreport',
            name='incidents',
            field=models.ManyToManyField(to='emergencyresponse.incidents'),
        ),
    ]
