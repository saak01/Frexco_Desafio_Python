from unicodedata import name
from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=40, primary_key=True,default = '')
    
    
class Fruit(models.Model):
    name = models.CharField(max_length=40, primary_key=True,default = '')
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    