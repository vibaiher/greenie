from datetime import timedelta
from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Plant, Task

@receiver(post_save, sender=Plant)
def create_initial_tasks(sender, instance, created, **kwargs):
    if created and instance.cultivation_plan:
        fertilizers = instance.cultivation_plan.fertilizers()
        for fertilizer in fertilizers:
            Task.objects.create(
                plant=instance,
                plan=instance.cultivation_plan,
                fertilizer=fertilizer,
                status='pending',
                suggested_date=timezone.now().date() + timedelta(days=fertilizer.frequency)
            )

@receiver(pre_save, sender=Plant)
def update_tasks_on_plan_change(sender, instance, **kwargs):
    if instance.pk:
        old_plant = Plant.objects.get(pk=instance.pk)
        if old_plant.cultivation_plan != instance.cultivation_plan:
            print("canceling!")
            tasks_to_cancel = old_plant.tasks.filter(status='pending')
            for task in tasks_to_cancel:
                task.status = 'canceled'
                task.save()
            
            fertilizers = instance.cultivation_plan.fertilizers()
            for fertilizer in fertilizers:
                Task.objects.create(
                    plant=instance,
                    plan=instance.cultivation_plan,
                    fertilizer=fertilizer,
                    status='pending',
                    suggested_date=timezone.now().date() + timedelta(days=fertilizer.frequency)
                )
