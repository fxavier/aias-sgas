import graphene
from graphene_django import DjangoObjectType
from graphene import Date, Time, Int, String, List
from graphene_file_upload.scalars import Upload

# Import your models and their TextChoices
from .models import (
    PessoaEnvolvida,
    PessoasEnvolvidasNaInvestigacao,
    AccoesImediatasECorrectivas,
    RelatorioAcidenteIncidente,
    ListaVerificacaoKitPrimeirosSocorros,
    Incidents,
    IncidentFlashReport,
    TipoIncidente,
    EnvoldidoOutroAcidente,
    RealizadaAnaliseRiscoImpactoAmbientalAntes,
    ExisteProcedimentoParaActividade,
    ColaboradorRecebeuTreinamento,
    NaturezaEExtensaoIncidente,
    PossiveisCausasAcidenteMetodologia,
    PossiveisCausasAcidenteEquipamentos,
    PossiveisCausasAcidenteMaterial,
    PossiveisCausasAcidenteColaboradores,
    PossiveisCausasAcidenteAmbienteESeguranca,
    PossiveisCausasAcidenteMedicoes,
    ObrasForamSuspensas,
    IncidenteEnvolveuEmpreteiro,
    Type,
    FurtherInvestigatioRequired,
    Department
)

from users.models import User

# Create Graphene enums from your Django TextChoices
TipoIncidenteEnum = graphene.Enum.from_enum(TipoIncidente)
EnvoldidoOutroAcidenteEnum = graphene.Enum.from_enum(EnvoldidoOutroAcidente)
RealizadaAnaliseRiscoImpactoAmbientalAntesEnum = graphene.Enum.from_enum(RealizadaAnaliseRiscoImpactoAmbientalAntes)
ExisteProcedimentoParaActividadeEnum = graphene.Enum.from_enum(ExisteProcedimentoParaActividade)
ColaboradorRecebeuTreinamentoEnum = graphene.Enum.from_enum(ColaboradorRecebeuTreinamento)
NaturezaEExtensaoIncidenteEnum = graphene.Enum.from_enum(NaturezaEExtensaoIncidente)
PossiveisCausasAcidenteMetodologiaEnum = graphene.Enum.from_enum(PossiveisCausasAcidenteMetodologia)
PossiveisCausasAcidenteEquipamentosEnum = graphene.Enum.from_enum(PossiveisCausasAcidenteEquipamentos)
PossiveisCausasAcidenteMaterialEnum = graphene.Enum.from_enum(PossiveisCausasAcidenteMaterial)
PossiveisCausasAcidenteColaboradoresEnum = graphene.Enum.from_enum(PossiveisCausasAcidenteColaboradores)
PossiveisCausasAcidenteAmbienteESegurancaEnum = graphene.Enum.from_enum(PossiveisCausasAcidenteAmbienteESeguranca)
PossiveisCausasAcidenteMedicoesEnum = graphene.Enum.from_enum(PossiveisCausasAcidenteMedicoes)
ObrasForamSuspensasEnum = graphene.Enum.from_enum(ObrasForamSuspensas)
IncidenteEnvolveuEmpreteiroEnum = graphene.Enum.from_enum(IncidenteEnvolveuEmpreteiro)
TypeEnum = graphene.Enum.from_enum(Type)
FurtherInvestigatioRequiredEnum = graphene.Enum.from_enum(FurtherInvestigatioRequired)

# -------------------------
# Graphene Types for Models
# -------------------------

class PessoaEnvolvidaNode(DjangoObjectType):
    class Meta:
        model = PessoaEnvolvida
        fields = '__all__'

class PessoasEnvolvidasNaInvestigacaoNode(DjangoObjectType):
    class Meta:
        model = PessoasEnvolvidasNaInvestigacao
        fields = '__all__'

class AccoesImediatasECorrectivasNode(DjangoObjectType):
    class Meta:
        model = AccoesImediatasECorrectivas
        fields = '__all__'

class RelatorioAcidenteIncidenteNode(DjangoObjectType):
    class Meta:
        model = RelatorioAcidenteIncidente
        fields = '__all__'

class ListaVerificacaoKitPrimeirosSocorrosNode(DjangoObjectType):
    class Meta:
        model = ListaVerificacaoKitPrimeirosSocorros
        fields = '__all__'

class IncidentsNode(DjangoObjectType):
    class Meta:
        model = Incidents
        fields = '__all__'

class IncidentFlashReportNode(DjangoObjectType):
    class Meta:
        model = IncidentFlashReport
        fields = '__all__'

# -------------------------
# Queries
# -------------------------

class Query(graphene.ObjectType):
    all_pessoas_envolvidas = graphene.List(PessoaEnvolvidaNode)
    all_relatorios_incidente = graphene.List(RelatorioAcidenteIncidenteNode)
    all_lista_verificacao = graphene.List(ListaVerificacaoKitPrimeirosSocorrosNode)
    all_incidents = graphene.List(IncidentsNode)
    all_incident_flash_reports = graphene.List(IncidentFlashReportNode)

    pessoa_envolvida = graphene.Field(PessoaEnvolvidaNode, id=Int(required=True))
    relatorio_incidente = graphene.Field(RelatorioAcidenteIncidenteNode, id=Int(required=True))
    lista_verificacao = graphene.Field(ListaVerificacaoKitPrimeirosSocorrosNode, id=Int(required=True))
    incident = graphene.Field(IncidentsNode, id=Int(required=True))
    incident_flash_report = graphene.Field(IncidentFlashReportNode, id=Int(required=True))

    def resolve_all_pessoas_envolvidas(root, info):
        return PessoaEnvolvida.objects.all()

    def resolve_all_relatorios_incidente(root, info):
        return RelatorioAcidenteIncidente.objects.all()

    def resolve_all_lista_verificacao(root, info):
        return ListaVerificacaoKitPrimeirosSocorros.objects.all()

    def resolve_all_incidents(root, info):
        return Incidents.objects.all()

    def resolve_all_incident_flash_reports(root, info):
        return IncidentFlashReport.objects.all()

    def resolve_pessoa_envolvida(root, info, id):
        try:
            return PessoaEnvolvida.objects.get(pk=id)
        except PessoaEnvolvida.DoesNotExist:
            return None

    def resolve_relatorio_incidente(root, info, id):
        try:
            return RelatorioAcidenteIncidente.objects.get(pk=id)
        except RelatorioAcidenteIncidente.DoesNotExist:
            return None

    def resolve_lista_verificacao(root, info, id):
        try:
            return ListaVerificacaoKitPrimeirosSocorros.objects.get(pk=id)
        except ListaVerificacaoKitPrimeirosSocorros.DoesNotExist:
            return None

    def resolve_incident(root, info, id):
        try:
            return Incidents.objects.get(pk=id)
        except Incidents.DoesNotExist:
            return None

    def resolve_incident_flash_report(root, info, id):
        try:
            return IncidentFlashReport.objects.get(pk=id)
        except IncidentFlashReport.DoesNotExist:
            return None

# -------------------------
# Mutations
# -------------------------

# Mutation for RelatorioAcidenteIncidente with many-to-many and file uploads.
class CreateRelatorioAcidenteIncidente(graphene.Mutation):
    class Arguments:
        # Required fields
        nome = String(required=True)
        funcao = String(required=True)
        departamento_id = Int(required=True)
        data = Date(required=True)
        hora = Time(required=True)
        local = String(required=True)
        actividade_em_curso = String(required=True)
        descricao_do_acidente = String(required=True)
        tipo_de_incidente = TipoIncidenteEnum(required=True)
        equipamento_envolvido = String(required=True)
        observacao = String(required=True)
        colaborador_envolvido_outro_acidente_antes = EnvoldidoOutroAcidenteEnum(required=True)
        realizada_analise_risco_impacto_ambiental_antes = RealizadaAnaliseRiscoImpactoAmbientalAntesEnum(required=True)
        existe_procedimento_para_actividade = ExisteProcedimentoParaActividadeEnum(required=True)
        colaborador_recebeu_treinamento = ColaboradorRecebeuTreinamentoEnum(required=True)
        incidente_envolve_empreteiro = IncidenteEnvolveuEmpreteiroEnum(required=True)
        nome_comercial_empreteiro = String()
        natureza_e_extensao_incidente = NaturezaEExtensaoIncidenteEnum(required=True)
        possiveis_causas_acidente_metodologia = PossiveisCausasAcidenteMetodologiaEnum(required=True)
        possiveis_causas_acidente_equipamentos = PossiveisCausasAcidenteEquipamentosEnum(required=True)
        possiveis_causas_acidente_material = PossiveisCausasAcidenteMaterialEnum(required=True)
        possiveis_causas_acidente_colaboradores = PossiveisCausasAcidenteColaboradoresEnum(required=True)
        possiveis_causas_acidente_ambiente_e_seguranca = PossiveisCausasAcidenteAmbienteESegurancaEnum(required=True)
        possiveis_causas_acidente_medicoes = PossiveisCausasAcidenteMedicoesEnum(required=True)
        pessoa_envolvida_id = Int(required=True)
        criado_por_id = Int(required=True)
        # Many-to-many fields (as list of IDs)
        pessoas_envolvidas_na_investigacao_ids = List(Int)
        accoes_imediatas_e_correctivas_ids = List(Int)
        # File upload fields (optional)
        fotografia_frontal = Upload()
        fotografia_posterior = Upload()
        fotografia_lateral_direita = Upload()
        fotografia_lateral_esquerda = Upload()
        fotografia_do_melhor_angulo = Upload()
        fotografia = Upload()

    relatorio = graphene.Field(RelatorioAcidenteIncidenteNode)

    def mutate(self, info, **kwargs):
        # Import foreign key models
        from riskmanagement.models import Department
        from users.models import User

        try:
            departamento = Department.objects.get(pk=kwargs.pop("departamento_id"))
        except Department.DoesNotExist:
            raise Exception("Department not found")

        try:
            pessoa_envolvida = PessoaEnvolvida.objects.get(pk=kwargs.pop("pessoa_envolvida_id"))
        except PessoaEnvolvida.DoesNotExist:
            raise Exception("PessoaEnvolvida not found")

        try:
            criado_por = User.objects.get(pk=kwargs.pop("criado_por_id"))
        except User.DoesNotExist:
            raise Exception("User not found")

        # Pop many-to-many fields and file uploads from kwargs
        pessoas_ids = kwargs.pop("pessoas_envolvidas_na_investigacao_ids", [])
        accoes_ids = kwargs.pop("accoes_imediatas_e_correctivas_ids", [])

        fotografia_frontal = kwargs.pop("fotografia_frontal", None)
        fotografia_posterior = kwargs.pop("fotografia_posterior", None)
        fotografia_lateral_direita = kwargs.pop("fotografia_lateral_direita", None)
        fotografia_lateral_esquerda = kwargs.pop("fotografia_lateral_esquerda", None)
        fotografia_do_melhor_angulo = kwargs.pop("fotografia_do_melhor_angulo", None)
        fotografia = kwargs.pop("fotografia", None)

        # Create the relatorio instance with remaining fields
        relatorio = RelatorioAcidenteIncidente.objects.create(
            departamento=departamento,
            pessoa_envolvida=pessoa_envolvida,
            criado_por=criado_por,
            **kwargs
        )

        # Assign file fields if provided
        if fotografia_frontal:
            relatorio.fotografia_frontal = fotografia_frontal
        if fotografia_posterior:
            relatorio.fotografia_posterior = fotografia_posterior
        if fotografia_lateral_direita:
            relatorio.fotografia_lateral_direita = fotografia_lateral_direita
        if fotografia_lateral_esquerda:
            relatorio.fotografia_lateral_esquerda = fotografia_lateral_esquerda
        if fotografia_do_melhor_angulo:
            relatorio.fotografia_do_melhor_angulo = fotografia_do_melhor_angulo
        if fotografia:
            relatorio.fotografia = fotografia
        relatorio.save()

        # Set many-to-many relationships if IDs were provided
        if pessoas_ids:
            investigation_objs = PessoasEnvolvidasNaInvestigacao.objects.filter(pk__in=pessoas_ids)
            relatorio.pessoas_envolvidas_na_investigacao.set(investigation_objs)
        if accoes_ids:
            correctivas_objs = AccoesImediatasECorrectivas.objects.filter(pk__in=accoes_ids)
            relatorio.accoes_imediatas_e_correctivas.set(correctivas_objs)

        return CreateRelatorioAcidenteIncidente(relatorio=relatorio)

class UpdateRelatorioAcidenteIncidente(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        # For simplicity, only a few fields are updatable here.
        nome = String()
        funcao = String()
        local = String()
        # You can add file upload fields and many-to-many updates similarly.
    relatorio = graphene.Field(RelatorioAcidenteIncidenteNode)

    def mutate(self, info, id, **kwargs):
        try:
            relatorio = RelatorioAcidenteIncidente.objects.get(pk=id)
        except RelatorioAcidenteIncidente.DoesNotExist:
            raise Exception("RelatorioAcidenteIncidente not found")
        for key, value in kwargs.items():
            setattr(relatorio, key, value)
        relatorio.save()
        return UpdateRelatorioAcidenteIncidente(relatorio=relatorio)

class DeleteRelatorioAcidenteIncidente(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            relatorio = RelatorioAcidenteIncidente.objects.get(pk=id)
        except RelatorioAcidenteIncidente.DoesNotExist:
            raise Exception("RelatorioAcidenteIncidente not found")
        relatorio.delete()
        return DeleteRelatorioAcidenteIncidente(ok=True)

# Sample mutation for IncidentFlashReport (without many-to-many file uploads)
class CreateIncidentFlashReport(graphene.Mutation):
    class Arguments:
        incidents_ids = List(Int, required=True)
        date_incident = Date(required=True)
        time_incident = Time(required=True)
        section = String()
        location_incident = String(required=True)
        date_reported = Date(required=True)
        supervisor = String(required=True)
        type = TypeEnum(required=True)
        employee_name = String()
        subcontrator_name = String()
        incident_description = String(required=True)
        details_of_injured_person = String(required=True)
        witness_statement = String()
        preliminary_findings = String()
        recomendations = String(required=True)
        further_investigation_required = FurtherInvestigatioRequiredEnum(required=True)
        incident_reportable = FurtherInvestigatioRequiredEnum(required=True)
        lenders_to_be_notified = FurtherInvestigatioRequiredEnum(required=True)
        author_of_report = String(required=True)
        approver_name = String(required=True)
        date_approved = Date(required=True)

    incident_flash_report = graphene.Field(IncidentFlashReportNode)

    def mutate(self, info, incidents_ids, **kwargs):
        incident_objs = Incidents.objects.filter(pk__in=incidents_ids)
        if not incident_objs.exists():
            raise Exception("No valid incidents found")
        flash_report = IncidentFlashReport.objects.create(**kwargs)
        flash_report.incidents.set(incident_objs)
        flash_report.save()
        return CreateIncidentFlashReport(incident_flash_report=flash_report)

class UpdateIncidentFlashReport(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        location_incident = String()
        supervisor = String()
        recomendations = String()
    incident_flash_report = graphene.Field(IncidentFlashReportNode)

    def mutate(self, info, id, **kwargs):
        try:
            report = IncidentFlashReport.objects.get(pk=id)
        except IncidentFlashReport.DoesNotExist:
            raise Exception("IncidentFlashReport not found")
        for key, value in kwargs.items():
            setattr(report, key, value)
        report.save()
        return UpdateIncidentFlashReport(incident_flash_report=report)

class DeleteIncidentFlashReport(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            report = IncidentFlashReport.objects.get(pk=id)
        except IncidentFlashReport.DoesNotExist:
            raise Exception("IncidentFlashReport not found")
        report.delete()
        return DeleteIncidentFlashReport(ok=True)
    
class CreatePessoaEnvolvida(graphene.Mutation):
    class Arguments:
        nome = String(required=True)
        departamento_id = Int(required=True)
        outras_informacoes = String(required=True)

    pessoa = graphene.Field(PessoaEnvolvidaNode)

    def mutate(self, info, nome, departamento_id, outras_informacoes):
        try:
            department = Department.objects.get(pk=departamento_id)
        except Department.DoesNotExist:
            raise Exception("Department not found")
        pessoa = PessoaEnvolvida.objects.create(
            nome=nome,
            departamento=department,
            outras_informacoes=outras_informacoes
        )
        return CreatePessoaEnvolvida(pessoa=pessoa)

class UpdatePessoaEnvolvida(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        nome = String()
        departamento_id = Int()
        outras_informacoes = String()

    pessoa = graphene.Field(PessoaEnvolvidaNode)

    def mutate(self, info, id, nome=None, departamento_id=None, outras_informacoes=None):
        try:
            pessoa = PessoaEnvolvida.objects.get(pk=id)
        except PessoaEnvolvida.DoesNotExist:
            raise Exception("PessoaEnvolvida not found")
        if nome is not None:
            pessoa.nome = nome
        if departamento_id is not None:
            try:
                department = Department.objects.get(pk=departamento_id)
            except Department.DoesNotExist:
                raise Exception("Department not found")
            pessoa.departamento = department
        if outras_informacoes is not None:
            pessoa.outras_informacoes = outras_informacoes
        pessoa.save()
        return UpdatePessoaEnvolvida(pessoa=pessoa)

class DeletePessoaEnvolvida(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            pessoa = PessoaEnvolvida.objects.get(pk=id)
        except PessoaEnvolvida.DoesNotExist:
            raise Exception("PessoaEnvolvida not found")
        pessoa.delete()
        return DeletePessoaEnvolvida(ok=True)

# -------------------------
# Mutations for PessoasEnvolvidasNaInvestigacao
# -------------------------

class CreatePessoasEnvolvidasNaInvestigacao(graphene.Mutation):
    class Arguments:
        nome = String(required=True)
        empresa = String(required=True)
        actividade = String(required=True)
        assinatura = String(required=True)
        data = Date(required=True)

    investigacao = graphene.Field(PessoasEnvolvidasNaInvestigacaoNode)

    def mutate(self, info, nome, empresa, actividade, assinatura, data):
        inv = PessoasEnvolvidasNaInvestigacao.objects.create(
            nome=nome,
            empresa=empresa,
            actividade=actividade,
            assinatura=assinatura,
            data=data
        )
        return CreatePessoasEnvolvidasNaInvestigacao(investigacao=inv)

class UpdatePessoasEnvolvidasNaInvestigacao(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        nome = String()
        empresa = String()
        actividade = String()
        assinatura = String()
        data = Date()

    investigacao = graphene.Field(PessoasEnvolvidasNaInvestigacaoNode)

    def mutate(self, info, id, nome=None, empresa=None, actividade=None, assinatura=None, data=None):
        try:
            inv = PessoasEnvolvidasNaInvestigacao.objects.get(pk=id)
        except PessoasEnvolvidasNaInvestigacao.DoesNotExist:
            raise Exception("PessoasEnvolvidasNaInvestigacao not found")
        if nome is not None:
            inv.nome = nome
        if empresa is not None:
            inv.empresa = empresa
        if actividade is not None:
            inv.actividade = actividade
        if assinatura is not None:
            inv.assinatura = assinatura
        if data is not None:
            inv.data = data
        inv.save()
        return UpdatePessoasEnvolvidasNaInvestigacao(investigacao=inv)

class DeletePessoasEnvolvidasNaInvestigacao(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            inv = PessoasEnvolvidasNaInvestigacao.objects.get(pk=id)
        except PessoasEnvolvidasNaInvestigacao.DoesNotExist:
            raise Exception("PessoasEnvolvidasNaInvestigacao not found")
        inv.delete()
        return DeletePessoasEnvolvidasNaInvestigacao(ok=True)

# -------------------------
# Mutations for AccoesImediatasECorrectivas
# -------------------------

class CreateAccoesImediatasECorrectivas(graphene.Mutation):
    class Arguments:
        accao = String(required=True)
        descricao = String(required=True)
        responsavel = String(required=True)
        data = Date(required=True)
        assinatura = String(required=True)

    accao_obj = graphene.Field(AccoesImediatasECorrectivasNode)

    def mutate(self, info, accao, descricao, responsavel, data, assinatura):
        accao_obj = AccoesImediatasECorrectivas.objects.create(
            accao=accao,
            descricao=descricao,
            responsavel=responsavel,
            data=data,
            assinatura=assinatura
        )
        return CreateAccoesImediatasECorrectivas(accao_obj=accao_obj)

class UpdateAccoesImediatasECorrectivas(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        accao = String()
        descricao = String()
        responsavel = String()
        data = Date()
        assinatura = String()

    accao_obj = graphene.Field(AccoesImediatasECorrectivasNode)

    def mutate(self, info, id, accao=None, descricao=None, responsavel=None, data=None, assinatura=None):
        try:
            accao_obj = AccoesImediatasECorrectivas.objects.get(pk=id)
        except AccoesImediatasECorrectivas.DoesNotExist:
            raise Exception("AccoesImediatasECorrectivas not found")
        if accao is not None:
            accao_obj.accao = accao
        if descricao is not None:
            accao_obj.descricao = descricao
        if responsavel is not None:
            accao_obj.responsavel = responsavel
        if data is not None:
            accao_obj.data = data
        if assinatura is not None:
            accao_obj.assinatura = assinatura
        accao_obj.save()
        return UpdateAccoesImediatasECorrectivas(accao_obj=accao_obj)

class DeleteAccoesImediatasECorrectivas(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            accao_obj = AccoesImediatasECorrectivas.objects.get(pk=id)
        except AccoesImediatasECorrectivas.DoesNotExist:
            raise Exception("AccoesImediatasECorrectivas not found")
        accao_obj.delete()
        return DeleteAccoesImediatasECorrectivas(ok=True)

# -------------------------
# Mutations for ListaVerificacaoKitPrimeirosSocorros
# -------------------------

class CreateListaVerificacaoKitPrimeirosSocorros(graphene.Mutation):
    class Arguments:
        descricao = String(required=True)
        quantidade = Int(required=True)
        data = Date(required=True)
        prazo = Date(required=True)
        observacao = String(required=True)
        inspecao_realizada_por = String(required=True)

    kit = graphene.Field(ListaVerificacaoKitPrimeirosSocorrosNode)

    def mutate(self, info, descricao, quantidade, data, prazo, observacao, inspecao_realizada_por):
        # try:
        #     user = User.objects.get(pk=inspecao_realizada_por_id)
        # except User.DoesNotExist:
        #     raise Exception("User not found")
        kit = ListaVerificacaoKitPrimeirosSocorros.objects.create(
            descricao=descricao,
            quantidade=quantidade,
            data=data,
            prazo=prazo,
            observacao=observacao,
            inspecao_realizada_por=inspecao_realizada_por
        )
        return CreateListaVerificacaoKitPrimeirosSocorros(kit=kit)

class UpdateListaVerificacaoKitPrimeirosSocorros(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        descricao = String()
        quantidade = Int()
        data = Date()
        prazo = Date()
        observacao = String()
        inspecao_realizada_por_id = Int()

    kit = graphene.Field(ListaVerificacaoKitPrimeirosSocorrosNode)

    def mutate(self, info, id, descricao=None, quantidade=None, data=None, prazo=None, observacao=None, inspecao_realizada_por_id=None):
        try:
            kit = ListaVerificacaoKitPrimeirosSocorros.objects.get(pk=id)
        except ListaVerificacaoKitPrimeirosSocorros.DoesNotExist:
            raise Exception("ListaVerificacaoKitPrimeirosSocorros not found")
        if descricao is not None:
            kit.descricao = descricao
        if quantidade is not None:
            kit.quantidade = quantidade
        if data is not None:
            kit.data = data
        if prazo is not None:
            kit.prazo = prazo
        if observacao is not None:
            kit.observacao = observacao
        if inspecao_realizada_por_id is not None:
            try:
                user = User.objects.get(pk=inspecao_realizada_por_id)
            except User.DoesNotExist:
                raise Exception("User not found")
            kit.inspecao_realizada_por = user
        kit.save()
        return UpdateListaVerificacaoKitPrimeirosSocorros(kit=kit)

class DeleteListaVerificacaoKitPrimeirosSocorros(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            kit = ListaVerificacaoKitPrimeirosSocorros.objects.get(pk=id)
        except ListaVerificacaoKitPrimeirosSocorros.DoesNotExist:
            raise Exception("ListaVerificacaoKitPrimeirosSocorros not found")
        kit.delete()
        return DeleteListaVerificacaoKitPrimeirosSocorros(ok=True)

# -------------------------
# Mutations for Incidents
# -------------------------

class CreateIncident(graphene.Mutation):
    class Arguments:
        description = String(required=True)

    incident = graphene.Field(IncidentsNode)

    def mutate(self, info, description):
        incident = Incidents.objects.create(description=description)
        return CreateIncident(incident=incident)

class UpdateIncident(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        description = String()

    incident = graphene.Field(IncidentsNode)

    def mutate(self, info, id, description=None):
        try:
            incident = Incidents.objects.get(pk=id)
        except Incidents.DoesNotExist:
            raise Exception("Incident not found")
        if description is not None:
            incident.description = description
        incident.save()
        return UpdateIncident(incident=incident)

class DeleteIncident(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            incident = Incidents.objects.get(pk=id)
        except Incidents.DoesNotExist:
            raise Exception("Incident not found")
        incident.delete()
        return DeleteIncident(ok=True)


# -------------------------
# Root Mutation
# -------------------------

class Mutation(graphene.ObjectType):
    create_relatorio_acidente_incidente = CreateRelatorioAcidenteIncidente.Field()
    update_relatorio_acidente_incidente = UpdateRelatorioAcidenteIncidente.Field()
    delete_relatorio_acidente_incidente = DeleteRelatorioAcidenteIncidente.Field()

    create_incident_flash_report = CreateIncidentFlashReport.Field()
    update_incident_flash_report = UpdateIncidentFlashReport.Field()
    delete_incident_flash_report = DeleteIncidentFlashReport.Field()

    create_pessoa_envolvida = CreatePessoaEnvolvida.Field()
    update_pessoa_envolvida = UpdatePessoaEnvolvida.Field()
    delete_pessoa_envolvida = DeletePessoaEnvolvida.Field()

    create_pessoas_envolvidas_na_investigacao = CreatePessoasEnvolvidasNaInvestigacao.Field()
    update_pessoas_envolvidas_na_investigacao = UpdatePessoasEnvolvidasNaInvestigacao.Field()
    delete_pessoas_envolvidas_na_investigacao = DeletePessoasEnvolvidasNaInvestigacao.Field()

    create_accoes_imediatas_e_correctivas = CreateAccoesImediatasECorrectivas.Field()
    update_accoes_imediatas_e_correctivas = UpdateAccoesImediatasECorrectivas.Field()
    delete_accoes_imediatas_e_correctivas = DeleteAccoesImediatasECorrectivas.Field()

    create_lista_verificacao_kit_primeiros_socorros = CreateListaVerificacaoKitPrimeirosSocorros.Field()
    update_lista_verificacao_kit_primeiros_socorros = UpdateListaVerificacaoKitPrimeirosSocorros.Field()
    delete_lista_verificacao_kit_primeiros_socorros = DeleteListaVerificacaoKitPrimeirosSocorros.Field()

    create_incident = CreateIncident.Field()
    update_incident = UpdateIncident.Field()
    delete_incident = DeleteIncident.Field()
    

# -------------------------
# Schema
# -------------------------

schema = graphene.Schema(query=Query, mutation=Mutation)
