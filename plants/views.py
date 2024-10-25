from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Plant, Task

def index(request):
    plants = Plant.objects.order_by("-id")
    return render(request, "plants/index.html", { "plants": plants })

def detail(request, plant_id):
    try:
        plant = Plant.objects.get(pk=plant_id)
        cultivation_plan = plant.cultivation_plan
        tasks = Task.objects.filter(plant=plant, status="pending").order_by("suggested_date")
    except Plant.DoesNotExist:
        raise Http404("plant does not exist")
    return render(request, "plants/detail.html", { "plant": plant, "cultivation_plan": cultivation_plan, "tasks": tasks })

def complete_task(request, plant_id, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.status = 'completed'
    task.completed_date = timezone.now().date()
    task.save()
    task.create_next_task()
    return redirect('plants:detail', plant_id=task.plant.id)
