from django.http import Http404
from django.shortcuts import render

from .models import Fertilizer

def index(request):
    fertilizers = Fertilizer.objects.order_by("-id")
    return render(request, "fertilizers/index.html", { "fertilizers": fertilizers })

def detail(request, fertilizer_id):
    try:
        fertilizer = Fertilizer.objects.get(pk=fertilizer_id)
    except Fertilizer.DoesNotExist:
        raise Http404("Fertilizer does not exist")
    return render(request, "fertilizers/detail.html", { "fertilizer": fertilizer })
