from rest_framework import serializers
from symptom.models import Symptom

class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ("__all__")