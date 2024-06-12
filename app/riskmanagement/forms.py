from django import forms
from .models import EnvironmentalSocialScreening

class EnvironmentalSocialScreeningForm(forms.ModelForm):
    class Meta:
        model = EnvironmentalSocialScreening
        fields = '__all__'
    
    class Media:
        js = ('js/environmental_social_screening.js',)
