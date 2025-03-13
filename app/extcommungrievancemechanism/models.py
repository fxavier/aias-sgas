from django.db import models
from riskmanagement.models import Department
from users.models import User

class Status(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
    COMPLETED = 'COMPLETED', 'Completed'

class EfecctivivenessEvaluation(models.TextChoices):
    EFFECTIVE = 'EFFECTIVE', 'Effective'
    NOT_EFFECTIVE = 'NOT_EFFECTIVE', 'Not Effective'

class NotifiedComplaint(models.TextChoices):
    YES = 'YES', 'Yes'
    NO = 'NO', 'No'

class ClaimNonComplianceControl(models.Model):
    number = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    non_compliance_description = models.TextField()
    identified_causes = models.TextField()
    corrective_actions = models.TextField()
    responsible_person = models.CharField(max_length=100)
    deadline = models.DateField()
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.PENDING)
    effectiveness_evaluation = models.CharField(max_length=50, choices=EfecctivivenessEvaluation.choices, default=EfecctivivenessEvaluation.NOT_EFFECTIVE)
    responsible_person_evaluation = models.CharField(max_length=100)
    observation = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='claim_non_compliance_control')
    created_at = models.DateTimeField(auto_now_add=True)
  
    class Meta:
        db_table = 'claim_non_compliance_control'
        verbose_name = 'FR.AS.013_Non Compliance Control'
        verbose_name_plural = 'FR.AS.013_Non Compliance Controls'

    def __str__(self):
        return f'{self.claim} - {self.non_compliance_control}'
    
class ClaimComplainControl(models.Model):
    number = models.CharField(max_length=50, unique=True)
    claim_complain_submitted_by = models.CharField(max_length=100)
    claim_complain_reception_date = models.DateField()
    claim_complain_description = models.TextField()
    treatment_action = models.TextField()
    claim_complain_responsible_person = models.CharField(max_length=100)
    claim_complain_deadline = models.DateField()
    claim_complain_status = models.CharField(max_length=50, choices=Status.choices, default=Status.PENDING)
    closure_date = models.DateField()
    observation = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='claim_complain_control')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'claim_complain_control'
        verbose_name = 'FR.AS.013_Claim And Complain Control'
        verbose_name_plural = 'FR.AS.013_Claim And Complain Controls'

    def __str__(self):
        return f'{self.number} - {self.claim_complain_submitted_by}'

class ComplaintantGender(models.TextChoices):
    MALE = 'MALE', 'Male'
    FEMALE = 'FEMALE', 'Female' 

class AnonymousComplaint(models.TextChoices):
    YES = 'YES', 'Yes'
    NO = 'NO', 'No'

class ComplaintantAccepted(models.TextChoices):
    YES = 'YES', 'Yes'
    NO = 'NO', 'No'

class ClaimCategory(models.TextChoices):
    Odor = 'Odor', 'Odor'
    Noise = 'Noise', 'Noise'
    Effluents = 'Effluents', 'Effluents'
    Company_vehicles = 'Company vehicles', 'Company vehicles'
    Flow_of_migrant_workers = 'Flow of migrant workers', 'Flow of migrant workers'
    Security_personnel = 'Security personnel', 'Security personnel'
    gbv = "GBV/SA/SEA"
    Other = 'Other', 'Other'

class CollectedInformation(models.TextChoices):
    Photos = 'Photos', 'Photos'
    proof_of_legitimacy_documents = 'Proof of legitimacy documents', 'Proof of legitimacy documents'

class ResolutionType(models.TextChoices):
    internal_resolution = 'Internal resolution', 'Internal resolution'
    second_level_resolution = 'Second level resolution', 'Second level resolution'
    third_level_resolution = 'Third level resolution', 'Third level resolution'

class ResolutionSubmitted(models.TextChoices):
    YES = 'YES', 'Yes'
    NO = 'NO', 'No'

class ComplaintantSatisfaction(models.TextChoices):
    SATISFIED = 'SATISFIED', 'Satisfied'
    NOT_SATISFIED = 'NOT_SATISFIED', 'Not Satisfied'

class MonitoringAfterClosure(models.TextChoices):
    YES = 'YES', 'Yes'
    NO = 'NO', 'No'


class PhotoDocumentProvingClosure(models.Model):
    photo = models.ImageField(upload_to='complaints_and_claims_photos')
    document = models.FileField(upload_to='complaints_and_claims_documents')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
  
    class Meta:
        db_table = 'photo_document_proving_closure'
        verbose_name = 'Photo and Document Proving Closure'
        verbose_name_plural = 'Photos and Documents Proving Closure'

    def __str__(self):
        return f'{self.photo} - {self.document}'

class ComplaintAndClaimRecord(models.Model):
    number = models.CharField(max_length=50, unique=True)
    date_occurred = models.DateField()
    local_occurrence = models.CharField(max_length=100)
    how_occurred = models.TextField()
    who_involved = models.TextField()
    report_and_explanation = models.TextField()
    registered_date = models.DateTimeField(auto_now_add=True)
    claim_local_occurrence = models.CharField(max_length=100)
    complaintant_gender = models.CharField(max_length=50, choices=ComplaintantGender.choices)
    complaintant_age = models.IntegerField()
    anonymous_complaint = models.CharField(max_length=50, choices=AnonymousComplaint.choices)
    telephone = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    complaintant_address = models.CharField(max_length=100)
    complaintant_accepted = models.CharField(max_length=50, choices=ComplaintantAccepted.choices)
    action_taken = models.TextField()
    complaintant_notified = models.CharField(max_length=50, choices=NotifiedComplaint.choices, default=NotifiedComplaint.NO)
    notification_method = models.CharField(max_length=100)
    closing_date = models.DateField()
    claim_category = models.CharField(max_length=50, choices=ClaimCategory.choices)
    other_claim_category = models.CharField(max_length=100)
    inspection_date = models.DateField()
    collected_information = models.CharField(max_length=50, choices=CollectedInformation.choices)
    resolution_type = models.CharField(max_length=50, choices=ResolutionType.choices)
    resolution_date = models.DateField()
    resolution_submitted = models.CharField(max_length=100, choices=ResolutionSubmitted.choices)
    corrective_action_taken = models.TextField()
    involved_in_resolution = models.TextField()
    complaintant_satisfaction = models.CharField(max_length=50, choices=ComplaintantSatisfaction.choices)
    photos_and_documents_proving_closure = models.ManyToManyField(PhotoDocumentProvingClosure, blank=True)
    resources_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    number_of_days_since_received_to_closure = models.IntegerField()
    monitoring_after_closure = models.CharField(max_length=100, choices=MonitoringAfterClosure.choices)
    monitoring_method_and_frequency = models.TextField()
    follow_up = models.TextField()
    involved_institutions = models.CharField(max_length=100, null=True, blank=True)
    suggested_preventive_actions = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaint_and_claim_records')
    created_at = models.DateTimeField(auto_now_add=True)
  
    class Meta:
        db_table = 'complaint_and_claim_record'
        verbose_name = 'FR.AS.026_Complaints and Claims Registration Form'
        verbose_name_plural = 'FR.AS.026_Complaints and Claims Registration Form'

    def __str__(self):
        return f'{self.number} - {self.department}'
    

#Worker Grievance

class PreferedContactMethod(models.TextChoices):
    EMAIL = 'EMAIL', 'Email'
    PHONE = 'PHONE', 'Phone'
    FACE_TO_FACE = 'FACE_TO_FACE', 'Face to Face'


class PreferedLanguage(models.TextChoices):
    PORTUGUESE = 'PORTUGUESE', 'Portuguese'
    ENGLISH = 'ENGLISH', 'English'
    OTHER = 'OTHER', 'Other'


class WorkerGrievance(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    date = models.DateField()
    prefered_contact_method = models.CharField(max_length=50, choices=PreferedContactMethod.choices)
    contact = models.CharField(max_length=100)
    prefered_language = models.CharField(max_length=50, choices=PreferedLanguage.choices)
    other_language = models.CharField(max_length=100, null=True, blank=True)
    grievance_details = models.TextField()
    unique_identification_of_company_acknowlegement = models.CharField(max_length=100)
    name_of_person_acknowledging_grievance = models.CharField(max_length=100)
    position_of_person_acknowledging_grievance = models.CharField(max_length=100)
    date_of_acknowledgement = models.DateField()
    signature_of_person_acknowledging_grievance = models.CharField(max_length=100)
    follow_up_details = models.TextField()
    closed_out_date = models.DateField()
    signature_of_response_corrective_action_person = models.CharField(max_length=100)
    acknowledge_receipt_of_response = models.CharField(max_length=100)
    name_of_person_acknowledging_response = models.CharField(max_length=100)
    signature_of_person_acknowledging_response = models.CharField(max_length=100)
    date_of_acknowledgement_response = models.DateField()


    class Meta:
        verbose_name = 'FR.AS.033_Worker Grievance'
        verbose_name_plural = 'FR.AS.033_Worker Grievances'