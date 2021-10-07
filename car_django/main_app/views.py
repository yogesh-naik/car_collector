from django.shortcuts import render
from django.views.generic.base import TemplateView
from . models import CarManufacturer

# Create your views here.
class AllCars(TemplateView):
    template_name = "home.html"

#  #This is constructor
# class CarManufacturer:
#     def __init__(self, name, logo, Information):
#         self.name = name
#         self.logo = logo
#         self.Information = Information
        
#controller
class CarsList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_Cars"] = CarManufacturer.objects.all() # Here we are using the model to query the database for us.
        return context