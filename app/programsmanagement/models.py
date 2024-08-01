from django.db import models
from users.models import User

class StrategicObjective(models.Model):
    description = models.CharField(max_length=255)
    goals = models.CharField(max_length=255)
    strategies_for_achievement = models.TextField()

    
    def __str__(self):
        return self.description
    

class SpecificObjective(models.Model):
    strategic_objective = models.CharField(max_length=255)
    specific_objective = models.CharField(max_length=255)
    actions_for_achievement = models.TextField()
    responsible_person = models.CharField(max_length=100)
    necessary_resources = models.TextField()
    indicator = models.CharField(max_length=100)
    goal = models.CharField(max_length=100)
    monitoring_frequency = models.CharField(max_length=100)
    deadline = models.DateField()
    observation = models.TextField()

    def __str__(self):
        return self.strategic_objective