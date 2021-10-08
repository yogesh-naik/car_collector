from django.shortcuts import render
from django.views.generic.base import TemplateView
# This will import the class we are extending 
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView


from . models import CarManufacturer

# Create your views here.
class AllCars(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about_page.html"
#  #This is constructor
# class CarManufacturer:
#     def __init__(self, name, logo, Information):
#         self.name = name
#         self.logo = logo
#         self.Information = Information
        
#controller
class CarsList(TemplateView):
    template_name = "cars_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["all_Cars"] = CarManufacturer.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["all_Cars"] = CarManufacturer.objects.all()
            context["header"] = "Top USA Car Manufacturer"
        return context
    
class AddCar_Create(CreateView):
    model = CarManufacturer
    fields = ['name', 'logo', 'information']
    template_name = "car_create.html"
    success_url = "/cars/"  #redirect path
    
    
class CarDetail(DetailView):
    model = CarManufacturer
    template_name = "car_detail.html"
    
class CarUpdate(UpdateView):
    model = CarManufacturer
    fields = ['name', 'logo', 'information']
    template_name = "car_update.html"
    success_url = "/cars/"  #redirect path
    
    
class CarDelete(DeleteView):
    model = CarManufacturer
    template_name = "car_delete.html"
    success_url = "/cars/" #redirect path