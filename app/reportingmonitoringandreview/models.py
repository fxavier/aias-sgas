from django.db import models

class WasteTransferLog(models.Model):
    waste_type = models.CharField(max_length=255)
    how_is_waste_contained = models.CharField(max_length=255)
    how_much_waste = models.PositiveIntegerField()
    reference_number = models.CharField(max_length=255)
    date_of_removal = models.DateField()
    transfer_company = models.CharField(max_length=255)
    special_instructions = models.TextField()

    class Meta:
        verbose_name = 'FR.AS.031 Waste Transfer Log'
        verbose_name_plural = 'FR.AS.031 Waste Transfer'

    def __str__(self):
        return self.reference_number
