# Generated by Django 5.1.2 on 2024-10-25 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fertilizers', '0002_cultivationplan_cultivationplanfertilizer'),
        ('plants', '0004_plant_cultivation_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=10)),
                ('suggested_date', models.DateField()),
                ('completed_date', models.DateField(blank=True, null=True)),
                ('fertilizer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='fertilizers.fertilizer')),
                ('plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='fertilizers.cultivationplan')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='plants.plant')),
            ],
        ),
    ]