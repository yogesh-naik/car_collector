from django.contrib import admin
from .models import CarManufacturer
from .models import Carmodel
# Register your models here.
admin.site.register(CarManufacturer) # this line will add the model to the admin panel
admin.site.register(Carmodel)