from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('symptom', views.symptom, name='symptom'),
    path('add-symptom', views.add_symptom, name='add-symptom'),
    path('<int:symptom_id>/', views.update, name='update'),
    path('<int:symptom_id>/', views.update_symptom, name='update-symptom'),
    # path('add/', views.SymptomCreateView.as_view(), name='symptom_add'),
    # path('ajax/load-zones/', views.load_zones, name='ajax_load_zones'),
]
