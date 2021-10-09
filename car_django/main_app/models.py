from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CarManufacturer(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=250)
    information = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
      # Here is our new column
      #new auth code
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

#for One to many model
class Carmodel(models.Model):

    modelname = models.CharField(max_length=150)
    image = models.CharField(max_length=250)
    make = models.ForeignKey(CarManufacturer, on_delete=models.CASCADE, related_name="carmodels")

    def __str__(self):
        return self.modelname