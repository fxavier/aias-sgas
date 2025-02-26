# Generated by Django 4.2.19 on 2025-02-23 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('riskmanagement', '0001_initial'),
        ('organizationalcapacityandcompetency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingneeds',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riskmanagement.department'),
        ),
        migrations.AddField(
            model_name='trainingmatrix',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizationalcapacityandcompetency.position'),
        ),
        migrations.AddField(
            model_name='trainingmatrix',
            name='toolbox_talks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizationalcapacityandcompetency.toolboxtalks'),
        ),
        migrations.AddField(
            model_name='trainingmatrix',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizationalcapacityandcompetency.training'),
        ),
        migrations.AddField(
            model_name='trainingeffectivnessassessment',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riskmanagement.department'),
        ),
        migrations.AddField(
            model_name='trainingeffectivnessassessment',
            name='training_evaluation_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizationalcapacityandcompetency.trainingevaluationquestions'),
        ),
        migrations.AddField(
            model_name='ohsacting',
            name='acceptance_confirmation',
            field=models.ManyToManyField(to='organizationalcapacityandcompetency.acceptanceconfirmation'),
        ),
    ]
