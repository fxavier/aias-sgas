from django.db import models
from riskmanagement.models import Department, Subproject


class TrainingNeeds(models.Model):
    filled_by = models.CharField(max_length=100)
    date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    subproject = models.ForeignKey(Subproject, on_delete=models.CASCADE, null=True, blank=True)
    training = models.CharField(max_length=255)
    training_objective = models.TextField()
    proposal_of_training_entity = models.CharField(max_length=255)
    potential_training_participants = models.TextField()

    class Meta:
        verbose_name = 'FR.AS.005 Training Need'
        verbose_name_plural = 'FR.AS.005 Training Needs'

    def __str__(self):
        return self.training
    
class TrainingTtype(models.Choices):
    INTERNAL = 'Internal'
    EXTERNAL = 'External'

class Months(models.Choices):
    JANUARY = 'January'
    FEBRUARY = 'February'
    MARCH = 'March'
    APRIL = 'April'
    MAY = 'May'
    JUNE = 'June'
    JULY = 'July'
    AUGUST = 'August'
    SEPTEMBER = 'September'
    OCTOBER = 'October'
    NOVEMBER = 'November'
    DECEMBER = 'December'

class TrainingStatus(models.Choices):
    PLANNED = 'Planned'
    COMPLETED = 'Completed'

class TrainingPlan(models.Model):
    updated_by = models.CharField(max_length=100)
    date = models.DateField()
    year = models.PositiveIntegerField()
    training_area = models.CharField(max_length=255)
    training_title = models.CharField(max_length=255)
    training_objective = models.TextField()
    training_type = models.CharField(max_length=255, choices=TrainingTtype.choices)
    training_entity = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    number_of_trainees = models.PositiveIntegerField()
    training_recipients = models.TextField()
    training_month = models.CharField(max_length=20, choices=Months.choices)
    training_status = models.CharField(max_length=20, choices=TrainingStatus.choices)
    observations = models.TextField()

    class Meta:
        verbose_name = 'FR.AS.006_Training Plan'
        verbose_name_plural = 'FR.AS.006_Training Plans'

    def __str__(self):
        return self.training_title
    

class AnswerChoices(models.Choices):
    SATISFACTORY = 'Satisfactory'
    PARTIALLY_SATISFACTORY = 'Partially Satisfactory'
    UNSATISFACTORY = 'Unsatisfactory'

class TrainingEvaluationQuestions(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question


# class TrainingEvaluationQuestions(models.Choices):
#    Q1 = 'After the training, has the employee demonstrated greater knowledge related to their work?'
#    Q2 = 'Was the employee able to put the knowledge obtained in the training into practice?'
#    Q3 = 'Were working conditions provided to the employee to apply the knowledge acquired in the training?'
#    Q4 = 'Did the training achieve its objectives?' 
#    Q5 = 'What result was obtained after the training? (Justify by indicating the employee results, comparing before and after)'

class HumanResourceAnswerChoices(models.Choices):
    EFFECTIVE = 'effective'
    INEFFECTIVE = 'ineffective'

class TrainingEffectivnessAssessment(models.Model):
    training = models.CharField(max_length=255)
    date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    subproject = models.ForeignKey(Subproject, on_delete=models.CASCADE, null=True, blank=True)
    trainee = models.CharField(max_length=100)
    immediate_supervisor = models.CharField(max_length=100)
    training_evaluation_question = models.ForeignKey(TrainingEvaluationQuestions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=50, choices=AnswerChoices.choices)
    human_resource_evaluation = models.CharField(max_length=50, choices=HumanResourceAnswerChoices.choices)

    class Meta:
        verbose_name = 'FR.AS.007 Training Effectiveness Assessment'
        verbose_name_plural = 'FR.AS.007 Training Effectiveness Assessments'

    def __str__(self):
        return self.trainee
    
class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Training(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class ToolBoxTalks(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Effectiveness(models.Choices):
    Effective = 'Effective'
    Ineffective = 'Not effective'

class TrainingMatrix(models.Model):
    date = models.DateField(null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    toolbox_talks = models.ForeignKey(ToolBoxTalks, on_delete=models.CASCADE)
    effectiveness = models.CharField(max_length=255, choices=Effectiveness.choices)
    actions_training_not_effective = models.TextField(blank=True, null=True)
    approved_by = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'FR.AS.006_Training Matrix'
        verbose_name_plural = 'FR.AS.006_Training Matrix'

    def __str__(self):
        return self.position.name


class AcceptanceConfirmation(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
    
class OHSACTING(models.Model):
    fullname = models.CharField(max_length=255)
    designation = models.CharField(max_length=100, blank=True, null=True)
    terms_of_office_from = models.CharField(max_length=100, null=True, blank=True)
    terms_of_office_to = models.CharField(max_length=100, null=True, blank=True)
    acceptance_confirmation = models.ManyToManyField(AcceptanceConfirmation)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'FR.AS.038 OHS ACTING' 
        verbose_name_plural = 'FR.AS.038 OHS ACTING'

    def __str__(self):
        return self.fullname


    
