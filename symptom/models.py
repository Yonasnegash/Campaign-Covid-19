from django.db import models
from datetime import datetime

class Region(models.Model):
    name = models.CharField(max_length=30)
    submit_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

class Zone(models.Model):
    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='regions')
    submit_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

class Symptom(models.Model):    
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name="zones")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    shortness_of_breath = models.IntegerField(default=0)
    cough = models.IntegerField(default=0)
    high_fever = models.IntegerField(default=0)
    tiredness = models.IntegerField(default=0)
    sore_throat = models.IntegerField(default=0)
    user_id = models.IntegerField(blank=True)
    comment = models.TextField(blank=True)
    submit_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=200)
    shortness_of_breath = models.IntegerField(default=0)
    cough = models.IntegerField(default=0)
    high_fever = models.IntegerField(default=0)
    tiredness = models.IntegerField(default=0)
    sore_throat = models.IntegerField(default=0)
    user_id = models.IntegerField(blank=True)
    submit_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name