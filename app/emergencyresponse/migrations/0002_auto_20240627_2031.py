# Generated by Django 3.2.25 on 2024-06-27 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emergencyresponse', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relatorioacidenteincidente',
            options={'verbose_name': 'FR.AS.009_RELATÓRIO DE INCIDENTE', 'verbose_name_plural': 'FR.AS.009_RELATÓRIOS DE INCIDENTE'},
        ),
        migrations.AddField(
            model_name='relatorioacidenteincidente',
            name='incidente_envolve_empreteiro',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relatorioacidenteincidente',
            name='nome_comercial_empreteiro',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ListaVerificacaoKitPrimeirosSocorros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('quantidade', models.IntegerField()),
                ('data', models.DateField()),
                ('prazo', models.DateField()),
                ('observacao', models.TextField()),
                ('inspecao_realizada_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'FR.AS.011 LISTA DE VERIFICAÇÃO KIT DE PRIMEIROS SOCORROS',
                'verbose_name_plural': 'FR.AS.011 LISTAS DE VERIFICAÇÃO KIT DE PRIMEIROS SOCORROS',
            },
        ),
    ]
