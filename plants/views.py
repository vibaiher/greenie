from django.http import Http404
from django.shortcuts import render

from .models import Plant

def index(request):
    plants = Plant.objects.order_by("-id")
    return render(request, "plants/index.html", { "plants": plants })

def detail(request, plant_id):
    try:
        plant = Plant.objects.get(pk=plant_id)
    except Plant.DoesNotExist:
        raise Http404("plant does not exist")
    return render(request, "plants/detail.html", { "plant": plant })
