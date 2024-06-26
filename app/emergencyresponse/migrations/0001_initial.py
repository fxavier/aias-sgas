# Generated by Django 3.2.25 on 2024-06-27 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import emergencyresponse.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('riskmanagement', '0006_alter_legalrequirementcontrol_law_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccoesImediatasECorrectivas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accao', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('responsavel', models.CharField(max_length=255)),
                ('data', models.DateField()),
                ('assinatura', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PessoaEnvolvida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('outras_informacoes', models.TextField()),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riskmanagement.department')),
            ],
        ),
        migrations.CreateModel(
            name='PessoasEnvolvidasNaInvestigacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('empresa', models.CharField(max_length=255)),
                ('actividade', models.CharField(max_length=255)),
                ('assinatura', models.CharField(max_length=255)),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RelatorioAcidenteIncidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('funcao', models.CharField(max_length=255)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('local', models.CharField(max_length=255)),
                ('actividade_em_curso', models.CharField(max_length=255)),
                ('descricao_acidente', models.TextField()),
                ('tipo_incidente', models.CharField(choices=[('Humano', 'Humano'), ('Segurança', 'Segurança'), ('Infraestruturas', 'Infraestruturas'), ('Ambiental', 'Ambiental'), ('Social', 'Social'), ('Outros', 'Outros')], max_length=255)),
                ('equipamento_envolvido', models.CharField(max_length=255)),
                ('observacao', models.TextField()),
                ('colaborador_envolvido_outro_acidente_antes', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=255)),
                ('realizada_analise_risco_impacto_ambiental_antes', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=255)),
                ('existe_procedimento_para_actividade', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=255)),
                ('colaborador_recebeu_treinamento', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=255)),
                ('natureza_e_extensao_incidente', models.CharField(choices=[('Intoxicação leve', 'Intoxicação leve'), ('Intoxicação grave', 'Intoxicação grave'), ('Ferimento leve', 'Ferimento leve'), ('Ferimento grave', 'Ferimento grave'), ('Morte', 'Morte'), ('Nenhum', 'Nenhum'), ('Outros', 'Outros')], max_length=255)),
                ('possiveis_causas_acidente_metodologia', models.CharField(choices=[('Falta de procedimentos para actividade', 'Falta de procedimentos para actividade'), ('Falhas no procedimento existente', 'Falhas no procedimento existente'), ('Falta de plano de trabalho', 'Falta de plano de trabalho'), ('Falha na comunicação', 'Falha na comunicação'), ('Outros', 'Outros')], max_length=255)),
                ('possiveis_causas_acidente_equipamentos', models.CharField(choices=[('Falha de equipamento', 'Falha de equipamento'), ('Equipamento inapropriado', 'Equipamento inapropriado'), ('Falha na protecção do equipamento', 'Falha na protecção do equipamento'), ('Falha na sinalização', 'Falha na sinalização'), ('Espaço inapropriado para equipamento', 'Espaço inapropriado para equipamento'), ('Outros', 'Outros')], max_length=255)),
                ('possiveis_causas_acidente_material', models.CharField(choices=[('Ferramenta defeituosa', 'Ferramenta defeituosa'), ('Falha na ferramenta', 'Falha na ferramenta'), ('Falta de inventário', 'Falta de inventário'), ('EPI inadequado', 'EPI inadequado'), ('Outros', 'Outros')], max_length=255)),
                ('possiveis_causas_acidente_colaboradores', models.CharField(choices=[('Falta de treinamento', 'Falta de treinamento'), ('Negligência do colaborador', 'Negligência do colaborador'), ('Negligência do operador sazonal', 'Negligência do operador sazonal'), ('Não concordância com procedimentos', 'Não concordância com procedimentos'), ('Uso inadequado de equipamento', 'Uso inadequado de equipamento'), ('Outros', 'Outros')], max_length=255)),
                ('possiveis_causas_acidente_ambiente_e_seguranca', models.CharField(choices=[('Agentes perigosos', 'Agentes perigosos'), ('Falta de sinalização', 'Falta de sinalização'), ('Pavimento irregular', 'Pavimento irregular'), ('Pavimento escorregadio', 'Pavimento escorregadio'), ('Outros', 'Outros')], max_length=255)),
                ('possiveis_causas_acidente_medicoes', models.CharField(choices=[('Falta no instrumento de medição', 'Falta no instrumento de medição'), ('Instrumento de ajustamento inadequado', 'Instrumento de ajustamento inadequado'), ('Falha no instrumento de calibração', 'Falha no instrumento de calibração'), ('Falta de inspenção', 'Falta de inspenção'), ('Outros', 'Outros')], max_length=255)),
                ('fotografia_frontal', models.ImageField(blank=True, null=True, upload_to=emergencyresponse.models.relatorio_incidente_file_path)),
                ('fotografia_posterior', models.ImageField(blank=True, null=True, upload_to=emergencyresponse.models.relatorio_incidente_file_path)),
                ('fotografia_lateral_direita', models.ImageField(blank=True, null=True, upload_to=emergencyresponse.models.relatorio_incidente_file_path)),
                ('fotografia_lateral_esquerda', models.ImageField(blank=True, null=True, upload_to=emergencyresponse.models.relatorio_incidente_file_path)),
                ('fotografia_do_melhor_angulo', models.ImageField(blank=True, null=True, upload_to=emergencyresponse.models.relatorio_incidente_file_path)),
                ('fotografia', models.ImageField(blank=True, null=True, upload_to=emergencyresponse.models.relatorio_incidente_file_path)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('accoes_imediatas_e_correctivas', models.ManyToManyField(to='emergencyresponse.AccoesImediatasECorrectivas')),
                ('criado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riskmanagement.department')),
                ('pessoa_envolvida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergencyresponse.pessoaenvolvida')),
                ('pessoas_envolvidas_na_investigacao', models.ManyToManyField(to='emergencyresponse.PessoasEnvolvidasNaInvestigacao')),
            ],
        ),
    ]
