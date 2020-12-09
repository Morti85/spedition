from django.db import models
import datetime

# Create your models here.
class Kunde(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name+" ("+str(self.id)+")"
    class Meta:
        verbose_name_plural = "Kunden"

class Bestellung(models.Model):
    kunde = models.ForeignKey(Kunde, on_delete=models.CASCADE)
    bestellung = models.TextField()
    datum = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.kunde.name+", "+self.bestellung+", "+str(self.datum)
    class Meta:
        verbose_name_plural = "Bestellungen"