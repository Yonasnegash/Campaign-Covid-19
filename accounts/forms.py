from django.forms import ModelForm
from symptom.models import Symptom, Status

class SymptomForm(ModelForm):
    class Meta:
        model = Symptom
        fields = ['shortness_of_breath', 'cough', 'high_fever', 'tiredness', 'sore_throat']

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['shortness_of_breath', 'cough', 'high_fever', 'tiredness', 'sore_throat']





