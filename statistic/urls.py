from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fever-chart/', views.fever_chart, name='fever-chart'),
    path('shortness-of-breath/', views.shortness_of_breath, name='shortness-of-breath'),
    path('cough/', views.cough, name='cough'),
]