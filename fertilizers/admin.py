from django.contrib import admin

from .models import Fertilizer, CultivationPlan, CultivationPlanFertilizer

class CultivationPlanFertilizerInline(admin.TabularInline):
    model = CultivationPlanFertilizer
    extra = 1
    fields = ['fertilizer']
    
class CultivationPlanAdmin(admin.ModelAdmin):
    inlines = [CultivationPlanFertilizerInline]
    list_display = ['name', 'description']
    search_fields = ['name']

admin.site.register(Fertilizer)
admin.site.register(CultivationPlan, CultivationPlanAdmin)
