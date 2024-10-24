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
