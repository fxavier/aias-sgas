from django.db import models


class WastManagement(models.Model):
    waste_route = models.CharField(max_length=255)
    labelling = models.CharField(max_length=255)
    storage = models.CharField(max_length=255)
    transportation_company_method = models.CharField(max_length=255)
    disposal_company = models.CharField(max_length=255)
    special_instructions = models.TextField()

    class Meta:
        verbose_name = 'FR.AS.032 Waste Management'
        verbose_name_plural = 'FR.AS.032 Waste Managements'

    def __str__(self):
        return self.waste_route
