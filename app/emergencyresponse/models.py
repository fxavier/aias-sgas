from django.db import models
from riskmanagement.models import Department
from users.models import User
from riskmanagement.models import Subproject

 
def relatorio_incidente_file_path(instance, filename):
    return f'incidentes_files/{instance.number}/{filename}'




class TipoIncidente(models.TextChoices):
    HUMANO = 'Humano', 'Humano'
    SEGURANCA = 'Segurança', 'Segurança'
    INFRAESTRUTURAS = 'Infraestruturas', 'Infraestruturas'
    AMBIENTAL = 'Ambiental', 'Ambiental'
    SOCIAL = 'Social', 'Social'
    OUTROS = 'Outros', 'Outros'

class EnvoldidoOutroAcidente(models.TextChoices):
    SIM = 'Sim', 'Sim'
    NAO = 'Não', 'Não'

class RealizadaAnaliseRiscoImpactoAmbientalAntes(models.TextChoices):
    SIM = 'Sim', 'Sim'
    NAO = 'Não', 'Não'

class ExisteProcedimentoParaActividade(models.TextChoices):
    SIM = 'Sim', 'Sim'
    NAO = 'Não', 'Não'

class ColaboradorRecebeuTreinamento(models.TextChoices):
    SIM = 'Sim', 'Sim'
    NAO = 'Não', 'Não'

class NaturezaEExtensaoIncidente(models.TextChoices):
    INTOXICACAO_LEVE = 'Intoxicação leve', 'Intoxicação leve'
    INTOXICACAO_GRAVE = 'Intoxicação grave', 'Intoxicação grave'
    FERIMENTO_LEVE = 'Ferimento leve', 'Ferimento leve'
    FERIMENTO_GRAVE = 'Ferimento grave', 'Ferimento grave'
    MORTE = 'Morte', 'Morte'
    NENHUM = 'Nenhum', 'Nenhum'
    OUTROS = 'Outros', 'Outros'

class PossiveisCausasAcidenteMetodologia(models.TextChoices):
    FALTA_DE_PROCEDIMENTOS_PARA_ACTIVIDADE = 'Falta de procedimentos para actividade', 'Falta de procedimentos para actividade'
    FALHAS_NO_PROCEDIMENTO_EXISTENTE = 'Falhas no procedimento existente', 'Falhas no procedimento existente'
    FALTA_DE_PLANO_DE_TRABALHO = 'Falta de plano de trabalho', 'Falta de plano de trabalho'
    FALHA_NA_COMUNICACAO = 'Falha na comunicação', 'Falha na comunicação'
    OUTROS = 'Outros', 'Outros'

class PossiveisCausasAcidenteEquipamentos(models.TextChoices):
    FALHA_DE_EQUIPAMENTO = 'Falha de equipamento', 'Falha de equipamento'
    EQUIPAMENTO_INAPROPRIADO = 'Equipamento inapropriado', 'Equipamento inapropriado'
    FALHA_NA_PROTECCAO_DO_EQUIPAMENTO = 'Falha na protecção do equipamento', 'Falha na protecção do equipamento'
    FALHA_NA_SINALIZACAO = 'Falha na sinalização', 'Falha na sinalização'
    ESPACO_INAPROPRIADO_PARA_EQUIPAMENTO = 'Espaço inapropriado para equipamento', 'Espaço inapropriado para equipamento'
    OUTROS = 'Outros', 'Outros'

class PossiveisCausasAcidenteMaterial(models.TextChoices):
    FERRAMENTA_DEFEITUOSA = 'Ferramenta defeituosa', 'Ferramenta defeituosa'
    FALHA_NA_FERRAMENTA = 'Falha na ferramenta', 'Falha na ferramenta'
    FALTA_DE_INVENTARIO = 'Falta de inventário', 'Falta de inventário'
    EPI_INADEQUADO = 'EPI inadequado', 'EPI inadequado'
    OUTROS = 'Outros', 'Outros'

class PossiveisCausasAcidenteColaboradores(models.TextChoices):
    FALTA_DE_TREINAMENTO = 'Falta de treinamento', 'Falta de treinamento'
    NEGLIGENCIA_DO_COLABORADOR = 'Negligência do colaborador', 'Negligência do colaborador'
    NEGLIGENCIA_DO_OPERADOR_SAZONAL = 'Negligência do operador sazonal', 'Negligência do operador sazonal'
    NAO_CONCARDANCIA_COM_PROCEDIMENTOS = 'Não concordância com procedimentos', 'Não concordância com procedimentos'
    USO_INADEQUADO_DE_EQUIPAMENTO = 'Uso inadequado de equipamento', 'Uso inadequado de equipamento'
    OUTROS = 'Outros', 'Outros'
    
class PossiveisCausasAcidenteAmbienteESeguranca(models.TextChoices):
    AGENTES_PERIGOSOS = 'Agentes perigosos', 'Agentes perigosos'
    FALTA_DE_SINALIZACAO = 'Falta de sinalização', 'Falta de sinalização'
    PAVIMENTO_IRREGULAR = 'Pavimento irregular', 'Pavimento irregular'
    PAVIMENTO_ESCORREGADIO = 'Pavimento escorregadio', 'Pavimento escorregadio'
    OUTROS = 'Outros', 'Outros'

class PossiveisCausasAcidenteMedicoes(models.TextChoices):
    FALTA_NO_INSTRUMENTO_DE_MEDICAO = 'Falta no instrumento de medição', 'Falta no instrumento de medição'
    INSTRUMENTO_DE_AJUSTAMENTO_INADEQUADO = 'Instrumento de ajustamento inadequado', 'Instrumento de ajustamento inadequado'
    FALHA_NO_INSTRUMENTO_DE_CALIBRACAO = 'Falha no instrumento de calibração', 'Falha no instrumento de calibração'
    FALTA_DE_INSPENCAO = 'Falta de inspenção', 'Falta de inspenção'
    OUTROS = 'Outros', 'Outros'

class PessoaEnvolvida(models.Model):
    nome = models.CharField(max_length=255)
    departamento = models.ForeignKey(Department, on_delete=models.CASCADE)
    outras_informacoes = models.TextField()

    def __str__(self):
        return self.nome
    
class PessoasEnvolvidasNaInvestigacao(models.Model):
    nome = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    actividade = models.CharField(max_length=255)
    assinatura = models.CharField(max_length=255)
    data = models.DateField()
   

    def __str__(self):
        return self.nome
    
class AccoesImediatasECorrectivas(models.Model):
    accao = models.CharField(max_length=255)
    descricao = models.TextField()
    responsavel = models.CharField(max_length=255)
    data = models.DateField()
    assinatura = models.CharField(max_length=255)

    def __str__(self):
        return self.accao
    
class ObrasForamSuspensas(models.TextChoices):
    SIM = 'Sim', 'Sim'
    NAO = 'Não', 'Não'

class IncidenteEnvolveuEmpreteiro(models.TextChoices):
    SIM = 'Sim', 'Sim'
    NAO = 'Não', 'Não'

class RelatorioAcidenteIncidente(models.Model):
    nome = models.CharField(max_length=255)
    funcao = models.CharField(max_length=255)
    departamento = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    subprojecto = models.ForeignKey(Subproject, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField()
    hora = models.TimeField()
    local = models.CharField(max_length=255)
    actividade_em_curso = models.CharField(max_length=255)
    descricao_do_acidente = models.TextField()
    tipo_de_incidente = models.CharField(max_length=255, choices=TipoIncidente.choices)
    equipamento_envolvido = models.CharField(max_length=255)
    observacao = models.TextField()
    colaborador_envolvido_outro_acidente_antes = models.CharField(max_length=255, choices=EnvoldidoOutroAcidente.choices)
    realizada_analise_risco_impacto_ambiental_antes = models.CharField(max_length=255, choices=RealizadaAnaliseRiscoImpactoAmbientalAntes.choices)
    existe_procedimento_para_actividade = models.CharField(max_length=255, choices=ExisteProcedimentoParaActividade.choices)
    colaborador_recebeu_treinamento = models.CharField(max_length=255, choices=ColaboradorRecebeuTreinamento.choices)
    incidente_envolve_empreteiro = models.CharField(max_length=255, choices=IncidenteEnvolveuEmpreteiro.choices)
    nome_comercial_empreteiro = models.CharField(max_length=255, null=True, blank=True)
    natureza_e_extensao_incidente = models.CharField(max_length=255, choices=NaturezaEExtensaoIncidente.choices)
    possiveis_causas_acidente_metodologia = models.CharField(max_length=255, choices=PossiveisCausasAcidenteMetodologia.choices)
    possiveis_causas_acidente_equipamentos = models.CharField(max_length=255, choices=PossiveisCausasAcidenteEquipamentos.choices)
    possiveis_causas_acidente_material = models.CharField(max_length=255, choices=PossiveisCausasAcidenteMaterial.choices)
    possiveis_causas_acidente_colaboradores = models.CharField(max_length=255, choices=PossiveisCausasAcidenteColaboradores.choices)
    possiveis_causas_acidente_ambiente_e_seguranca = models.CharField(max_length=255, choices=PossiveisCausasAcidenteAmbienteESeguranca.choices)
    possiveis_causas_acidente_medicoes = models.CharField(max_length=255, choices=PossiveisCausasAcidenteMedicoes.choices)
    pessoa_envolvida = models.ForeignKey(PessoaEnvolvida, on_delete=models.CASCADE)
    pessoas_envolvidas_na_investigacao = models.ManyToManyField(PessoasEnvolvidasNaInvestigacao)
    accoes_imediatas_e_correctivas = models.ManyToManyField(AccoesImediatasECorrectivas)
    fotografia_frontal = models.ImageField(upload_to='documents/', null=True, blank=True)
    fotografia_posterior = models.ImageField(upload_to="documents/", null=True, blank=True)
    fotografia_lateral_direita = models.ImageField(upload_to="documents/", null=True, blank=True)
    fotografia_lateral_esquerda = models.ImageField(upload_to="documents/", null=True, blank=True)
    fotografia_do_melhor_angulo = models.ImageField(upload_to="documents/", null=True, blank=True)
    fotografia = models.ImageField(upload_to="documents/", null=True, blank=True)
   #  criado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'FR.AS.009_RELATÓRIO DE INCIDENTE'
        verbose_name_plural = 'FR.AS.009_RELATÓRIOS DE INCIDENTE'
   

    def __str__(self):
        return self.local
    

class ListaVerificacaoKitPrimeirosSocorros(models.Model):
    descricao = models.TextField()
    quantidade = models.IntegerField()
    data = models.DateField()
    prazo = models.DateField()
    observacao = models.TextField()
    inspecao_realizada_por = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'FR.AS.011 LISTA DE VERIFICAÇÃO KIT DE PRIMEIROS SOCORROS'
        verbose_name_plural = 'FR.AS.011 LISTAS DE VERIFICAÇÃO KIT DE PRIMEIROS SOCORROS'

    def __str__(self):
        return self.descricao


class Incidents(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    
class Type(models.TextChoices):
    Employee = 'Employee'
    SubContrator = 'Subcontrator'

class FurtherInvestigatioRequired(models.TextChoices):
    Yes = 'Yes'
    No = 'No'


    
class IncidentFlashReport(models.Model):
    incidents = models.ManyToManyField(Incidents)
    date_incident = models.DateField()
    time_incident = models.TimeField()
    section = models.CharField(max_length=100, null=True, blank=True)
    location_incident = models.CharField(max_length=255)
    date_reported = models.DateField()
    supervisor = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=Type.choices)
    employee_name = models.CharField(max_length=100, null=True, blank=True)
    subcontrator_name = models.CharField(max_length=100, null=True, blank=True)
    incident_description = models.TextField()
    details_of_injured_person = models.TextField()
    witness_statement = models.TextField(null=True, blank=True)
    preliminary_findings = models.CharField(max_length=255, null=True, blank=True)
    recomendations = models.TextField()
    further_investigation_required = models.CharField(max_length=100, choices=FurtherInvestigatioRequired.choices)
    incident_reportable = models.CharField(max_length=100, choices=FurtherInvestigatioRequired.choices)
    lenders_to_be_notified = models.CharField(max_length=100, choices=FurtherInvestigatioRequired.choices)
    author_of_report = models.CharField(max_length=10)
    date_created = models.DateField(auto_now_add=True)
    approver_name = models.CharField(max_length=100)
    date_approved = models.DateField()
    

    class Meta:
        verbose_name = 'FR.AS.028_Incident Flash Report'
        verbose_name_plural = 'FR.AS.028_Incident Flash Reports'

    def __str__(self):  
        return self.location_incident
























































































