from datetime import timedelta
from django.utils import timezone
from django.db import models

from fertilizers.models import Fertilizer, CultivationPlan

class Plant(models.Model):
    name = models.CharField(max_length=32)
    scientific_name = models.CharField(max_length=64)
    alias = models.CharField(max_length=32, null=True, blank=True)
    acquisition_date = models.DateField()
    cultivation_plan = models.ForeignKey(CultivationPlan, on_delete=models.SET_NULL, blank=True, null=True, related_name="plants")

    def __str__(self):
        if self.alias:
            return f"{self.name} - {self.alias}"
        return f"{self.name}"

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='tasks')
    plan = models.ForeignKey(CultivationPlan, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    suggested_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True, default=None)
    
    def create_next_task(self):
        next_task = Task.objects.create(
            plant=self.plant,
            plan=self.plan,
            fertilizer=self.fertilizer,
            status='pending',
            suggested_date=self.completed_date + timedelta(days=self.fertilizer.frequency)
        )
        next_task.save()

    def __str__(self):
        return f"Task for {self.plant.name} - Status: {self.status}"
