from django.db import models

class Deconvolution(models.Model):
  user = models.CharField(max_length=150)
  spectra = models.IntegerField()
  date = models.DateField()