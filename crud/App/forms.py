from django import forms
from App.models import Candidate


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
    def __str__(self):
        return 

    

