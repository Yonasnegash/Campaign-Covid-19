from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('initiator/', views.initiator, name='initiator'),
    path('fever-chart/', views.fever_chart, name='fever-chart'),
    path('shortness-of-breath/', views.shortness_of_breath, name='shortness-of-breath'),
    path('cough/', views.cough, name='cough'),
    path('three-symptoms', views.three_symptoms, name="three-symptoms"),
    path('five-symptoms', views.five_symptoms, name="five-symptoms"),
    path('gender', views.gender, name='gender'),
    path('gender-3-symptom', views.gender_with_three_symptom, name="gender-3-symptom"),
    path('all-symptoms', views.all_symptoms, name="all-symptoms"),
]
