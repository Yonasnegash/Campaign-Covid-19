# Generated by Django 2.0.1 on 2020-04-09 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('symptom', '0003_auto_20200406_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='region',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='symptom.Region'),
        ),
    ]
