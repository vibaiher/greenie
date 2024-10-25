from datetime import timedelta
from django.utils import timezone
from django.core.management.base import BaseCommand
from plants.models import Plant, Task

class Command(BaseCommand):
    help = 'Create pending tasks for plants without tasks'

    def handle(self, *args, **kwargs):
        for plant in Plant.objects.all():
            if not plant.tasks.filter(status='pending').exists():
                fertilizers = plant.cultivation_plan.fertilizers()
                for index, fertilizer in enumerate(fertilizers):
                    suggested_date = timezone.now() + timedelta(days=index*7)

                    Task.objects.create(
                        plant=plant,
                        plan=plant.cultivation_plan,
                        fertilizer=fertilizer,
                        status='pending',
                        suggested_date=suggested_date.date()
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f'Created task for plant: {plant.name}, fertilizer: {fertilizer.name}, suggested date: {suggested_date.date()}'
                    ))

        self.stdout.write(self.style.SUCCESS('Pending tasks checked for all plants.'))
