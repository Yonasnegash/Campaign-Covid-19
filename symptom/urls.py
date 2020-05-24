from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register("symptomsapi", views.SymptomAPI)

urlpatterns = [
    path('', include(router.urls))
    # path('symptom', views.index, name='symptom')
]
