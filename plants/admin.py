from django.contrib import admin

from .models import Plant

class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'alias', 'scientific_name', 'acquisition_date', 'cultivation_plan']
    search_fields = ['name', 'scientific_name', 'alias']
    list_filter = ['acquisition_date', 'cultivation_plan']

admin.site.register(Plant, PlantAdmin)
