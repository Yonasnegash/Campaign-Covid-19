from django.contrib import admin

from .models import Symptom, Region, Zone, Status

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    list_per_page = 25

admin.site.register(Region, RegionAdmin)

class ZoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    list_per_page = 25

admin.site.register(Zone, ZoneAdmin)

class SymptomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'cough','shortness_of_breath', 'high_fever', 'tiredness', 'sore_throat', 'zone_id', 'region_id')
    list_display_links = ('id', 'name',)
    list_editable = ('cough', 'shortness_of_breath', 'high_fever', 'tiredness', 'sore_throat')
    search_fields = ('name', 'city', 'phone')

admin.site.register(Symptom, SymptomAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    list_per_page = 25

admin.site.register(Status, StatusAdmin)