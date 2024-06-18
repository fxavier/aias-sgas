from django import forms
from .models import ComplaintAndClaimRecord

class ComplaintAndClaimRecordForm(forms.ModelForm):
    class Meta:
        model = ComplaintAndClaimRecord
        fields = '__all__'
    
    class Media:
        js = ('js/ext_com_grievance.js',)
