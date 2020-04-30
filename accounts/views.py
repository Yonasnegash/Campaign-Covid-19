from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from symptom.models import Symptom, Region, Zone, Status
from .forms import SymptomForm, StatusForm

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    status = Status.objects.order_by('-submit_date').filter(user_id=request.user.id)
    symptom = Symptom.objects.order_by('-submit_date').filter(user_id=request.user.id)
    context = {
        'symptom': symptom,
        'status': status,
    }
    return render(request, 'accounts/dashboard.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def symptom(request):
    region_list = Region.objects.all()
    zone_list = Zone.objects.all()

    zone_list1 = Zone.objects.filter(region_id=1)
    zone_list2 = Zone.objects.filter(region_id=2)
    zone_list3 = Zone.objects.filter(region_id=3)
    zone_list4 = Zone.objects.filter(region_id=4)
    zone_list5 = Zone.objects.filter(region_id=5)
    zone_list6 = Zone.objects.filter(region_id=6)
    zone_list7 = Zone.objects.filter(region_id=7)
    zone_list8 = Zone.objects.filter(region_id=8)
    zone_list9 = Zone.objects.filter(region_id=9)
    zone_list10 = Zone.objects.filter(region_id=10)
    zone_list11 = Zone.objects.filter(region_id=11)
    
    
    context = {
        'region_list': region_list,
        'zone_list1': zone_list1,
        'zone_list2': zone_list2,
        'zone_list3': zone_list3,
        'zone_list4': zone_list4,
        'zone_list5': zone_list5,
        'zone_list6': zone_list6,
        'zone_list7': zone_list7,
        'zone_list8': zone_list8,
        'zone_list9': zone_list9,
        'zone_list10': zone_list10,
        'zone_list11': zone_list11,
    }
    return render(request, 'accounts/symptom.html', context)

def add_symptom(request):
    zone_id = None
    zone1 = None
    zone2 = None
    zone3 = None
    zone4 = None
    zone5 = None
    zone6 = None
    zone7 = None
    zone8 = None
    zone9 = None
    zone10 = None
    zone11 = None

    if request.method == 'POST':
        user_id = request.POST['user_id']
        username = request.POST['username']
        age = request.POST['age']
        gender = request.POST['gender']
        region = request.POST['region']
        zone1 = request.POST['zone1']
        zone2 = request.POST['zone2']
        zone3 = request.POST['zone3']
        zone4 = request.POST['zone4']
        zone5 = request.POST['zone5']
        zone6 = request.POST['zone6']
        zone7 = request.POST['zone7']
        zone8 = request.POST['zone8']
        zone9 = request.POST['zone9']
        zone10 = request.POST['zone10']
        zone11 = request.POST['zone11']
        phone = request.POST['phone']
        city = request.POST['city']
        shortness_of_breath = request.POST['shortness_of_breath']
        cough = request.POST['cough']
        fever = request.POST['fever']
        tiredness = request.POST['tiredness']
        sore_throat = request.POST['sore_throat']
        comment = request.POST['comment']

      
        integer_region = int(region)
        if integer_region == 1:
            zone = request.POST['zone1']
        if integer_region == 2:
            zone = request.POST['zone2']
        if integer_region == 3:
            zone = request.POST['zone3']
        if integer_region == 4:
            zone = request.POST['zone4']
        if integer_region == 5:
            zone = request.POST['zone5']
        if integer_region == 6:
            zone = request.POST['zone6']
        if integer_region == 7:
            zone = request.POST['zone7']
        if integer_region == 8:
            zone = request.POST['zone8']
        if integer_region == 9:
            zone = request.POST['zone9']
        if integer_region == 10:
            zone = request.POST['zone10']
        if integer_region == 11:
            zone = request.POST['zone11']
       

        # return render(request, 'accounts/symptom.html')

        if shortness_of_breath == "Yes":
            s_of_breath = 1
        else:
            s_of_breath = 0

        if cough == "Yes":
            c = 1
        else:
            c = 0
        
        if fever == "Yes":
            f = 1
        else:
            f = 0

        if tiredness == "Yes":
            t = 1
        else:
            t = 0

        if sore_throat == "Yes":
            sore_t = 1
        else:
            sore_t = 0

        if Symptom.objects.filter(name=username).exists():
            messages.error(request, 'You have already submitted your health condition!')
            return redirect('dashboard')
        else:
            symptom = Symptom(name=username, age=age, gender=gender, zone_id=zone, region_id=region, phone=phone, 
                        city=city, shortness_of_breath=s_of_breath, cough=c, high_fever=f, 
                        tiredness=t, sore_throat=sore_t, user_id=user_id, comment=comment)
            symptom.save()
            status = Status(name=username, shortness_of_breath=s_of_breath, cough=c, high_fever=f, 
                        tiredness=t, sore_throat=sore_t, user_id=user_id)
            status.save()
            messages.success(request, 'Success')
            return redirect('dashboard')
    else:
        return render(request, 'accounts/symptom.html')

def update(request, symptom_id):
    single_symptom = get_object_or_404(Symptom, pk=symptom_id)
    tobe_update = Symptom.objects.order_by('-submit_date')
  
    update = Symptom.objects.get(id=symptom_id)
    context = {
        'single_symptom': single_symptom,
        'tobe_update': tobe_update,
    }
    
    if request.method == 'POST':
        user_id = request.POST['user_id']
        shortness_of_breath = request.POST['shortness_of_breath']
        cough = request.POST['cough']
        fever = request.POST['fever']
        tiredness = request.POST['tiredness']
        sore_throat = request.POST['sore_throat']
        if shortness_of_breath == "Yes":
            s_of_breath = 1
        else:
            s_of_breath = 0

        if cough == "Yes":
            c = 1
        else:
            c = 0
        
        if fever == "Yes":
            f = 1
        else:
            f = 0

        if tiredness == "Yes":
            t = 1
        else:
            t = 0

        if sore_throat == "Yes":
            sore_t = 1
        else:
            sore_t = 0

        short_of_breath = update.shortness_of_breath
        co = update.cough
        h_f = update.high_fever
        tir = update.tiredness
        sor_t = update.sore_throat

        short_of_breath = s_of_breath
        co = c
        h_f = f
        tir = t
        sor_t = sore_t
        
        Symptom.objects.filter(id=symptom_id).update(shortness_of_breath=short_of_breath, cough=co, high_fever=h_f, tiredness=tir, sore_throat=sor_t)
        status = Status(name=update, shortness_of_breath=short_of_breath, cough=co, high_fever=h_f, 
                        tiredness=tir, sore_throat=sor_t, user_id=user_id)
        status.save()
        messages.success(request, 'Success')
        return redirect('dashboard')
    
    return render(request, 'accounts/update_symptom.html', context)

def update_symptom(request, symptom_id):

    form = StatusForm()

    context = {'form': form}

    return render(request, 'accounts/dashboard.html', context)
# class SymptomCreateView(CreateView):
#     model = Symptom
#     form_class = SymptomForm
#     success_url = reverse_lazy('symptom')

# class SymptomUpdateView(UpdateView):
#     model = Symptom
#     form_class = SymptomForm
#     success_url = reverse_lazy('Symptom')

# def load_zones(request):
#     region_id = request.GET.get('region')
#     zones = Zone.objects.filter(region_id=region_id).order_by('name')
#     return render(request, 'accounts/zone_dropdown_list_option.html', {'zones': zones})