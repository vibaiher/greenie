from django.db import models

class Fertilizer(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    dose = models.CharField(max_length=32)
    frequency = models.IntegerField()

    def __str__(self):
        return self.name
    
    def npk(self):
        return f"{int(self.nitrogen)}-{int(self.phosphorus)}-{int(self.potassium)}"

class CultivationPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def fertilizers(self):
        return [cf.fertilizer for cf in self.cultivationplanfertilizer_set.all()]

class CultivationPlanFertilizer(models.Model):
    cultivation_plan = models.ForeignKey(CultivationPlan, on_delete=models.CASCADE)
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cultivation_plan.name} - {self.fertilizer.name}"
