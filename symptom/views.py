from django.shortcuts import render
from django.http import HttpResponse
from .models import Symptom
from rest_framework import viewsets
from .serializer import SymptomSerializer

class SymptomAPI(viewsets.ModelViewSet):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
# def index(request):
#     if request.method == 'POST':
#         print('submitted')
#         return render(request, 'accounts/symptom.html')
#     else:
#         return render(request, 'accounts/symptom.html')
