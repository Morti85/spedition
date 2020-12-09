from django.db import models

# Create your models here.
class Kunde(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name+" ("+self.id+")"

class Bestellung(models.Model):
    kundennummer = models.Charfield(max_length=50)
    produkte = models.CharField(max_length=50)
    def __str__(self):
        return self.kundennummer+" ("+self.id+")"