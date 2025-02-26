import graphene
from graphene import Date, DateTime, Int, String, List, Decimal, Field
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload

# Import models from your app
from .models import (
    ClaimNonComplianceControl,
    ClaimComplainControl,
    PhotoDocumentProvingClosure,
    ComplaintAndClaimRecord,
    WorkerGrievance,
    # TextChoices classes:
    Status,
    EfecctivivenessEvaluation,
    NotifiedComplaint,
    ComplaintantGender,
    AnonymousComplaint,
    ComplaintantAccepted,
    ClaimCategory,
    CollectedInformation,
    ResolutionType,
    ResolutionSubmitted,
    ComplaintantSatisfaction,
    MonitoringAfterClosure,
    PreferedContactMethod,
    PreferedLanguage,
)
# Import related models for foreign keys
from riskmanagement.models import Department
from users.models import User

# --------------------------------------------------------------------
# Create Graphene enums from your Django TextChoices
# --------------------------------------------------------------------

StatusEnum = graphene.Enum.from_enum(Status)
EffectivenessEvaluationEnum = graphene.Enum.from_enum(EfecctivivenessEvaluation)
NotifiedComplaintEnum = graphene.Enum.from_enum(NotifiedComplaint)
ComplaintantGenderEnum = graphene.Enum.from_enum(ComplaintantGender)
AnonymousComplaintEnum = graphene.Enum.from_enum(AnonymousComplaint)
ComplaintantAcceptedEnum = graphene.Enum.from_enum(ComplaintantAccepted)
ClaimCategoryEnum = graphene.Enum.from_enum(ClaimCategory)
CollectedInformationEnum = graphene.Enum.from_enum(CollectedInformation)
ResolutionTypeEnum = graphene.Enum.from_enum(ResolutionType)
ResolutionSubmittedEnum = graphene.Enum.from_enum(ResolutionSubmitted)
ComplaintantSatisfactionEnum = graphene.Enum.from_enum(ComplaintantSatisfaction)
MonitoringAfterClosureEnum = graphene.Enum.from_enum(MonitoringAfterClosure)
PreferedContactMethodEnum = graphene.Enum.from_enum(PreferedContactMethod)
PreferedLanguageEnum = graphene.Enum.from_enum(PreferedLanguage)

# --------------------------------------------------------------------
# Graphene Types for Models
# --------------------------------------------------------------------

class ClaimNonComplianceControlNode(DjangoObjectType):
    class Meta:
        model = ClaimNonComplianceControl
        fields = '__all__'

class ClaimComplainControlNode(DjangoObjectType):
    class Meta:
        model = ClaimComplainControl
        fields = '__all__'

class PhotoDocumentProvingClosureNode(DjangoObjectType):
    class Meta:
        model = PhotoDocumentProvingClosure
        fields = '__all__'

class ComplaintAndClaimRecordNode(DjangoObjectType):
    class Meta:
        model = ComplaintAndClaimRecord
        fields = '__all__'

class WorkerGrievanceNode(DjangoObjectType):
    class Meta:
        model = WorkerGrievance
        fields = '__all__'

# --------------------------------------------------------------------
# Queries
# --------------------------------------------------------------------

class Query(graphene.ObjectType):
    all_claim_non_compliance_controls = List(ClaimNonComplianceControlNode)
    claim_non_compliance_control = Field(ClaimNonComplianceControlNode, id=Int(required=True))

    all_claim_complain_controls = List(ClaimComplainControlNode)
    claim_complain_control = Field(ClaimComplainControlNode, id=Int(required=True))

    all_photo_document_proving_closures = List(PhotoDocumentProvingClosureNode)
    photo_document_proving_closure = Field(PhotoDocumentProvingClosureNode, id=Int(required=True))

    all_complaint_and_claim_records = List(ComplaintAndClaimRecordNode)
    complaint_and_claim_record = Field(ComplaintAndClaimRecordNode, id=Int(required=True))

    all_worker_grievances = List(WorkerGrievanceNode)
    worker_grievance = Field(WorkerGrievanceNode, id=Int(required=True))

    def resolve_all_claim_non_compliance_controls(root, info):
        return ClaimNonComplianceControl.objects.all()

    def resolve_claim_non_compliance_control(root, info, id):
        try:
            return ClaimNonComplianceControl.objects.get(pk=id)
        except ClaimNonComplianceControl.DoesNotExist:
            return None

    def resolve_all_claim_complain_controls(root, info):
        return ClaimComplainControl.objects.all()

    def resolve_claim_complain_control(root, info, id):
        try:
            return ClaimComplainControl.objects.get(pk=id)
        except ClaimComplainControl.DoesNotExist:
            return None

    def resolve_all_photo_document_proving_closures(root, info):
        return PhotoDocumentProvingClosure.objects.all()

    def resolve_photo_document_proving_closure(root, info, id):
        try:
            return PhotoDocumentProvingClosure.objects.get(pk=id)
        except PhotoDocumentProvingClosure.DoesNotExist:
            return None

    def resolve_all_complaint_and_claim_records(root, info):
        return ComplaintAndClaimRecord.objects.all()

    def resolve_complaint_and_claim_record(root, info, id):
        try:
            return ComplaintAndClaimRecord.objects.get(pk=id)
        except ComplaintAndClaimRecord.DoesNotExist:
            return None

    def resolve_all_worker_grievances(root, info):
        return WorkerGrievance.objects.all()

    def resolve_worker_grievance(root, info, id):
        try:
            return WorkerGrievance.objects.get(pk=id)
        except WorkerGrievance.DoesNotExist:
            return None

# --------------------------------------------------------------------
# Mutations
# --------------------------------------------------------------------

# --- ClaimNonComplianceControl Mutations ---

class CreateClaimNonComplianceControl(graphene.Mutation):
    class Arguments:
        number = String(required=True)
        department_id = Int(required=True)
        non_compliance_description = String(required=True)
        identified_causes = String(required=True)
        corrective_actions = String(required=True)
        responsible_person = String(required=True)
        deadline = Date(required=True)
        status = StatusEnum(required=False, default_value=Status.PENDING)
        effectiveness_evaluation = EffectivenessEvaluationEnum(required=False, default_value=EfecctivivenessEvaluation.NOT_EFFECTIVE)
        responsible_person_evaluation = String(required=True)
        observation = String(required=True)
        created_by_id = Int(required=True)

    claim_non_compliance_control = Field(ClaimNonComplianceControlNode)

    def mutate(self, info, number, department_id, non_compliance_description, identified_causes,
                 corrective_actions, responsible_person, deadline, responsible_person_evaluation,
                 observation, created_by_id, status=Status.PENDING, effectiveness_evaluation=EfecctivivenessEvaluation.NOT_EFFECTIVE):
        try:
            department = Department.objects.get(pk=department_id)
        except Department.DoesNotExist:
            raise Exception("Department not found")
        try:
            created_by = User.objects.get(pk=created_by_id)
        except User.DoesNotExist:
            raise Exception("User not found")
        control = ClaimNonComplianceControl.objects.create(
            number=number,
            department=department,
            non_compliance_description=non_compliance_description,
            identified_causes=identified_causes,
            corrective_actions=corrective_actions,
            responsible_person=responsible_person,
            deadline=deadline,
            status=status,
            effectiveness_evaluation=effectiveness_evaluation,
            responsible_person_evaluation=responsible_person_evaluation,
            observation=observation,
            created_by=created_by
        )
        return CreateClaimNonComplianceControl(claim_non_compliance_control=control)

class UpdateClaimNonComplianceControl(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        number = String()
        non_compliance_description = String()
        identified_causes = String()
        corrective_actions = String()
        responsible_person = String()
        deadline = Date()
        status = StatusEnum()
        effectiveness_evaluation = EffectivenessEvaluationEnum()
        responsible_person_evaluation = String()
        observation = String()
        department_id = Int()
        created_by_id = Int()

    claim_non_compliance_control = Field(ClaimNonComplianceControlNode)

    def mutate(self, info, id, **kwargs):
        try:
            control = ClaimNonComplianceControl.objects.get(pk=id)
        except ClaimNonComplianceControl.DoesNotExist:
            raise Exception("ClaimNonComplianceControl not found")
        if 'department_id' in kwargs:
            try:
                department = Department.objects.get(pk=kwargs.pop('department_id'))
                control.department = department
            except Department.DoesNotExist:
                raise Exception("Department not found")
        if 'created_by_id' in kwargs:
            try:
                created_by = User.objects.get(pk=kwargs.pop('created_by_id'))
                control.created_by = created_by
            except User.DoesNotExist:
                raise Exception("User not found")
        for key, value in kwargs.items():
            setattr(control, key, value)
        control.save()
        return UpdateClaimNonComplianceControl(claim_non_compliance_control=control)

class DeleteClaimNonComplianceControl(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            control = ClaimNonComplianceControl.objects.get(pk=id)
        except ClaimNonComplianceControl.DoesNotExist:
            raise Exception("ClaimNonComplianceControl not found")
        control.delete()
        return DeleteClaimNonComplianceControl(ok=True)

# --- ClaimComplainControl Mutations ---

class CreateClaimComplainControl(graphene.Mutation):
    class Arguments:
        number = String(required=True)
        claim_complain_submitted_by = String(required=True)
        claim_complain_reception_date = Date(required=True)
        claim_complain_description = String(required=True)
        treatment_action = String(required=True)
        claim_complain_responsible_person = String(required=True)
        claim_complain_deadline = Date(required=True)
        claim_complain_status = StatusEnum(required=False, default_value=Status.PENDING)
        closure_date = Date(required=True)
        observation = String(required=True)
        created_by_id = Int(required=True)

    claim_complain_control = Field(ClaimComplainControlNode)

    def mutate(self, info, number, claim_complain_submitted_by, claim_complain_reception_date,
                 claim_complain_description, treatment_action, claim_complain_responsible_person,
                 claim_complain_deadline, closure_date, observation, created_by_id,
                 claim_complain_status=Status.PENDING):
        try:
            created_by = User.objects.get(pk=created_by_id)
        except User.DoesNotExist:
            raise Exception("User not found")
        control = ClaimComplainControl.objects.create(
            number=number,
            claim_complain_submitted_by=claim_complain_submitted_by,
            claim_complain_reception_date=claim_complain_reception_date,
            claim_complain_description=claim_complain_description,
            treatment_action=treatment_action,
            claim_complain_responsible_person=claim_complain_responsible_person,
            claim_complain_deadline=claim_complain_deadline,
            claim_complain_status=claim_complain_status,
            closure_date=closure_date,
            observation=observation,
            created_by=created_by
        )
        return CreateClaimComplainControl(claim_complain_control=control)

class UpdateClaimComplainControl(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        number = String()
        claim_complain_submitted_by = String()
        claim_complain_reception_date = Date()
        claim_complain_description = String()
        treatment_action = String()
        claim_complain_responsible_person = String()
        claim_complain_deadline = Date()
        claim_complain_status = StatusEnum()
        closure_date = Date()
        observation = String()
        created_by_id = Int()

    claim_complain_control = Field(ClaimComplainControlNode)

    def mutate(self, info, id, **kwargs):
        try:
            control = ClaimComplainControl.objects.get(pk=id)
        except ClaimComplainControl.DoesNotExist:
            raise Exception("ClaimComplainControl not found")
        if 'created_by_id' in kwargs:
            try:
                created_by = User.objects.get(pk=kwargs.pop('created_by_id'))
                control.created_by = created_by
            except User.DoesNotExist:
                raise Exception("User not found")
        for key, value in kwargs.items():
            setattr(control, key, value)
        control.save()
        return UpdateClaimComplainControl(claim_complain_control=control)

class DeleteClaimComplainControl(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            control = ClaimComplainControl.objects.get(pk=id)
        except ClaimComplainControl.DoesNotExist:
            raise Exception("ClaimComplainControl not found")
        control.delete()
        return DeleteClaimComplainControl(ok=True)

# --- PhotoDocumentProvingClosure Mutations ---

class CreatePhotoDocumentProvingClosure(graphene.Mutation):
    class Arguments:
        photo = Upload(required=True)
        document = Upload(required=True)
        created_by_id = Int(required=True)

    photo_document_proving_closure = Field(PhotoDocumentProvingClosureNode)

    def mutate(self, info, photo, document, created_by_id):
        try:
            created_by = User.objects.get(pk=created_by_id)
        except User.DoesNotExist:
            raise Exception("User not found")
        pdpc = PhotoDocumentProvingClosure.objects.create(
            photo=photo,
            document=document,
            created_by=created_by
        )
        return CreatePhotoDocumentProvingClosure(photo_document_proving_closure=pdpc)

class UpdatePhotoDocumentProvingClosure(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        photo = Upload()
        document = Upload()
        created_by_id = Int()

    photo_document_proving_closure = Field(PhotoDocumentProvingClosureNode)

    def mutate(self, info, id, photo=None, document=None, created_by_id=None):
        try:
            pdpc = PhotoDocumentProvingClosure.objects.get(pk=id)
        except PhotoDocumentProvingClosure.DoesNotExist:
            raise Exception("PhotoDocumentProvingClosure not found")
        if photo is not None:
            pdpc.photo = photo
        if document is not None:
            pdpc.document = document
        if created_by_id is not None:
            try:
                created_by = User.objects.get(pk=created_by_id)
                pdpc.created_by = created_by
            except User.DoesNotExist:
                raise Exception("User not found")
        pdpc.save()
        return UpdatePhotoDocumentProvingClosure(photo_document_proving_closure=pdpc)

class DeletePhotoDocumentProvingClosure(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            pdpc = PhotoDocumentProvingClosure.objects.get(pk=id)
        except PhotoDocumentProvingClosure.DoesNotExist:
            raise Exception("PhotoDocumentProvingClosure not found")
        pdpc.delete()
        return DeletePhotoDocumentProvingClosure(ok=True)

# --- ComplaintAndClaimRecord Mutations ---

class CreateComplaintAndClaimRecord(graphene.Mutation):
    class Arguments:
        number = String(required=True)
        date_occurred = Date(required=True)
        local_occurrence = String(required=True)
        how_occurred = String(required=True)
        who_involved = String(required=True)
        report_and_explanation = String(required=True)
        claim_local_occurrence = String(required=True)
        complaintant_gender = ComplaintantGenderEnum(required=True)
        complaintant_age = Int(required=True)
        anonymous_complaint = AnonymousComplaintEnum(required=True)
        telephone = String(required=True)
        email = String()
        complaintant_address = String(required=True)
        complaintant_accepted = ComplaintantAcceptedEnum(required=True)
        action_taken = String(required=True)
        complaintant_notified = NotifiedComplaintEnum(required=False, default_value=NotifiedComplaint.NO)
        notification_method = String(required=True)
        closing_date = Date(required=True)
        claim_category = ClaimCategoryEnum(required=True)
        other_claim_category = String(required=True)
        inspection_date = Date(required=True)
        collected_information = CollectedInformationEnum(required=True)
        resolution_type = ResolutionTypeEnum(required=True)
        resolution_date = Date(required=True)
        resolution_submitted = ResolutionSubmittedEnum(required=True)
        corrective_action_taken = String(required=True)
        involved_in_resolution = String(required=True)
        complaintant_satisfaction = ComplaintantSatisfactionEnum(required=True)
        photos_and_documents_proving_closure_ids = List(Int)
        resources_spent = Decimal(required=True)
        number_of_days_since_received_to_closure = Int(required=True)
        monitoring_after_closure = MonitoringAfterClosureEnum(required=True)
        monitoring_method_and_frequency = String(required=True)
        follow_up = String(required=True)
        involved_institutions = String()
        suggested_preventive_actions = String(required=True)
        created_by_id = Int(required=True)

    complaint_and_claim_record = Field(ComplaintAndClaimRecordNode)

    def mutate(self, info, photos_and_documents_proving_closure_ids=None, created_by_id=None, **kwargs):
        try:
            created_by = User.objects.get(pk=created_by_id)
        except User.DoesNotExist:
            raise Exception("User not found")
        record = ComplaintAndClaimRecord.objects.create(created_by=created_by, **kwargs)
        if photos_and_documents_proving_closure_ids:
            photos = PhotoDocumentProvingClosure.objects.filter(pk__in=photos_and_documents_proving_closure_ids)
            record.photos_and_documents_proving_closure.set(photos)
        return CreateComplaintAndClaimRecord(complaint_and_claim_record=record)

class UpdateComplaintAndClaimRecord(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        number = String()
        date_occurred = Date()
        local_occurrence = String()
        how_occurred = String()
        who_involved = String()
        report_and_explanation = String()
        claim_local_occurrence = String()
        complaintant_gender = ComplaintantGenderEnum()
        complaintant_age = Int()
        anonymous_complaint = AnonymousComplaintEnum()
        telephone = String()
        email = String()
        complaintant_address = String()
        complaintant_accepted = ComplaintantAcceptedEnum()
        action_taken = String()
        complaintant_notified = NotifiedComplaintEnum()
        notification_method = String()
        closing_date = Date()
        claim_category = ClaimCategoryEnum()
        other_claim_category = String()
        inspection_date = Date()
        collected_information = CollectedInformationEnum()
        resolution_type = ResolutionTypeEnum()
        resolution_date = Date()
        resolution_submitted = ResolutionSubmittedEnum()
        corrective_action_taken = String()
        involved_in_resolution = String()
        complaintant_satisfaction = ComplaintantSatisfactionEnum()
        photos_and_documents_proving_closure_ids = List(Int)
        resources_spent = Decimal()
        number_of_days_since_received_to_closure = Int()
        monitoring_after_closure = MonitoringAfterClosureEnum()
        monitoring_method_and_frequency = String()
        follow_up = String()
        involved_institutions = String()
        suggested_preventive_actions = String()
        created_by_id = Int()

    complaint_and_claim_record = Field(ComplaintAndClaimRecordNode)

    def mutate(self, info, id, **kwargs):
        try:
            record = ComplaintAndClaimRecord.objects.get(pk=id)
        except ComplaintAndClaimRecord.DoesNotExist:
            raise Exception("ComplaintAndClaimRecord not found")
        if 'created_by_id' in kwargs:
            try:
                created_by = User.objects.get(pk=kwargs.pop('created_by_id'))
                record.created_by = created_by
            except User.DoesNotExist:
                raise Exception("User not found")
        if 'photos_and_documents_proving_closure_ids' in kwargs:
            photos_ids = kwargs.pop('photos_and_documents_proving_closure_ids')
            if photos_ids:
                photos = PhotoDocumentProvingClosure.objects.filter(pk__in=photos_ids)
                record.photos_and_documents_proving_closure.set(photos)
        for key, value in kwargs.items():
            setattr(record, key, value)
        record.save()
        return UpdateComplaintAndClaimRecord(complaint_and_claim_record=record)

class DeleteComplaintAndClaimRecord(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            record = ComplaintAndClaimRecord.objects.get(pk=id)
        except ComplaintAndClaimRecord.DoesNotExist:
            raise Exception("ComplaintAndClaimRecord not found")
        record.delete()
        return DeleteComplaintAndClaimRecord(ok=True)

# --- WorkerGrievance Mutations ---

class CreateWorkerGrievance(graphene.Mutation):
    class Arguments:
        name = String(required=True)
        company = String(required=True)
        date = Date(required=True)
        prefered_contact_method = PreferedContactMethodEnum(required=True)
        contact = String(required=True)
        prefered_language = PreferedLanguageEnum(required=True)
        other_language = String()
        grievance_details = String(required=True)
        unique_identification_of_company_acknowlegement = String(required=True)
        name_of_person_acknowledging_grievance = String(required=True)
        position_of_person_acknowledging_grievance = String(required=True)
        date_of_acknowledgement = Date(required=True)
        signature_of_person_acknowledging_grievance = String(required=True)
        follow_up_details = String(required=True)
        closed_out_date = Date(required=True)
        signature_of_response_corrective_action_person = String(required=True)
        acknowledge_receipt_of_response = String(required=True)
        name_of_person_acknowledging_response = String(required=True)
        signature_of_person_acknowledging_response = String(required=True)
        date_of_acknowledgement_response = Date(required=True)

    worker_grievance = Field(WorkerGrievanceNode)

    def mutate(self, info, **kwargs):
        grievance = WorkerGrievance.objects.create(**kwargs)
        return CreateWorkerGrievance(worker_grievance=grievance)

class UpdateWorkerGrievance(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        name = String()
        company = String()
        date = Date()
        prefered_contact_method = PreferedContactMethodEnum()
        contact = String()
        prefered_language = PreferedLanguageEnum()
        other_language = String()
        grievance_details = String()
        unique_identification_of_company_acknowlegement = String()
        name_of_person_acknowledging_grievance = String()
        position_of_person_acknowledging_grievance = String()
        date_of_acknowledgement = Date()
        signature_of_person_acknowledging_grievance = String()
        follow_up_details = String()
        closed_out_date = Date()
        signature_of_response_corrective_action_person = String()
        acknowledge_receipt_of_response = String()
        name_of_person_acknowledging_response = String()
        signature_of_person_acknowledging_response = String()
        date_of_acknowledgement_response = Date()

    worker_grievance = Field(WorkerGrievanceNode)

    def mutate(self, info, id, **kwargs):
        try:
            grievance = WorkerGrievance.objects.get(pk=id)
        except WorkerGrievance.DoesNotExist:
            raise Exception("WorkerGrievance not found")
        for key, value in kwargs.items():
            setattr(grievance, key, value)
        grievance.save()
        return UpdateWorkerGrievance(worker_grievance=grievance)

class DeleteWorkerGrievance(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            grievance = WorkerGrievance.objects.get(pk=id)
        except WorkerGrievance.DoesNotExist:
            raise Exception("WorkerGrievance not found")
        grievance.delete()
        return DeleteWorkerGrievance(ok=True)

# --------------------------------------------------------------------
# Root Mutation and Schema
# --------------------------------------------------------------------

class Mutation(graphene.ObjectType):
    create_claim_non_compliance_control = CreateClaimNonComplianceControl.Field()
    update_claim_non_compliance_control = UpdateClaimNonComplianceControl.Field()
    delete_claim_non_compliance_control = DeleteClaimNonComplianceControl.Field()

    create_claim_complain_control = CreateClaimComplainControl.Field()
    update_claim_complain_control = UpdateClaimComplainControl.Field()
    delete_claim_complain_control = DeleteClaimComplainControl.Field()

    create_photo_document_proving_closure = CreatePhotoDocumentProvingClosure.Field()
    update_photo_document_proving_closure = UpdatePhotoDocumentProvingClosure.Field()
    delete_photo_document_proving_closure = DeletePhotoDocumentProvingClosure.Field()

    create_complaint_and_claim_record = CreateComplaintAndClaimRecord.Field()
    update_complaint_and_claim_record = UpdateComplaintAndClaimRecord.Field()
    delete_complaint_and_claim_record = DeleteComplaintAndClaimRecord.Field()

    create_worker_grievance = CreateWorkerGrievance.Field()
    update_worker_grievance = UpdateWorkerGrievance.Field()
    delete_worker_grievance = DeleteWorkerGrievance.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
