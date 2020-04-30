from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum, Count
from django.http import JsonResponse

from symptom.models import Symptom

def index(request):
    return render(request, 'pages/index.html')

def fever_chart(request):
    labels = []
    data = []
    high_fever = Symptom.objects.values('high_fever').annotate(fever=Count('high_fever'))
    # strings = [str(integer) for integer in high_fever]
    # a_string = "".join(strings)
    # an_integer = int(a_string)
    print(high_fever)
    queryset = Symptom.objects.values('zone__name').annotate(fever=Count('high_fever'))
    for entry in queryset:
        labels.append(entry['zone__name'])
        data.append(entry['fever'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def shortness_of_breath(request):
    labels2 = []
    data2 = []

    queryset1 = Symptom.objects.values('zone__name').annotate(breath=Count('shortness_of_breath'))
    for entry in queryset1:
        labels2.append(entry['zone__name'])
        data2.append(entry['breath'])
    return JsonResponse(data={
        'labels': labels2,
        'data': data2,
    })

def cough(request):
    labels3 = []
    data3 = []

    queryset = Symptom.objects.values('zone__name').annotate(cough=Count('cough'))
    for entry in queryset:
        labels3.append(entry['zone__name'])
        data3.append(entry['cough'])
    return JsonResponse(data={
        'labels': labels3,
        'data': data3,
    })
