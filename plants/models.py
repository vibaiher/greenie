from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=32)
    scientific_name = models.CharField(max_length=64)
    alias = models.CharField(max_length=32, null=True, blank=True)
    acquisition_date = models.DateField()

    def __str__(self):
        if self.alias:
            return f"{self.name} - {self.alias}"
        return f"{self.name}"
