from django import forms
from .models import Event
class Applicantform(forms.ModelForm):
    class Meta:
        model= Applicant 
        fields= ['full_name','email','phone']
