from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum, Count
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth

from symptom.models import Symptom

def index(request):
    symptom = Symptom.objects.all()

    context = {
        'symptom': symptom,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def initiator(request):
    return render(request, 'pages/initiator.html')

def embed(request):
    return render(request, 'pages/embedded_map.html')

def three_symptoms(request):
    labels = []
    data = []
    data1 = []
    data2 = []
    final = []
   
    query = Symptom.objects.filter(high_fever=1, cough=1, shortness_of_breath=1)
    _3_symptoms = query.values('zone__name').annotate(hf=Sum('high_fever'), c=Sum('cough'), sh=Sum('shortness_of_breath'))
    # _3_symptoms = Symptom.objects.values('zone__name').annotate(hf=Sum('high_fever'), c=Sum('cough'), sh=Sum('shortness_of_breath'))

    for entry in _3_symptoms:
        labels.append(entry['zone__name'])
        data.append(entry['hf'])
        # data1.append(entry['c'])
        # data2.append(entry['sh'])

    # for i in range(len(data)):
    #     total = data[i] + data2[i] + data2[i]
    #     final.append(total)
    # print(final)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def five_symptoms(request):
    labels = []
    data = []

    query = Symptom.objects.filter(high_fever=1, cough=1, shortness_of_breath=1, tiredness=1, sore_throat=1)
    _5_symptoms = query.values('zone__name').annotate(hf=Sum('high_fever'),
                    c=Sum('cough'), sh=Sum('shortness_of_breath'), t=Sum('tiredness'), st=Sum('sore_throat'))
    
    for entry in _5_symptoms:
        labels.append(entry['zone__name'])
        data.append(entry['hf'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def gender(request):
    labels = []
    data = []

    query = Symptom.objects.filter(high_fever=1, cough=1, shortness_of_breath=1, tiredness=1, sore_throat=1)
    g = query.values('gender').annotate(high_f=Sum('high_fever'), coug=Sum('cough'), 
                            shortness_of_b=Sum('shortness_of_breath'), tired=Sum('tiredness'), 
                            sore_thro=Sum('sore_throat'))
    for entry in g:
        labels.append(entry['gender'])
        data.append(entry['tired'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def gender_with_three_symptom(request):
    labels = []
    data = []

    query = Symptom.objects.filter(high_fever=1, cough=1, shortness_of_breath=1)
    _3_symptom_gender = query.values('gender').annotate(high_fever=Sum('high_fever'), cough=Sum('cough'),
                        shortness_of_breath=Sum('shortness_of_breath'))
    for entry in _3_symptom_gender:
        labels.append(entry['gender'])
        data.append(entry['high_fever'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def fever_chart(request):
    labels = []
    data = []
    queryset = Symptom.objects.values('zone__name').annotate(fever=Sum('high_fever'))
    for entry in queryset:
        labels.append(entry['zone__name'])
        data.append(entry['fever'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def shortness_of_breath(request):
    labels = []
    data = []

    queryset1 = Symptom.objects.values('zone__name').annotate(breath=Sum('shortness_of_breath'))
    for entry1 in queryset1:
        labels.append(entry1['zone__name'])
        data.append(entry1['breath'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def cough(request):
    labels = []
    data = []

    queryset2 = Symptom.objects.values('zone__name').annotate(cough=Sum('cough'))
    for entry2 in queryset2:
        labels.append(entry2['zone__name'])
        data.append(entry2['cough'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def all_symptoms(request):
    label_f = []
    label_c = []
    label_sh = []
    label_t = []
    label_s = []
    data_f = []
    data_c = []
    data_sh = []
    data_t = []
    data_s = []

    query1 = Symptom.objects.values('zone__name').annotate(high_fever=Sum('high_fever'))
    query2 = Symptom.objects.values('zone__name').annotate(cough=Sum('cough'))
    query3 = Symptom.objects.values('zone__name').annotate(shortness_of_breath=Sum('shortness_of_breath'))
    query4 = Symptom.objects.values('zone__name').annotate(tiredness=Sum('tiredness'))
    query5 = Symptom.objects.values('zone__name').annotate(sore_throat=Sum('sore_throat'))

    for entry in query1:
        label_f.append(entry['zone__name'])
        data_f.append(entry['high_fever'])

    for entry in query2:
        label_c.append(entry['zone__name'])
        data_c.append(entry['cough'])
    
    for entry in query3:
        label_sh.append(entry['zone__name'])
        data_sh.append(entry['shortness_of_breath'])

    for entry in query4:
        label_t.append(entry['zone__name'])
        data_t.append(entry['tiredness'])

    for entry in query5:
        label_s.append(entry['zone__name'])
        data_s.append(entry['sore_throat'])

    return JsonResponse(data={
        'label_f': label_f,
        'label_c': label_c,
        'label_sh': label_sh,
        'label_t': label_t,
        'label_s': label_s,
        'data_f': data_f,
        'data_c': data_c,
        'data_sh': data_sh,
        'data_t': data_t,
        'data_s': data_s,
    })